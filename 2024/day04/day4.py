import sys
from collections import defaultdict

with open(sys.argv[1], "r") as f:
    lines = list(map(str.strip, f.readlines()))

char_map = defaultdict(set)
for r, row in enumerate(lines):
    for c, val in enumerate(row):
        char_map[val].add((r, c))

part1 = 0
for r, c in char_map["X"]:
    for dr, dc in [
        (-1, -1),
        (-1, 0),
        (-1, 1),
        (0, -1),
        (0, 1),
        (1, -1),
        (1, 0),
        (1, 1),
    ]:
        for i, char in enumerate("MAS", 1):
            if (r + (dr * i), c + (dc * i)) not in char_map[char]:
                break
        else:
            part1 += 1

print(f'Part 1: {part1}')

upleft = lambda r, c: (r - 1, c - 1)
upright = lambda r, c: (r - 1, c + 1)
downleft = lambda r, c: (r + 1, c - 1)
downright = lambda r, c: (r + 1, c + 1)
get = lambda r, c: lines[r][c]

part2 = 0
for r, c in char_map["A"]:
    # Cleaner Solution (Thanks HyperNeutrino)
    if r == 0 or c == 0 or r == len(lines) - 1 or c == len(lines[0]) - 1:
        continue
    corners = get(*upleft(r, c)) + get(*upright(r, c)) + get(*downright(r, c)) + get(*downleft(r, c))
    if corners in ["MMSS", "MSSM", "SSMM", "SMMS"]:
        part2 += 1

print(f'Part 2: {part2}')

# import sys
#
# with open(sys.argv[1], 'r') as f:
#     lines = [line.strip() for line in f.readlines()]
#     matrix = [list(line) for line in lines]
#
# word = ["X", "M", "A", "S"]
#
# directions = [
#     (-1, 0),  # top
#     (1, 0),   # down
#     (0, -1),  # left
#     (0, 1),   # right
#     (-1, -1), # top left
#     (-1, 1),  # top right
#     (1, -1),  # down left
#     (1, 1),   # down right
# ]
#
# def count_word_occurrences(matrix, word):
#     rows = len(matrix)
#     cols = len(matrix[0])
#     count = 0
#     occurrences = []
#
#     for y in range(rows):
#         for x in range(cols):
#             # Chek if word starts in a direction
#             for dy, dx in directions:
#                 # Check forward
#                 if check_direction(matrix, word, y, x, dy, dx):
#                     count += 1
#                     occurrences.append(((y, x), (dy, dx)))
#                 # Check backward
#                 if check_direction(matrix, word[::-1], y, x, dy, dx):
#                     count += 1
#                     occurrences.append(((y, x), (-dy, -dx)))
#     return count, occurrences
#
# def check_direction(matrix, word, start_y, start_x, dy, dx):
#     rows = len(matrix)
#     cols = len(matrix[0])
#     for k in range(len(word)):
#         ny, nx = start_y + k * dy, start_x + k * dx
#         if not (0 <= ny < rows and 0 <= nx < cols):
#             return False
#         if matrix[ny][nx] != word[k]:
#             return False
#     return True
#
# count, occurrences = count_word_occurrences(matrix, word)
#
# part1 = count
# print(f'Part 1: {part1}')
#
# part2 = ""
# print(f'Part 2: {part2}')