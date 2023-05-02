# 74xx-liberty

Yosys library for synthesizing to [74xx-series logic](https://en.wikipedia.org/wiki/7400-series_integrated_circuits).

# Functions and ICs

## Logic

See [74series.lib](./74series.lib).

> Thanks to [Skot Croshere](https://skot9000.com/)
> for [archiving all the 74xx datasheets](https://skot9000.com/posts/2011/04/28/logic.html) listed here!

- [74AC00](http://web.archive.org/web/20191223205521/http://www.skot9000.com/ttl/datasheets/0.pdf) quad 2-input NAND gate
- [74AC02](http://web.archive.org/web/20191223210813/http://www.skot9000.com/ttl/datasheets/2.pdf) quad 2-input NOR gate
- [74AC04](http://web.archive.org/web/20191223211038/http://www.skot9000.com/ttl/datasheets/4.pdf) hex inverter
- [74AC08](http://web.archive.org/web/20191223205534/http://www.skot9000.com/ttl/datasheets/8.pdf) quad 2-input AND
- [74AC10](http://web.archive.org/web/20191223210630/http://www.skot9000.com/ttl/datasheets/10.pdf) triple 3-input NAND
- [74AC20](http://web.archive.org/web/20191223210648/http://www.skot9000.com/ttl/datasheets/20.pdf) dual 4-input NAND
- [74AC27](http://web.archive.org/web/20191223210816/http://www.skot9000.com/ttl/datasheets/27.pdf) triple 3-input NOR
- [74AC32](http://web.archive.org/web/20191223210939/http://www.skot9000.com/ttl/datasheets/32.pdf) quad 2-input OR gate
- [74AC74](http://web.archive.org/web/20191223210139/http://www.skot9000.com/ttl/datasheets/74.pdf) dual D flip-flop with set and reset
- [74AC86](http://web.archive.org/web/20191223211253/http://www.skot9000.com/ttl/datasheets/86.pdf) quad 2-input XOR gate
- [74AC151](http://web.archive.org/web/20191223205810/http://www.skot9000.com/ttl/datasheets/151.pdf) 8-input (inverting-)multiplexer
- [74AC153](http://web.archive.org/web/20191223210604/http://www.skot9000.com/ttl/datasheets/153.pdf) dual 4-input multiplexer
- [74AC257](http://web.archive.org/web/20191223211218/http://www.skot9000.com/ttl/datasheets/257.pdf) quad 2-input multiplexer
- [74AC273](http://web.archive.org/web/20210507040113/http://www.skot9000.com/ttl/datasheets/273.pdf) octal D flip-flop with clear
- [74AC374](http://web.archive.org/web/20191223210342/http://www.skot9000.com/ttl/datasheets/373.pdf) octal D flip-flop

## Arithmetic

[74_models.v](./74_models.v) expresses:

- [74HC85](http://web.archive.org/web/20191223205930/http://www.skot9000.com/ttl/datasheets/85.pdf) 4-bit magnitude comparator
- [74AC161](http://web.archive.org/web/20191223210209/http://www.skot9000.com/ttl/datasheets/160.pdf) 4-bit synchronous counter
- [74AC283](http://web.archive.org/web/20230122205655/http://www.skot9000.com/ttl/datasheets/283.pdf) 4-bit binary full adder
- [74AC377](http://web.archive.org/web/20191223210749/http://www.skot9000.com/ttl/datasheets/377.pdf) octal D flip-flop with enable
- [74HC688](http://web.archive.org/web/20191223205712/http://www.skot9000.com/ttl/datasheets/682.pdf) 8-bit magnitude comparator

[74_adder.v](./74_adder.v) expresses `$add` and `$sub` celltypes of generic size in terms of the 74HC85.

## BRAM

See [bram.rules](./bram.rules).

- [IDT7132](https://www.alldatasheet.com/datasheet-pdf/pdf/65970/IDT/IDT7132.html) 2K x 8 dual port SRAM
