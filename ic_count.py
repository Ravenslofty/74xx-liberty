#!/usr/bin/env python3
import fileinput
import math
import re

IC_LIST = dict()

for line in fileinput.input():
    match = re.search(r"^\s*\\(\d+)_(\d+)x(\d+)\S+\s*(\d+)", line)

    if not match:
        continue

    part_number, gates_per_ic, gates_per_combo, combo_count = match.groups()

    if part_number not in IC_LIST:
        IC_LIST[part_number] = (
                (int(combo_count) * int(gates_per_combo))
                / int(gates_per_ic))
    else:
        IC_LIST[part_number] += (
                (int(combo_count) * int(gates_per_combo))
                / int(gates_per_ic))

TOTAL_ICs = 0

for part, count in IC_LIST.items():
    count = math.ceil(count)
    TOTAL_ICs += count
    print("{}: {}".format(part, count))

print()
print("Total: {}".format(TOTAL_ICs))
