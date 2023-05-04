module reg8 (
    input [7:0] data_i,
    input we,
    input oe,
    input clk,
    output [7:0] data_o
);
  reg [7:0] data;

  always @(posedge clk) begin
    if (we) begin
      data = data_i;
    end
  end

  assign data_o = oe ? data : 8'b0;
endmodule
