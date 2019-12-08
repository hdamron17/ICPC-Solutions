# One of Each problem 2019
# Created by: Hunter Damron
# Points awarded: no
# Status: incomplete
# Notes: Determines last instance of each number in the sequence then iterates
#        through the lasts and adds everything before them in order
#        TODO: issue with current implementation is that if there are duplicates
#        in a segment before a last value (e.g. [1 2 3 1 3 2 1])

n, k = (int(x) for x in input().split())
X = [int(input())-1 for _ in range(n)]

last = [None] * k
for i, x in enumerate(X):
    last[x] = (x, i)
last.sort(key=lambda x: x[1])

seq = [None] * k
j = 0  # Index on seq
used = [False] * k
i = 0  # Index on X
intermediates = []
# print(last[:20])
for lastx, lasti in last:
    if used[lastx]:
        # print("%d already used" % lastx)
        continue
    # print(":", lastx, lasti)
    intermediates = X[i:lasti]
    sintermediates = []
    for x in reversed(intermediates):
        if not used[x] and x < lastx and (not sintermediates or x < sintermediates[-1]):
            sintermediates.append(x)
    # print(sintermediates, lastx)
    k = len(sintermediates) - 1  # Reversed index on intermediates
    for l, x in enumerate(intermediates):
        # print("(1) %d == %d and %d >= 0 and %d == %d" % (x, lastx, k, x, sintermediates[k]))
        if x == lastx and k >= 0 and x == sintermediates[k]:
            # print("breakout %d (%d -> %d)" % (x, lasti, i + l))
            lasti = i + l
            break

        # print("(2) %d < %d and %s and %d >= 0 and %d == %d" % (x, lastx, not used[x], k, x, sintermediates[k]))
        if k >= 0 and x == sintermediates[k]:
            if not used[x]:
                # print("[%d] -> %d" % (j, x))
                seq[j] = x
                j += 1
                used[x] = True
            k -= 1
    if not used[lastx]:
        seq[j] = lastx
        j += 1
        used[lastx] = True
    i = lasti+1

print(" ".join(str(x+1) for x in seq))

## Check
i = 0
for x in X:
    if i < len(seq) and x == seq[i]:
        i += 1
if i != len(seq):
    print("Not valid after index %d of %d: %d" % (i, len(seq), seq[i]))
