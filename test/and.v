module and_tb (
    input [3:0] a,
    output s
);
  assign s = &a;
endmodule
