import skidl
import json
import sys
import os.path
import pprint
import pdb

def get_toplevel(data):
    top = None
    for mod in data['modules'].values():
        if 'top' in mod['attributes']:
            top = mod
            break
    return top

# create KiCad nets
VCC = skidl.Net('VCC')
GND = skidl.Net('GND')

def create_nets(top):
    nets = {}
    nets['0']=GND
    nets['1']=VCC
    for name, net in top['netnames'].items():
        for bit in net['bits']:
            if not bit in nets:
                nets[bit] = skidl.Net(name)

    return nets

def group_by(key, data):
    groups = {}
    for val in data:
        groups.setdefault(key(val), []).append(val)
    return groups

def make_abc(fnew, mapping, instances, nets):
    chip = fnew()
    idx = 0
    for inst in instances:
        if not hasattr(chip, next(iter(mapping)).format(idx)):
            chip = fnew()
            idx = 0

        for ch, nl in mapping.items():
            chip[ch.format(idx)] += nets[inst['connections'][nl][0]]
        idx+=1

def make_techmap(fnew, mapping, instances, nets, base=0):
    for inst in instances:
        chip = fnew()
        for ch, nl in mapping.items():
            for i, a in enumerate(inst['connections'][nl]):
                chip[ch.format(i+base)] += nets[a]


def new_74374():
    "8-bit DFF"
    chip = skidl.Part('74xx', '74LS374', footprint="Package_DIP:DIP-20_W7.62mm")
    chip.VCC += VCC
    chip.GND += GND
    chip.OE += GND # enable
    return chip

def new_74273():
    "8-bit DFF with clear"
    chip = skidl.Part('74xx', '74LS273', footprint="Package_DIP:DIP-20_W7.62mm")
    chip.VCC += VCC
    chip.GND += GND
    return chip

def new_74283():
    "4-bit adder"
    chip = skidl.Part('74xx', '74LS283', footprint="Package_DIP:DIP-16_W7.62mm")
    chip.VCC += VCC
    chip.GND += GND
    return chip

def new_7485():
    "4-bit magnitude comparator"
    chip = skidl.Part('74xx', '74LS85', footprint="Package_DIP:DIP-16_W7.62mm")
    chip.VCC += VCC
    chip.GND += GND
    return chip

def pin_getter(*args):
    return lambda chip: tuple(chip['connections'][arg][0] for arg in args)

def create_chips(chip_types, nets):
    for typ, chips in chip_types.items():
        if typ == '\\74AC16374_16x1DFF':
            mapping = {"D{}":"D", "O{}":"Q", "Cp": "CLK"}
            clocks = group_by(pin_getter("CLK"), chips)
            for instances in clocks.values():
                make_abc(new_74374, mapping, instances, nets)
        elif typ == '\\74AC273_8x1DFFR':
            mapping = {"D{}":"D", "Q{}":"Q", "Cp": "CLK", "~Mr": "C"}
            clocks = group_by(pin_getter("CLK", "C"), chips)
            for instances in clocks.values():
                make_abc(new_74273, mapping, instances, nets)
        elif typ == '\\74AC283_1x1ADD4':
            mapping = {"C0": "CI", "C4": "CO", "A{}": "A", "B{}": "B", "S{}": "S"}
            make_techmap(new_74283, mapping, chips, nets, 1)
        elif typ == '\\74HC85_1x1CMP4':
            mapping = {"A{}": "A", "B{}": "B",
                       "Ia=b": "Ei", "Oa=b": "Eo",
                       "Ia>b": "Gi", "Oa>b": "Go",
                       "Ia<b": "Li", "Oa<b": "Lo"}
            make_techmap(new_7485, mapping, chips, nets, 0)
        else:
            raise Exception("%s not handled" % typ)

def generate_netlist():
    skidl.ERC()
    name, ext = os.path.splitext(sys.argv[1])
    skidl.generate_netlist(file_=name+'.net')

if __name__ == '__main__':
    with open(sys.argv[1]) as f:
        data = json.load(f)

    top = get_toplevel(data)
    nets = create_nets(top)
    chip_types = group_by(lambda cell: cell['type'], top['cells'].values())
    create_chips(chip_types, nets)
    generate_netlist()
