74XX_SRC := $(wildcard *.v) 74series.v

74series.v: 74series.lib
	yosys -q -p "read_liberty $<" -p "write_verilog $@"

.PHONY: format
format: $(74XX_SRC) $(wildcard sim/*.v) $(wildcard test/*.v)
	verible-verilog-format --inplace $^

#
# Tests
#
test: \
	test/and_tb.test

test/%_74.v: test/%.v $(74XX_SRC) synth_74.ys
	yosys -q -s synth_74.ys -p "write_verilog $@" $<

test/%.stat: test/%_74.v
	yosys -q -s synth_74.ys -p "tee -o $@ stat" $<

test/%_74.dot: test/%_74.v 74series.v
	yosys -q -s synth_74.ys -p "show -lib 74series.v -width -prefix $(basename $@)" $^

test/%.out: test/%.stat
	./ic_count.py $^ > $@

test/%.test: test/%.out test/%.spec
	diff $^

#
# Statistics
#
stat: \
	stat/VexRiscv.stat \
	stat/arlet_6502.stat \
	stat/axilxbar.stat \
	stat/cordic_10_16.stat \
	stat/picorv32.stat \
	stat/shifter64.stat \
	stat/smartbextdep.stat

stat/%.stat: benchmarks/%.v $(74XX_SRC) synth_74.ys
	yosys -q -s synth_74.ys -p "tee -o $@ stat" $<

#
# Simulation
#
sim: \
	sim/cic5.vcd \
	sim/counter.vcd \
	sim/dspmac_16_40.vcd \
	sim/picorv32.vcd \
	sim/pwm256.vcd \
	sim/sddac.vcd
	
benchmarks/%.v: ;

sim/%.v: benchmarks/%.v 74series.lib 74_models.v 74_adder.v 74_dffe.v 74_mux.v 74_cmp.v synth_74.ys
	yosys -q -s synth_74.ys -p "write_verilog $@" $<

sim/%.vvp: sim/%.v benchmarks/%_tb.v 74series.v 74_models.v
	iverilog -o $@ $^

sim/%.vcd: sim/%.vvp
	vvp $<

clean:
	rm -f \
		sim/*.{v,vvp,vcd} \
		test/*.{_74.v,dot,stat,out,pid}
