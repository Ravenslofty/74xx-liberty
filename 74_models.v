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
