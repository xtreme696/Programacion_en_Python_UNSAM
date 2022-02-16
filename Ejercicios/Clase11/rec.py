# rec.py

def triangular(n):
    suma = 0
    
    def _triangular(n, s):
        if n > 0:
            return _triangular(n-1, s+n)
        return s
    
    return _triangular(n, suma)
