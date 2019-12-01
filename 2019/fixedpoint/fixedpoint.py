# Fixed Point Permutation problem 2019
# Created by: Hunter Damron
# Points awarded: no
# Status: incomplete
# Notes: Uses dynamic programming approach to count number of permutations for
#        each choice of fixed points then chooses appropriate fixed points and
#        finds permutation of remaining points.
#        Worst case for counting problem is O(n^3) and worst case for solving
#        final answer is O(n^2)

from itertools import permutations, combinations

n, m, k = (int(x) for x in input().split())
k -= 1  # We are indexing from 0
k_max = 10**18+1

def all_m_fixedpoint(n,m=0,k=0):
    l = []
    for p in permutations(["_"] * k + list(range(1+k,n+1))):
        if sum(int(i+1 == j) for i, j in enumerate(p)) == m:
            l.append(p)
    return l

def bf_count_fixedpoint(n,m=0,k=0):
    return len(all_m_fixedpoint(n,m,k))

fixedpoint_table = [[[None] * (n+1) for _ in range(n+1)] for _ in range(n+1)]
def dp_count_fixedpoint(n, m, k=0, prefix=""):
    cached_result = fixedpoint_table[n][m][k]
    if cached_result is not None:
        return cached_result

    if n == 0 and m == 0 and k == 0:
        ret = 1  # One way to do this vacuously
    elif n == 1:
        if m == 1 and k == 0 or m == 0 and k >= 1:
            ret = 1
        else:
            ret = 0  # Impossible
    elif m > n - k:
        # Cannot fill m fixed points from n-k possible
        ret = 0
    elif k > 0:
        ret = k * dp_count_fixedpoint(n-1, m, k-1, "."+prefix)
        if k <= n:
            ret += (n-k) * dp_count_fixedpoint(n-1, m, k, "."+prefix)
    elif m > 0:
        ret = dp_count_fixedpoint(n-1, m-1, k, "."+prefix)
        ret += (n-1) * dp_count_fixedpoint(n-1, m, k+1, "."+prefix)
    else:
        # case k=m=0, n>0
        ret = (n-1) * dp_count_fixedpoint(n-1, m, k+1, "."+prefix)
    if ret > k_max:
        ret = k_max  # Not super necessary but avoids annoyingly large numbers
    fixedpoint_table[n][m][k] = ret
    return ret

answer = [None] * n
remainder = list(range(1,n+1))
for i in range(1,n+1):
    free_points = len(list(filter(lambda x: x < i, remainder)))
    sub_n = len(remainder) - 1
    for d in remainder:
        if d < i:
            subcount = dp_count_fixedpoint(sub_n, m, free_points-1)
            if k < subcount:
                answer[i-1] = d
                remainder.remove(d)
                break
            else:
                k -= subcount
        elif d == i:
            subcount = dp_count_fixedpoint(sub_n, m-1, free_points)
            if k < subcount:
                answer[i-1] = d
                remainder.remove(d)
                m -= 1
                break
            else:
                k -= subcount
        else:
            subcount = dp_count_fixedpoint(sub_n, m, free_points+1)
            if k < subcount:
                answer[i-1] = d
                remainder.remove(d)
                break
            else:
                k -= subcount
    if answer[i-1] is None:
        print(-1)
        exit()
print(" ".join(str(x) for x in answer))
