module \74283_1x1ADD4 (A, B, CI, S, CO);

input [3:0] A;
input [3:0] B;
input CI;
output [3:0] S;
output CO;

assign {CO, S} = A + B + CI;

endmodule
