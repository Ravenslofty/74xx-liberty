module \74AC151_1x1MUX8 (D, S, O);

input [7:0] D;
input [2:0] S;
output O;

assign O = S[2] ? (S[1] ? (S[0] ? D[7] : D[6])
                        : (S[0] ? D[5] : D[4]))
                : (S[1] ? (S[0] ? D[3] : D[2])
                        : (S[0] ? D[1] : D[0]));

endmodule

module \74AC153_2x1MUX4 (D, S, O);

input [3:0] D;
input [1:0] S;
output O;

assign O = S[1] ? (S[0] ? D[3] : D[2])
                : (S[0] ? D[1] : D[0]);

endmodule

module \74AC283_1x1ADD4 (A, B, CI, S, CO);

input [3:0] A;
input [3:0] B;
input CI;
output [3:0] S;
output CO;

assign {CO, S} = A + B + CI;

endmodule

module \74AC377_8x1DFFE (D, CE, CP, Q);

input D, CE, CP;
output reg Q;

always @(posedge CP) begin
    if (!CE) Q <= D;
end

endmodule

module \74HC688_1x1EQ8 (A, B, E, Q);

input [7:0] A;
input [7:0] B;
input E;
output Q;

assign Q = E || !(A == B);

endmodule
