def newton_interpolation(x_vals, diffs, x):
    n = len(x_vals)
    
    h = x_vals[1] - x_vals[0]
    t = (x - x_vals[0]) / h
    result = diffs[0][0]
    product = 1
    
    for i in range(1, n):
        product *= (t - (i - 1)) / i
        result += product * diffs[i][0]
        
    return result
