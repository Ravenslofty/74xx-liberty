.PHONY: all

all: ../74series.lib VexRiscv.stat picorv32.stat shifter64.stat smartbextdep.stat cordic_10_16.stat \
    arlet_6502.stat axilxbar.stat

%.stat: ../benchmarks/%.v $(wildcard ../*.v) ../synth_74.ys
	yosys -q -s ../synth_74.ys -p "tee -o $@ stat" $<
