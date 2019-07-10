
(* techmap_celltype = "$__SHREG_DFF_P_" *)
module _80_74AC164(input C, D, output Q);
parameter DEPTH = 1;

wire [7:0] QBUF;
wire [1:0] DS;

assign DS = {1'b1, D};
assign Q = QBUF[DEPTH-1];

\74AC164_1x1SHREG8 _TECHMAP_REPLACE_ (
    .DS(DS),
    .MRn(1'b1),
    .CP(C),
    .Q(Q),
);
endmodule

(* techmap_celltype = "$__SHREG_DFFE_PP_" *)
module _80_74AC164E(input C, D, E, output Q);
parameter DEPTH = 1;

wire [7:0] QBUF;
wire [1:0] DS;

assign DS = {D, E};
assign Q = QBUF[DEPTH-1];

\74AC164_1x1SHREG8 _TECHMAP_REPLACE_ (
    .DS(DS),
    .MRn(1'b1),
    .CP(C),
    .Q(Q),
);
endmodule
