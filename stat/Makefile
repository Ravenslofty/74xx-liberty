.PHONY: all

all: ../74series.lib VexRiscv.stat picorv32.stat shifter64.stat smartbextdep.stat cordic_10_16.stat 

%.stat: ../benchmarks/%.v ../74series.lib
	yosys -p "read_verilog $<; hierarchy -auto-top; proc; flatten; opt; wreduce; opt; read_verilog -lib ../74_models.v; techmap -map ../74283.v; synth -run :fine; opt -full; memory_map; opt -full; techmap -map +/techmap.v; opt; dfflibmap -liberty ../74series.lib; abc -liberty ../74series.lib; tee -o $@ stat"
