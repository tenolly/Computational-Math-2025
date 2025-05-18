from .accuracy import runge_rule


def euler_method(f, x0, y0, xn, h, use_runge=True, eps=0.01):
    x_vals = [x0]
    y_vals = [y0]
    
    while x_vals[-1] < xn:
        xi = x_vals[-1] + h
        xi_h2 = x_vals[-1] + h / 2
        
        yi = y_vals[-1] + h * f(xi, y_vals[-1])
        yi_h2 = y_vals[-1] + h / 2 * f(xi_h2, y_vals[-1])
        
        if not use_runge or runge_rule(yi, yi_h2, 1, eps):
            x_vals.append(xi)
            y_vals.append(yi)
        else:
            h = h / 2
            
        if h < 1e-8:
            raise ValueError("Невозможно вычислить значение с такой точностью")
    
    return x_vals, y_vals
