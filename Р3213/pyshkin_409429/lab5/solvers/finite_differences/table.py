def create_table(x, y):
    n = len(x)
    
    if len(y) != n:
        raise ValueError("Длины x и y должны совпадать.")
    
    if n < 2:
        raise ValueError("Нужно как минимум две точки.")
    
    diffs = [y.copy()]
    for k in range(1, n):
        current_diff = []
        prev_diff = diffs[k-1]
        
        for i in range(n - k):
            current_diff.append(prev_diff[i+1] - prev_diff[i])
            
        diffs.append(current_diff)
        
    return diffs


def print_finite_differences_table(x, diffs):
    n = len(x)
    max_order = len(diffs) - 1
    
    header = ["x".ljust(10), "y".ljust(10)]
    for k in range(1, max_order + 1):
        header.append(f"Δ^{k}y".ljust(10) if k > 1 else "Δy".ljust(10))
        
    print("\nТаблица конечных разностей:")
    print("  ".join(header))
    
    for i in range(n):
        row = [f"{x[i]:<10.4f}", f"{diffs[0][i]:<10.4f}"]
        
        for k in range(1, max_order + 1):
            row.append(f"{diffs[k][i]:<10.4f}" if k <= n-1-i and i < len(diffs[k]) else " " * 10)
            
        print("  ".join(row))
