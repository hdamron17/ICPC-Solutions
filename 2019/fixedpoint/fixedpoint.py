# Fixed Point Permutation problem 2019
# Created by: Hunter Damron
# Points awarded: no
# Status: incomplete
# Notes: Uses dynamic programming approach to count number of permutations for
#        each choice of fixed points then chooses appropriate fixed points and
#        finds permutation of remaining points.
#
#        Algorithm made false assumption that fixed points are ordered
#        independently from subpermutations but this fails for
#        x=12435 and y=12543 because the y comes first in the way of fixed
#        points but x comes first overall

from itertools import permutations, combinations

DBG = False
dbg = lambda *s, **k: print(*s, **k) if DBG else None

n, m, k = (int(x) for x in input().split())
k_max = 10**18+1

def all_m_fixedpoint(n,m=0):
    l = []
    for p in permutations(range(1,n+1)):
        if sum(int(i+1 == j) for i, j in enumerate(p)) == m:
            l.append(p)
    return l

def bf_no_fixedpoint(n):
    return len(all_m_fixedpoint(n))

# print(": " + " ".join(str(x) for x in (all_m_fixedpoint(n,m)[k-1:]+[[-1]])[0]))

no_fixedpoint_table = [[None] * (n+1) for _ in range(n+1)]
def dp_count_no_fixedpoint(n, k=0):
    cached_result = no_fixedpoint_table[n][k]
    if cached_result is not None:
        return cached_result

    if n == 0:
        ret = 1
    elif n == k:
        ret = n * dp_count_no_fixedpoint(n-1, k-1)
    else:
        ret = 0
        if k > 0:
            ret += k * dp_count_no_fixedpoint(n-1, k)
        if n > k+1:
            ret += (n-k-1) * dp_count_no_fixedpoint(n-1, k+1)
    if ret > k_max:
        ret = k_max  # Not super necessary but avoids annoyingly large numbers
    no_fixedpoint_table[n][k] = ret
    return ret

factorial = [None] * (n+1)
factorial[0] = 1
for i in range(1,n+1):
    if factorial[i-1] >= k_max:
        factorial[i] = k_max
    factorial[i] = min(k_max, i * factorial[i-1])

def kth_permutation_n(k, n):
    return kth_permutation(k, list(range(1,n+1)))
def kth_permutation(k, xs):
    # Kth permutation of 1,...,n
    if len(xs) == 0:
        return []
    i = k // factorial[len(xs)-1]
    r = k % factorial[len(xs)-1]
    if i >= len(xs):
        return None
    # print(xs,"%d = %d * %d + %d" % (k, i, factorial[len(xs)-1], r))
    rec_ret = kth_permutation(r, xs[:i] + xs[i+1:])
    if rec_ret is None:
        return None
    else:
        return [xs[i]] + rec_ret

if k > factorial[n]:
    print(-1)
    exit()

per_permutation = dp_count_no_fixedpoint(n-m)
if per_permutation <= 0:
    print(-1)
    exit()
print("per_permutation =", per_permutation)
print("bf_no_fixedpoint =", bf_no_fixedpoint(n-m))

permutation_i = k % per_permutation
fixed_point_i = k // per_permutation

kth_subset_table = [[None] * (fixed_point_i+1) for _ in range(n-m+1)]
def choose(n,k):
    return factorial[n] // factorial[k] // factorial[n-k]
def kth_m_combo(k,xs,m):
    if m == 0:
        return []
    sub_count = choose(len(xs)-1,m-1)
    if k < sub_count:
        rec_ret = kth_m_combo(k, xs[1:], m-1)
        if rec_ret is None:
            return None
        return [xs[0]] + rec_ret
    else:
        return kth_m_combo(k-sub_count, xs[1:], m)

print("==",kth_m_combo(7,list(range(1,5+1)),3))

print("----")
print("\n".join(str(x) for x in combinations(list(range(1,n+1)),m)))

# fixed_points = kth_permutation_n(fixed_point_i,n-m)
# print(fixed_points)

print("----")
print("\n".join(str(x) for x in all_m_fixedpoint(n,m)))
