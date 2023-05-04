module alu (
    input [7:0] a,
    input [7:0] b,
    input clk,
    input fi,
    input su,
    output [7:0] s,
    output reg cf,
    output reg zf
);
  wire _cf;

  assign {_cf, s} = a + (b ^ {8{su}});

  always @(posedge clk) begin
    if (fi) begin
      cf = _cf;
      zf = s == 0;
    end
  end
endmodule
