module dff_tb (
    input clk,
    input d,
    output reg q,
    output reg qhat
);
  always @(posedge clk) begin
    q = d;
    qhat = !d;
  end
endmodule
