def runge_rule(y_h, y_h2, p, eps):
    error_estimate = abs(y_h - y_h2) / (2**p - 1)
    return error_estimate <= eps
