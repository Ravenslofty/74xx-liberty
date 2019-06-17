module \74150_1x1MUX16 (D, S, O);

input [15:0] D;
input [3:0] S;
output O;

assign O = S[3] ? (S[2] ? (S[1] ? (S[0] ? D[15] : D[14])
                                : (S[0] ? D[13] : D[12]))
                        : (S[1] ? (S[0] ? D[11] : D[10])
                                : (S[0] ? D[9] : D[8])))
                : (S[2] ? (S[1] ? (S[0] ? D[7] : D[6])
                                : (S[0] ? D[5] : D[4]))
                        : (S[1] ? (S[0] ? D[3] : D[2])
                                : (S[0] ? D[1] : D[0])));

endmodule

module \74151_1x1MUX8 (D, S, O);

input [7:0] D;
input [2:0] S;
output O;

assign O = S[2] ? (S[1] ? (S[0] ? D[7] : D[6])
                        : (S[0] ? D[5] : D[4]))
                : (S[1] ? (S[0] ? D[3] : D[2])
                        : (S[0] ? D[1] : D[0]));

endmodule

module \74153_2x1MUX4 (D, S, O);

input [3:0] D;
input [1:0] S;
output O;

assign O = S[1] ? (S[0] ? D[3] : D[2])
                : (S[0] ? D[1] : D[0]);

endmodule

module \74283_1x1ADD4 (A, B, CI, S, CO);

input [3:0] A;
input [3:0] B;
input CI;
output [3:0] S;
output CO;

assign {CO, S} = A + B + CI;

endmodule
