from typing import Callable, Any, List
import sympy as sp


class QuadraticApproximation:
    def __init__(self, table: bool = False):
        self.table = table
    
    def solve(self, *args, **kwargs) -> Any:
        if self.table:
            return self._table_solve(*args, **kwargs)
        
        return self._func_solve(*args, **kwargs)
    
    def _func_solve(self, f: Callable, left: float, right: float, n: int, lambdify: bool = True) -> Any:
        sx = sx2 = sx3 = sx4 = sy = sxy = sx2y = 0
    
        h = (right - left) / n
        for i in range(n + 1):
            x = left + h * i
            y = f(x)
            sx += x
            sx2 += x**2
            sx3 += x**3
            sx4 += x**4
            sy += y
            sxy += x*y
            sx2y += x**2*y
        
        a0, a1, a2 = sp.symbols("a0 a1 a2")
        root = sp.solve(
            [
                n * a0 + sx * a1 + sx2 * a2 - sy, 
                sx * a0 + sx2 * a1 + sx3 * a2 - sxy,
                sx2 * a0 + sx3 * a1 + sx4 * a2 - sx2y
            ], 
            [a0, a1, a2], 
            dict=True
        )[0]
        
        x = sp.Symbol("x")
        function = root[a0] + root[a1] * x + root[a2] * x ** 2
        
        if lambdify:
            return sp.lambdify(x, function)
        
        return x, function
    
    def _table_solve(self, table: List[List[float]], lambdify: bool = True) -> Any:
        sx = sx2 = sx3 = sx4 = sy = sxy = sx2y = 0
        
        n = len(table[0])
        for x, y in zip(table[0], table[1]):
            sx += x
            sx2 += x**2
            sx3 += x**3
            sx4 += x**4
            sy += y
            sxy += x*y
            sx2y += x**2*y
        
        a0, a1, a2 = sp.symbols("a0 a1 a2")
        root = sp.solve(
            [
                n * a0 + sx * a1 + sx2 * a2 - sy, 
                sx * a0 + sx2 * a1 + sx3 * a2 - sxy,
                sx2 * a0 + sx3 * a1 + sx4 * a2 - sx2y
            ], 
            [a0, a1, a2], 
            dict=True
        )[0]
        
        x = sp.Symbol("x")
        function = root[a0] + root[a1] * x + root[a2] * x ** 2
        
        if lambdify:
            return sp.lambdify(x, function)
        
        return x, function
