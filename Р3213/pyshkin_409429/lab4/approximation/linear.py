from typing import Callable, Any, List
import sympy as sp


class LinearApproximation:
    def __init__(self, table: bool = False):
        self.table = table
    
    def solve(self, *args, **kwargs) -> Any:
        if self.table:
            return self._table_solve(*args, **kwargs)
        
        return self._func_solve(*args, **kwargs)
    
    def _func_solve(self, f: Callable, left: float, right: float, n: int, lambdify: bool = True) -> Any:
        sx = sxx = sy = sxy = 0
    
        h = (right - left) / n
        for i in range(n + 1):
            x = left + h * i
            y = f(x)
            sx += x
            sxx += x**2
            sy += y
            sxy += x*y
        
        a, b = sp.symbols("a b")
        root = sp.solve([a * sxx + b * sx - sxy, a * sx + b * n - sy], [a, b], dict=True)[0]
        
        x = sp.Symbol("x")
        function = root[a] * x + root[b]
        
        if lambdify:
            return sp.lambdify(x, function)
        
        return x, function
    
    def _table_solve(self, table: List[List[float]], lambdify: bool = True) -> Any:
        sx = sxx = sy = sxy = 0
        
        n = len(table[0])
        for x, y in zip(table[0], table[1]):
            sx += x
            sxx += x**2
            sy += y
            sxy += x*y
        
        a, b = sp.symbols("a b")
        root = sp.solve([a * sxx + b * sx - sxy, a * sx + b * n - sy], [a, b], dict=True)[0]
        
        x = sp.Symbol("x")
        function = root[a] * x + root[b]
        
        if lambdify:
            return sp.lambdify(x, function)
        
        return x, function
