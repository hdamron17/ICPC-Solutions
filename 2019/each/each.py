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
intermediates = []
for i, x in enumerate(X):
    lastx, lasti = last[-1]
    if lasti == i:
        # This implies x == lastx
        intermediates.sort()
        jn = j + len(intermediates)
        seq[j:jn] = intermediates
        j = jn
        for k in intermediates:
            used[k] = True
        intermediates = []

        if not used[x]:
            seq[j] = x
            j += 1
            used[x] = True
        last.pop()
    elif not used[x] and x < lastx:
        intermediates.append(x)
        used[x] = True

print(" ".join(str(x+1) for x in seq))

## Check
i = 0
for x in X:
    if i < len(seq) and x == seq[i]:
        i += 1
if i != len(seq):
    print("Not valid after index %d of %d: %d" % (i, len(seq), seq[i]))
