module add5 (
    input [7:0] a,
    input [7:0] b,
    output [7:0] sum,
    output cf
);
  assign {cf, sum} = a + b;
endmodule
