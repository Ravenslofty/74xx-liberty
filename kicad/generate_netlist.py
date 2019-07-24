import skidl
import json
import sys
import os.path
import pprint
import pdb

from parts import *

def get_toplevel(data):
    top = None
    for mod in data['modules'].values():
        if 'top' in mod['attributes']:
            top = mod
            break
    return top


def create_nets(top):
    nets = {}
    nets['0']=GND
    nets['1']=VCC
    for name, net in top['netnames'].items():
        for bit in net['bits']:
            if not bit in nets:
                net = skidl.Net(name)
                nets[bit] = net
            else:
                net = nets[bit]
            # suppress ERC warnings about unconnected pins
            if name in top['ports'] and top['ports'][name]['direction']=='input':
                net.drive = skidl.POWER

    return nets

def group_by(key, data):
    groups = {}
    for val in data:
        groups.setdefault(key(val), []).append(val)
    return groups

def make_abc(fnew, mapping, instances, nets, base=0):
    new_cap()
    chip = fnew()
    idx = base
    for inst in instances:
        if not chip[next(iter(mapping)).format(idx)]:
            new_cap()
            chip = fnew()
            idx = base

        for ch, nl in mapping.items():
            try:
                chip[ch.format(idx)] += nets[inst['connections'][nl][0]]
            except TypeError:
                print("Pin", ch.format(idx), "not found")
                print(chip)
                raise

        idx+=1

    # suppress ERC warnings about unconnected pins
    while chip[next(iter(mapping)).format(idx)]:
        for ch, nl in mapping.items():
            if "{}" in ch: #only numbered pins
                chip[ch.format(idx)] += NC
        idx+=1

def make_techmap(fnew, mapping, instances, nets, base=0):
    for inst in instances:
        new_cap()
        chip = fnew()
        for ch, nl in mapping.items():
            for i, a in enumerate(inst['connections'][nl]):
                chip[ch.format(i+base)] += nets[a]

def pin_getter(*args):
    return lambda chip: tuple(chip['connections'][arg][0] for arg in args)

def create_chips(chip_types, nets):
    for typ, chips in chip_types.items():
        if typ == '\\74AC16374_16x1DFF':
            mapping = {"D{}":"D", "O{}":"Q", "Cp": "CLK"}
            clocks = group_by(pin_getter("CLK"), chips)
            for instances in clocks.values():
                make_abc(new_74374, mapping, instances, nets)
        elif typ == '\\74AC377_8x1DFFE':
            mapping = {"D{}":"D", "Q{}":"Q", "~E": "CE", "CP": "CP"}
            clocks = group_by(pin_getter("CP", "CE"), chips)
            for instances in clocks.values():
                make_abc(new_74377, mapping, instances, nets)
        elif typ == '\\74AC273_8x1DFFR':
            mapping = {"D{}":"D", "Q{}":"Q", "Cp": "CLK", "~Mr": "C"}
            clocks = group_by(pin_getter("CLK", "C"), chips)
            for instances in clocks.values():
                make_abc(new_74273, mapping, instances, nets)
        elif typ == '\\74AC11074_2x1DFFSR':
            mapping = {"D{}":"D", "Q{}":"Q", "C{}": "CLK", "~R{}": "C", "~S": "P"}
            make_abc(new_7474, mapping, chips, nets, 1)
        elif typ == '\\74AC11257_4x1MUX2':
            mapping = {"{}A": "A", "{}B": "B", "{}Y": "Y", "S": "S"}
            select = group_by(pin_getter("S"), chips)
            for instances in select.values():
                make_abc(new_74257, mapping, instances, nets, 1)
        elif typ == '\\74AC158_4x1MUXI2':
            mapping = {"{}A": "A", "{}B": "B", "{}Y": "Y", "S": "S"}
            select = group_by(pin_getter("S"), chips)
            for instances in select.values():
                make_abc(new_74158, mapping, instances, nets, 1)
        elif typ == '\\74AC153_2x1MUX4':
            mapping = {"{}A": "A", "{}B": "B", "{}C": "C", "{}D": "D",
                       "{}Y": "Y", "S0": "S0", "S1": "S1"}
            select = group_by(pin_getter("S0", "S1"), chips)
            for instances in select.values():
                make_abc(new_74153, mapping, instances, nets, 1)
        elif typ == '\\74AC151_1x1MUX8':
            mapping = {"I0": "A", "I1": "B", "I2": "C", "I3": "D",
                       "I4": "E", "I5": "F", "I6": "G", "I7": "H",
                       "Z": "Y", "S0": "S0", "S1": "S1", "S2": "S2"}
            select = group_by(pin_getter("S0", "S1", "S2"), chips)
            for instances in select.values():
                #ABC but only one mux per chip
                make_techmap(new_74151, mapping, instances, nets)
        elif typ == '\\74AC151_1x1MUXI8':
            mapping = {"I0": "A", "I1": "B", "I2": "C", "I3": "D",
                       "I4": "E", "I5": "F", "I6": "G", "I7": "H",
                       "~Z": "Y", "S0": "S0", "S1": "S1", "S2": "S2"}
            select = group_by(pin_getter("S0", "S1", "S2"), chips)
            for instances in select.values():
                #ABC but only one mux per chip
                make_techmap(new_74151, mapping, instances, nets)
        elif typ == '\\74AC11086_4x1XOR2':
            mapping = {"{}A": "A", "{}B": "B", "{}Y": "Y"}
            make_abc(new_7486, mapping, chips, nets, 1)
        elif typ == '\\74AC11004_6x1NOT':
            mapping = {"{}A": "A", "{}Y": "Y"}
            make_abc(new_7404, mapping, chips, nets, 1)
        elif typ == '\\74AC02_4x1NOR2':
            mapping = {"{}A": "A", "{}B": "B", "{}Y": "Y"}
            make_abc(new_7402, mapping, chips, nets, 1)
        elif typ == '\\74AC11_3x1AND3':
            mapping = {"{}A": "A", "{}B": "B", "{}C": "C", "{}Y": "Y"}
            make_abc(new_7411, mapping, chips, nets, 1)
        elif typ == '\\74AC10_3x1NAND3':
            mapping = {"{}A": "A", "{}B": "B", "{}C": "C", "{}Y": "Y"}
            make_abc(new_7410, mapping, chips, nets, 1)
        elif typ == '\\74AC20_2x1NAND4':
            mapping = {"{}A": "A", "{}B": "B", "{}C": "C", "{}D": "D", "{}Y": "Y"}
            make_abc(new_7420, mapping, chips, nets, 1)
        elif typ == '\\74AC11032_4x1OR2':
            mapping = {"{}A": "A", "{}B": "B", "{}Y": "Y"}
            make_abc(new_7432, mapping, chips, nets, 1)
        elif typ == '\\74AC11008_4x1AND2':
            mapping = {"{}A": "A", "{}B": "B", "{}Y": "Y"}
            make_abc(new_7408, mapping, chips, nets, 1)
        elif typ == '\\74AC11000_4x1NAND2':
            mapping = {"{}A": "A", "{}B": "B", "{}Y": "Y"}
            make_abc(new_7400, mapping, chips, nets, 1)
        elif typ == '\\74AC11244_8x1BUF':
            mapping = {"A{}": "A", "Y{}": "Y"}
            make_abc(new_74244, mapping, chips, nets, 1)
        elif typ == '\\74AC283_1x1ADD4':
            mapping = {"C0": "CI", "C4": "CO", "A{}": "A", "B{}": "B", "S{}": "S"}
            make_techmap(new_74283, mapping, chips, nets, 1)
        elif typ == '\\74HC85_1x1CMP4':
            mapping = {"A{}": "A", "B{}": "B",
                       "Ia=b": "Ei", "Oa=b": "Eo",
                       "Ia>b": "Gi", "Oa>b": "Go",
                       "Ia<b": "Li", "Oa<b": "Lo"}
            make_techmap(new_7485, mapping, chips, nets, 0)
        elif typ == '\\74HC688_1x1EQ8':
            mapping = {"P{}": "A", "R{}": "B", "G": "E", "P=R": "Q"}
            make_techmap(new_74688, mapping, chips, nets, 0)
        elif typ == '\\74AC161_1x1COUNT4':
            mapping = {"D{}": "A", "Q{}": "Q", "~PE": "LOAD", "CET": "ENT", "TC": "RCO", "CP": "CLK"}
            make_techmap(new_74161, mapping, chips, nets, 0)
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
