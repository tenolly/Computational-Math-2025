def lagrange_interpolation(x_vals, y_vals, x):
    n = len(x_vals)
    
    result = 0
    for i in range(n):
        term = y_vals[i]
        
        for j in range(n):
            if j != i:
                term *= (x - x_vals[j]) / (x_vals[i] - x_vals[j])
                
        result += term
        
    return result
