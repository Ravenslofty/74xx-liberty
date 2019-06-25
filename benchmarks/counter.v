// Quick blinking a LED

/* module */
module counter (
  input rst,
  input clk,
  output led
    
);

    /* reg */
    reg [7:0] counter = 0;
    reg state;
    
    /* assign */
    assign led = counter[7];
    
    /* always */
    always @ (posedge clk or negedge rst) begin
      if (!rst) begin
        counter <= 0;
      end else begin
        counter <= counter + 1;
      end
    end

endmodule
