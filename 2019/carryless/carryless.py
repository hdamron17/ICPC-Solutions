# Carryless Square Root problem 2019
# Created by: Hunter Damron
# Points awarded: no
# Status: incomplete
# Notes: Transforms the problem into the square root of a polynomial modulo 10
#        Worst case explores each of 2 options at 13 branches -> 2^13 = 8192

DBG = False
dbg = lambda *s, **k: print(*s, **k) if DBG else None

s = [ord(d) - ord('0') for d in input()]

digit_sqrt_dict = {
    0: [0],
    1: [1,9],
    4: [2,8],
    9: [3,7],
    6: [4,6],
    5: [5]
}

digit_sqrt = lambda n: digit_sqrt_dict.get(n, [])

def carryless_sqrt(xs):
    if len(xs) % 2 == 0:
        return None
    for d0 in digit_sqrt(xs[0]):
        dbg("Trying d0 =", d0)
        dlen = (len(xs) - 1) // 2
        sol = carryless_sqrt_(1, [d0] + [None] * dlen, xs)
        if sol is not None:
            return sol
    return None

def carryless_sqrt_(n, ds, xs):
    if n >= len(xs):
        return ds
    dbg("--", n, ds, xs)
    if n < len(ds):
        ds_i = len(ds) - n - 1
        # solves equivalence for d_n: 2 d_0 d_n = x_n - \sum_{i=1}^{n-1} d_i d_{n-i}
        lhs_factor = 2 * ds[0] % 10
        rhs = xs[n]
        dbg(str(lhs_factor) + " d_" + str(n) + " = " + str(rhs), end='')
        for i in range(1,n):
            dbg(" - " + str(ds[i]) + "*" + str(ds[n-i]), end='')
            rhs -= ds[i] * ds[n-i]
            rhs %= 10
        dbg(" = " + str(rhs))
        d_ns = even_digit_equiv(lhs_factor, rhs)
        dbg("-> d_" + str(n) + " in " + str(d_ns))
        for d_n in d_ns:
            ds[n] = d_n
            ret = carryless_sqrt_(n+1, ds, xs)
            if ret is not None:
                return ret
        return None

    else:
        # checks the equivalence d_n: x_n - \sum_{i+j=n} d_i d_j = 0
        check = xs[n]
        dbg(str(check), end='')
        start_i = n - len(ds) + 1
        for i in range(start_i,n-start_i+1):
            dbg(" - " + str(ds[i]) + "*" + str(ds[n-i]) + " [%d,%d]" % (i,n-i), end='')
            check -= ds[i] * ds[n-i]
            check %= 10
        dbg(" = " + str(check))
        return carryless_sqrt_(n+1, ds, xs) if check == 0 else None

def even_digit_equiv(lhs_factor, rhs):
    # Solves the equivalence for d: lhs_factor * d = rhs
    # Assumes lhs_factor != 0 and lhs_factor is even
    if rhs == 0:
        return [0]

    if rhs % 2 == 1:
        return []

    factor = lhs_factor
    for i in range(1,5):
        if factor == rhs:
            return [i,i+5]
        factor = factor + lhs_factor % 10
    return []  # Should be unnecessary

sol = carryless_sqrt(s)
if sol:
    print("".join(str(x) for x in sol))
else:
    print(-1)
