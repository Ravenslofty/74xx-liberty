import skidl
import json
import sys
import os.path
import pprint
import pdb

VCC = skidl.Net('VCC')
GND = skidl.Net('GND')

def make_74374(instances, nets):
    template = skidl.Part('74xx', '74LS374', footprint="Package_DIP:DIP-20_W7.62mm", dest=skidl.TEMPLATE)
    chip = template()
    chip.VCC += VCC
    chip.GND += VCC
    idx = 0
    for inst in instances:
        if not hasattr(chip, "D%d"%idx):
            chip = template()
            chip.VCC += VCC
            chip.GND += GND
            chip.OE += GND # enable
            idx = 0

        chip['D%d'%idx] += nets[inst['connections']['D'][0]]
        chip['O%d'%idx] += nets[inst['connections']['Q'][0]]
        #TODO multiple clocks?
        chip['CP'] += nets[inst['connections']['CLK'][0]]
        idx+=1

def make_74283(instances, nets):
    template = skidl.Part('74xx', '74LS283', footprint="Package_DIP:DIP-16_W7.62mm", dest=skidl.TEMPLATE)
    for inst in instances:
        chip = template()
        chip.VCC += VCC
        chip.GND += GND
        chip['C0'] += nets[inst['connections']['CI'][0]]
        chip['C4'] += nets[inst['connections']['CO'][0]]
        for i, a in enumerate(inst['connections']['A']):
            chip['A%d'%(i+1)] += nets[a]
        for i, b in enumerate(inst['connections']['B']):
            chip['B%d'%(i+1)] += nets[b]
        for i, s in enumerate(inst['connections']['S']):
            chip['S%d'%(i+1)] += nets[s]

# load Yosys netlist
with open(sys.argv[1]) as f:
    data = json.load(f)

# Find top-level module
top = None
for mod in data['modules'].values():
    if 'top' in mod['attributes']:
        top = mod
        break

# create KiCad nets
nets = {}
nets['0']=GND
nets['1']=VCC
for name, net in top['netnames'].items():
    for bit in net['bits']:
        if not bit in nets:
            nets[bit] = skidl.Net(name)

# sort Yosys cells by type
types = {}
for cell in top['cells'].values():
    types.setdefault(cell['type'], []).append(cell)

# creat KiCad chips
make_74374(types['\\74AC16374_16x1DFF'], nets)
make_74283(types['\\74AC283_1x1ADD4'], nets)

skidl.ERC()
name, ext = os.path.splitext(sys.argv[1])
skidl.generate_netlist(file_=name+'.net')
