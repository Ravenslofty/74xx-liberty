
autoidx 22

attribute \cells_not_processed 1
attribute \src "74_extract.v:16"
module \_74xx_counter16

  attribute \src "74_extract.v:22"
  wire width 16 $0\counter[15:0]

  attribute \src "74_extract.v:26"
  wire width 16 $add$74_extract.v:26$6_Y

  attribute \src "74_extract.v:18"
  wire input 2 \clk

  attribute \src "74_extract.v:20"
  wire width 16 output 4 \counter

  attribute \src "74_extract.v:19"
  wire width 16 input 3 \preset

  attribute \src "74_extract.v:17"
  wire input 1 \rst

  attribute \src "74_extract.v:26"
  cell $add $add$74_extract.v:26$6
    parameter \A_SIGNED 0
    parameter \A_WIDTH 16
    parameter \B_SIGNED 0
    parameter \B_WIDTH 1
    parameter \Y_WIDTH 16
    connect \A \counter
    connect \B 1'1
    connect \Y $add$74_extract.v:26$6_Y
  end

  attribute \src "74_extract.v:22"
  cell $dff $procdff$20
    parameter \CLK_POLARITY 1'1
    parameter \WIDTH 16
    connect \CLK \clk
    connect \D $0\counter[15:0]
    connect \Q \counter
  end

  attribute \full_case 1
  attribute \src "74_extract.v:23"
  cell $mux $procmux$14
    parameter \WIDTH 16
    connect \A \preset
    connect \B $add$74_extract.v:26$6_Y
    connect \S \rst
    connect \Y $0\counter[15:0]
  end
end

attribute \cells_not_processed 1
attribute \src "74_extract.v:31"
module \_74xx_counter32

  attribute \src "74_extract.v:37"
  wire width 32 $0\counter[31:0]

  attribute \src "74_extract.v:41"
  wire width 32 $add$74_extract.v:41$9_Y

  attribute \src "74_extract.v:33"
  wire input 2 \clk

  attribute \src "74_extract.v:35"
  wire width 32 output 4 \counter

  attribute \src "74_extract.v:34"
  wire width 33 input 3 \preset

  attribute \src "74_extract.v:32"
  wire input 1 \rst

  attribute \src "74_extract.v:41"
  cell $add $add$74_extract.v:41$9
    parameter \A_SIGNED 0
    parameter \A_WIDTH 32
    parameter \B_SIGNED 0
    parameter \B_WIDTH 1
    parameter \Y_WIDTH 32
    connect \A \counter
    connect \B 1'1
    connect \Y $add$74_extract.v:41$9_Y
  end

  attribute \src "74_extract.v:37"
  cell $dff $procdff$19
    parameter \CLK_POLARITY 1'1
    parameter \WIDTH 32
    connect \CLK \clk
    connect \D $0\counter[31:0]
    connect \Q \counter
  end

  attribute \full_case 1
  attribute \src "74_extract.v:38"
  cell $mux $procmux$11
    parameter \WIDTH 32
    connect \A \preset [31:0]
    connect \B $add$74_extract.v:41$9_Y
    connect \S \rst
    connect \Y $0\counter[31:0]
  end
end

attribute \cells_not_processed 1
attribute \src "74_extract.v:1"
module \_74xx_counter8

  attribute \src "74_extract.v:7"
  wire width 8 $0\counter[7:0]

  attribute \src "74_extract.v:11"
  wire width 8 $add$74_extract.v:11$3_Y

  attribute \src "74_extract.v:3"
  wire input 2 \clk

  attribute \src "74_extract.v:5"
  wire width 8 output 4 \counter

  attribute \src "74_extract.v:4"
  wire width 8 input 3 \preset

  attribute \src "74_extract.v:2"
  wire input 1 \rst

  attribute \src "74_extract.v:11"
  cell $add $add$74_extract.v:11$3
    parameter \A_SIGNED 0
    parameter \A_WIDTH 8
    parameter \B_SIGNED 0
    parameter \B_WIDTH 1
    parameter \Y_WIDTH 8
    connect \A \counter
    connect \B 1'1
    connect \Y $add$74_extract.v:11$3_Y
  end

  attribute \src "74_extract.v:7"
  cell $dff $procdff$21
    parameter \CLK_POLARITY 1'1
    parameter \WIDTH 8
    connect \CLK \clk
    connect \D $0\counter[7:0]
    connect \Q \counter
  end

  attribute \full_case 1
  attribute \src "74_extract.v:8"
  cell $mux $procmux$17
    parameter \WIDTH 8
    connect \A \preset
    connect \B $add$74_extract.v:11$3_Y
    connect \S \rst
    connect \Y $0\counter[7:0]
  end
end
