#!/usr/bin/env python3

import sys
import re

with open(sys.argv[1], 'r') as f:
    lines = f.readlines()

strings = "".join(lines)

def mul(x,y):
    return x * y

pattern = r"mul\(\s*(\d{1,3})\s*,\s*(\d{1,3})\s*\)|do\(\)|don\'t\(\)"
pattern_do = r"do\(\)"
pattern_dont = r"don\'t\(\)"
matches = re.findall(pattern, strings)
print(strings)

total_sum = sum(mul(int(x), int(y)) for x, y in matches)

part1 = total_sum
print(f'Part 1: {part1}')

part2 = ""
print(f'Part 2: {part2}')