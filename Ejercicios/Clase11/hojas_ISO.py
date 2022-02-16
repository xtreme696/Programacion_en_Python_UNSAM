# hojas_ISO.py

def medidas_hoja_A(N):
    def _medidas_hoja_A(N, t = (841,1189)):
        if N > 0:
            N -= 1
            return _medidas_hoja_A(N, (t[1]//2, t[0]))
        return t
    return _medidas_hoja_A(N)