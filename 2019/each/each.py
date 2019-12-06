# One of Each problem 2019
# Created by: Hunter Damron
# Points awarded: no
# Status: incomplete
# Notes: Determines last instance of each number in the sequence then iterates
#        through the list, adding point when they are either last or the next in
#        the sequence
#        TODO: we must find all elements before the next last and apply all
#        of them

n, k = (int(x) for x in input().split())
X = [int(input())-1 for _ in range(n)]

last = [None] * k
for i, x in enumerate(X):
    last[x] = (x, i)
last.sort(key=lambda x: x[1], reverse=True)

seq = [None] * k
j = 0
used = [False] * k
next = 0
for i, x in enumerate(X):
    lastx, lasti = last[-1]
    if lasti == i:
        # This implies x == lastx
        if not used[x]:
            seq[j] = x
            j += 1
            used[x] = True
        last.pop()
    elif x == next:
        seq[j] = x
        j += 1
        used[x] = True
    while next < k and used[next]:
        next += 1

print(" ".join(str(x+1) for x in seq))
