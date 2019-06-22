.PHONY: all clean sim_counter
.SECONDARY:

all: sim_counter sim_picorv32

%.v: ../%.lib
	yosys -q -p "read_liberty $<" -p "write_verilog $@"

../benchmarks/%.v: ;

%.v: ../benchmarks/%.v ../74series.lib ../74_models.v ../74_adder.v ../74_dffe.v ../74_mux.v ../synth_74.ys
	yosys -q -s ../synth_74.ys -p "write_verilog $@" $<

%.vvp: %.v ../benchmarks/%_tb.v 74series.v ../74_models.v
	iverilog -o $@ $^

sim_counter: counter.vvp
	vvp counter.vvp

sim_picorv32: picorv32.vvp
	vvp picorv32.vvp

clean:
	rm *.v *.vvp *.vcd
