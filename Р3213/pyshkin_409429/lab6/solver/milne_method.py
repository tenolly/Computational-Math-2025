def milne_method(f, x0, y0, xn, h, eps):
    x = x0
    y = y0
    x_values = [x]
    y_values = [y]
    
    for _ in range(3):
        k1 = h * f(x, y)
        k2 = h * f(x + h / 2, y + k1 / 2)
        k3 = h * f(x + h / 2, y + k2 / 2)
        k4 = h * f(x + h, y + k3)
        y += (k1 + 2 * k2 + 2 * k3 + k4) / 6
        x += h
        x_values.append(x)
        y_values.append(y)
    
    while x < xn:
        i = len(y_values) - 1
        
        f_im3 = f(x_values[i - 3], y_values[i - 3])
        f_im2 = f(x_values[i - 2], y_values[i - 2])
        f_im1 = f(x_values[i - 1], y_values[i - 1])
        
        y_prog = y_values[i - 4] + (4 * h / 3) * (2 * f_im3 - f_im2 + 2 * f_im1)
        x_prog = x + h
        
        y_corr_prev = y_prog
        for _ in range(100):
            f_prog = f(x_prog, y_corr_prev)
            y_corr = y_values[i - 2] + (h / 3) * (f_im2 + 4 * f_im1 + f_prog)
            
            if abs(y_corr - y_corr_prev) <= eps:
                break
            
            y_corr_prev = y_corr
        
        x = x_prog
        y = y_corr
        x_values.append(x)
        y_values.append(y)
    
    return x_values, y_values
