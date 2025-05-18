from .accuracy import runge_rule


def fourth_order_runge_kutta_method(f, x0, y0, xn, h, use_runge=True, eps=0.01):
    def calc_iter(x_last, y_last, h):
        xi = x_last + h

        k1 = h * f(xi,y_last)
        k2 = h * f(xi + h / 2, y_last + k1 / 2)
        k3 = h * f(xi + h / 2, y_last + k2 / 2)
        k4 = h * f(xi + h, y_last + k3)
        
        yi = y_last + 1 / 6 * (k1 + 2 * k2 + 2 * k3 + k4)
        
        return xi, yi
        
    x_vals = [x0]
    y_vals = [y0]
    
    while x_vals[-1] < xn:
        xi, yi = calc_iter(x_vals[-1], y_vals[-1], h)
        _, yi_h2 = calc_iter(x_vals[-1], y_vals[-1], h / 2)
        
        if not use_runge or runge_rule(yi, yi_h2, 4, eps):
            x_vals.append(xi)
            y_vals.append(yi)
        else:
            h = h / 2
        
        if h < 1e-8:
            raise ValueError("Невозможно вычислить значение с такой точностью")
        
    return x_vals, y_vals
