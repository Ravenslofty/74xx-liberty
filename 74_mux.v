(* techmap_celltype = "$_MUX4_" *)
module _80_74153_mux4 (A, B, C, D, S, T, Y);

input A, B, C, D, S, T;
output Y;

\74153_2x1MUX4 _TECHMAP_REPLACE_ (
    .S({T, S}),
    .D({D, C, B, A}),
    .O(Y)
);

endmodule

(* techmap_celltype = "$_MUX8_" *)
module _80_74151_mux8 (A, B, C, D, E, F, G, H, S, T, U, Y);

input A, B, C, D, E, F, G, H, S, T, U;
output Y;

\74151_1x1MUX8 _TECHMAP_REPLACE_ (
    .S({U, T, S}),
    .D({H, G, F, E, D, C, B, A}),
    .O(Y)
);

endmodule

(* techmap_celltype = "$_MUX16_" *)
module _80_74150_mux16 (A, B, C, D, E, F, G, H, I, J, K, L, M, N, O, P, S, T, U, V, Y);

input A, B, C, D, E, F, G, H, I, J, K, L, M, N, O, P, S, T, U, V;
output Y;

\74150_1x1MUX16 _TECHMAP_REPLACE_ (
    .S({V, U, T, S}),
    .D({P, O, N, M, L, K, J, I, H, G, F, E, D, C, B, A}),
    .O(Y)
);

endmodule
