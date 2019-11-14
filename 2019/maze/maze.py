# Maze problem 2019
# Created by: Hunter Damron
# Points awarded: no
# Status: incomplete
# Notes: Works for sample inputs but not all secret inputs
#        Method of counting inner dots fails for shapes with holes
#        Alternative will be to do flood fill repeatedly instead of counting dots

from copy import copy

r, c = [int(x) for x in input().split()]
m = [input() for _ in range(r)]

rms = []
for i, line in enumerate(m):
  if line.count(".") == c:
    rms.append(i)

for rm in reversed(rms):
  m.pop(rm)
  r -= 1

if not m:
  print(0)
  exit()

# print("%d %d\n%s" % (r,c,"\n".join(m)))

firstbslash = True
try:
  firstbslash = m[0].index("/") % 2
except ValueError:
  try:
    firstbslash = (m[0].index("\\") + 1)  % 2
  except ValueError:
    exit(-1)

#print(firstbslash)

boundary = set()

for row in range(r-1):
  if row == 0 or row == r-2:
    for col in range(firstbslash ^ (row % 2), c-1, 2):
      #print(row,col)
      if row == 0:
        #print("%c%c" % (m[row][col], m[row][col+1]))
        if "." in m[row][col:col+2]:
          boundary.add((row,col))
      if row == r-2:
        #print("%c%c" % (m[row+1][col], m[row+1][col+1]))
        if "." in m[row+1][col:col+2]:
          boundary.add((row,col))

  left = firstbslash ^ (row % 2)
  right = left + (c-1) // 2 * 2
  while right >= c-1:
    right -= 2

  if left == 0:
    #print("%d %d:\n%c\n%c" % (row,left,m[row][left],m[row+1][left]))
    if "." in (m[row][left], m[row+1][left]):
      boundary.add((row,left))
  if right == c-2:
    #print("%d %d:\n%c\n%c" % (row,right,m[row][right+1],m[row+1][right+1]))
    if "." in (m[row][right+1], m[row+1][right+1]):
      boundary.add((row,right))
  #print(row, ":",left,right)

r1 = [firstbslash, int(not firstbslash)] * ((c-1) // 2)
if not c % 2:
   r1.append(firstbslash)
r2 = list(map(lambda b: int(not b), r1))

explored = [copy(r1 if not i % 2 else r2) for i in range(r-1)]
# print("\n".join("".join(str(c) for c in x) for x in explored))

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

#print(boundary)

#print(m[0][2], neighbors(2,0))
# print("===\n%s\n%s\n%s\n===" % (m[0][1:4], m[1][1:4], m[2][1:4]))

def explore():
  while boundary:
    bx, by = boundary.pop()
    # print(">", bx, by)
    if explored[bx][by]:
      continue
    explored[bx][by] = 1
    boundary.update(neighbors(bx,by))

explore()

# print("---")
# print("\n".join("".join(str(c) for c in x) for x in explored))
# print("---")

enclosed_area = sum(line.count(0) for line in explored)
#print(enclosed_area)

# inner_dots = 0
count = 0
# for row in range(len(explored)-1):
for row in range(len(explored)):
  for col in range(len(r1)):
    if explored[row][col]:
      continue
    # print("++", row, col)
    boundary.add((row,col))
    explore()
    count += 1

    # print("---")
    # print("\n".join("".join(str(c) for c in x) for x in explored))
    # print("---")

    # if col > 0 and not explored[row+1][col-1] and m[row+1][col] == ".":
    #   #print("< %d,%d -> %d,%d" % (row,col,row+1,col-1))
    #   inner_dots += 1
    # if col < len(r1)-1 and not explored[row+1][col+1] and m[row+1][col+1] == ".":
    #   #print("> %d,%d -> %d,%d" % (row,col,row+1,col+1))
    #   inner_dots += 1

#print(inner_dots)

# print(enclosed_area - inner_dots)
print(count)
