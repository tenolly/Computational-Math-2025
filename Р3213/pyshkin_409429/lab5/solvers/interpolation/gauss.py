import sympy as sp

def gauss_interpolation(x_vals, diffs, x):
    n = len(x_vals)
    h = x_vals[1] - x_vals[0]
    m = n // 2
    t = (x - x_vals[m]) / h

    result = diffs[0][m]

    for k in range(1, n):
        P = 1
        offset = k // 2
        for j in range(k):
            P *= (t - offset + j)

        i = m - offset
        if i < 0 or i >= len(diffs[k]):
            break

        result += P * diffs[k][i] / sp.factorial(k)

    return result