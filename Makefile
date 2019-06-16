.PHONY: all

all: 74series.lib VexRiscv.v picorv32.v
	yosys -p "read_verilog picorv32.v; hierarchy -top picorv32; flatten; synth; dfflibmap -liberty 74series.lib; abc -liberty 74series.lib; tee -o picorv32.stat stat"
	yosys -p "read_verilog VexRiscv.v; hierarchy -top VexRiscv; flatten; synth; dfflibmap -liberty 74series.lib; abc -liberty 74series.lib; tee -o vexriscv.stat stat"
