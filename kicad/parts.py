import skidl

# create KiCad nets
VCC = skidl.Net('VCC')
VCC.drive = skidl.POWER
GND = skidl.Net('GND')
GND.drive = skidl.POWER

def new_cap():
    "a decoupling capacitor"
    chip = skidl.Part('Device', 'C', footprint="Capacitor_THT:C_Disc_D4.7mm_W2.5mm_P5.00mm")
    chip[1] += VCC
    chip[2] += GND

def new_74374():
    "8-bit DFF"
    chip = skidl.Part('74xx', '74LS374', footprint="Package_DIP:DIP-20_W7.62mm")
    chip.VCC += VCC
    chip.GND += GND
    chip.OE += GND # enable
    return chip

def new_74377():
    "8-bit DFFE"
    chip = skidl.Part('74xx', '74LS377', footprint="Package_DIP:DIP-20_W7.62mm")
    chip.VCC += VCC
    chip.GND += GND
    return chip

def new_74244():
    "8-bit buffer"
    chip = skidl.Part('74xx', '74LS244', footprint="Package_DIP:DIP-20_W7.62mm")
    chip.VCC += VCC
    chip.GND += GND
    chip.OE0 += GND # enable
    chip.OE1 += GND # enable
    return chip

def new_74257():
    "quad 2-1 MUX"
    chip = skidl.Part('74xx', '74LS257', footprint="Package_DIP:DIP-16_W7.62mm")
    chip.VCC += VCC
    chip.GND += GND
    chip.OE += GND # enable
    return chip

def new_74158():
    "quad 2-1 MUX, inverted"
    chip = skidl.Part('74xx', '74LS158', footprint="Package_DIP:DIP-16_W7.62mm")
    chip.VCC += VCC
    chip.GND += GND
    chip.OE += GND # enable
    return chip

def new_74153():
    "dual 4-1 MUX"
    chip = skidl.Part('74xx', '74LS153', footprint="Package_DIP:DIP-16_W7.62mm")
    chip.VCC += VCC
    chip.GND += GND
    chip['0E'] += GND # enable
    chip['1E'] += GND # enable
    return chip

def new_74151():
    "single 8-1 MUX"
    chip = skidl.Part('74xx', '74LS151', footprint="Package_DIP:DIP-16_W7.62mm")
    chip.VCC += VCC
    chip.GND += GND
    chip['~E'] += GND # enable
    return chip

def new_74273():
    "8-bit DFF with clear"
    chip = skidl.Part('74xx', '74LS273', footprint="Package_DIP:DIP-20_W7.62mm")
    chip.VCC += VCC
    chip.GND += GND
    return chip

def new_7474():
    "dual DFFSR"
    chip = skidl.Part('74xx', '74LS74', footprint="Package_DIP:DIP-14_W7.62mm")
    chip.VCC += VCC
    chip.GND += GND
    return chip

def new_7486():
    "quad XOR"
    chip = skidl.Part('74xx', '74LS86', footprint="Package_DIP:DIP-14_W7.62mm")
    chip.VCC += VCC
    chip.GND += GND
    return chip

def new_7404():
    "hex NOT"
    chip = skidl.Part('74xx', '74LS04', footprint="Package_DIP:DIP-14_W7.62mm")
    chip.VCC += VCC
    chip.GND += GND
    return chip

def new_7402():
    "quad NOR"
    chip = skidl.Part('74xx', '74LS02', footprint="Package_DIP:DIP-14_W7.62mm")
    chip.VCC += VCC
    chip.GND += GND
    return chip

def new_7400():
    "quad NOR"
    chip = skidl.Part('74xx', '74LS00', footprint="Package_DIP:DIP-14_W7.62mm")
    chip.VCC += VCC
    chip.GND += GND
    return chip

def new_7411():
    "triple AND3"
    chip = skidl.Part('74xx', '74LS11', footprint="Package_DIP:DIP-14_W7.62mm")
    chip.VCC += VCC
    chip.GND += GND
    return chip

def new_7410():
    "triple NAND3"
    chip = skidl.Part('74xx', '74LS10', footprint="Package_DIP:DIP-14_W7.62mm")
    chip.VCC += VCC
    chip.GND += GND
    return chip

def new_7432():
    "quad OR"
    chip = skidl.Part('74xx', '74LS32', footprint="Package_DIP:DIP-14_W7.62mm")
    chip.VCC += VCC
    chip.GND += GND
    return chip

def new_7408():
    "quad AND"
    chip = skidl.Part('74xx', '74LS08', footprint="Package_DIP:DIP-14_W7.62mm")
    chip.VCC += VCC
    chip.GND += GND
    return chip

def new_7420():
    "dual NAND4"
    chip = skidl.Part('74xx', '74LS20', footprint="Package_DIP:DIP-14_W7.62mm")
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

def new_74688():
    "8-bit magnitude comparator"
    chip = skidl.Part('74xx', '74LS688', footprint="Package_DIP:DIP-20_W7.62mm")
    chip.VCC += VCC
    chip.GND += GND
    return chip
