module \74HC85_1x1CMP4 (A, B, Li, Ei, Gi, Lo, Eo, Go);

input [3:0] A;
input [3:0] B;
input Li, Ei, Gi;
output Lo, Eo, Go;

assign Lo = (A < B) || (A == B && !Gi && !Ei);
assign Go = (A > B) || (A == B && !Li && !Ei);
assign Eo = (A == B) && Ei;

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

module \74AC164_1x1SHREG8 (DS, MRn, CP, Q);

input [1:0] DS;
input MRn, CP;
output reg [7:0] Q;

always @(posedge CP, negedge MRn) begin
  if (MRn==1'b0)
    Q = 8'h00;
  else
    Q = {&DS, Q[6:0]};
end

endmodule
