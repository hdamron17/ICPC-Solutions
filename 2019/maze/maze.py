# Maze problem 2019
# Created by: Hunter Damron
# Points awarded: no
# Status: complete
# Notes: Solved after competition by looking at secret test cases.
#        Algorithm created during competition counted inner dots which turned
#        out to be faulty.

from copy import copy

# Gather input
r, c = [int(x) for x in input().split()]
m = [input() for _ in range(r)]

# Remove leading empty lines
rms = []
for i, line in enumerate(m):
  if line.count(".") == c:
    rms.append(i)

for rm in reversed(rms):
  m.pop(rm)
  r -= 1

# If it was all empty, the answer is 0
if not m:
  print(0)
  exit()

# Determine direction of backslashes
firstbslash = True
try:
  firstbslash = m[0].index("/") % 2
except ValueError:
  try:
    firstbslash = (m[0].index("\\") + 1)  % 2
  except ValueError:
    exit(-1)

# Create external boundary by checking if there are dots to the outside
boundary = set()
for row in range(r-1):
  # Handle top and bottom rows
  if row == 0 or row == r-2:
    for col in range(firstbslash ^ (row % 2), c-1, 2):
      if row == 0:
        if "." in m[row][col:col+2]:
          boundary.add((row,col))
      if row == r-2:
        if "." in m[row+1][col:col+2]:
          boundary.add((row,col))

  # Handle left and right columns (indices are skewed)
  left = firstbslash ^ (row % 2)
  right = left + (c-1) // 2 * 2
  while right >= c-1:
    right -= 2

  if left == 0:
    if "." in (m[row][left], m[row+1][left]):
      boundary.add((row,left))
  if right == c-2:
    if "." in (m[row][right+1], m[row+1][right+1]):
      boundary.add((row,right))

# Create first and second rows then repeat the alternation for base explored map
r1 = [firstbslash, int(not firstbslash)] * ((c-1) // 2)
if not c % 2:
   r1.append(firstbslash)
r2 = list(map(lambda b: int(not b), r1))
explored = [copy(r1 if not i % 2 else r2) for i in range(r-1)]

# Function to get all valid neighbors of a position
def neighbors(row,col):
  ret = []
  if m[row][col] == '.' and row-1 >= 0 and col-1 >= 0:
    ret.append((row-1,col-1))
  if m[row][col+1] == '.' and row-1 >= 0 and col+1 < c-1:
    ret.append((row-1,col+1))
  if m[row+1][col] == '.' and row+1 < r-1 and col-1 >= 0:
    ret.append((row+1,col-1))
  if m[row+1][col+1] == '.' and row+1 < r-1 and col+1 < c-1:
    ret.append((row+1,col+1))
  return ret

# Function to run flood fill algorithm on current boundary
def explore():
  while boundary:
    bx, by = boundary.pop()
    # print(">", bx, by)
    if explored[bx][by]:
      continue
    explored[bx][by] = 1
    boundary.update(neighbors(bx,by))

# Explore the external boundary (no wall breaking to reach)
explore()

# Count the number of internal cells by repeatedly running exploration
count = 0
for row in range(len(explored)):
  for col in range(len(r1)):
    if explored[row][col]:
      continue
    boundary.add((row,col))
    explore()
    count += 1

# Output number of internal cells - must break one wall for each
print(count)
