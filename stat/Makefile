.PHONY: all

all: ../74series.lib VexRiscv.stat picorv32.stat shifter64.stat smartbextdep.stat cordic_10_16.stat arlet_6502.stat

%.stat: ../benchmarks/%.v ../74series.lib ../74_models.v ../74_adder.v ../74_mux.v ../synth_74.ys
	yosys -s ../synth_74.ys -p "tee -o $@ stat" $<
