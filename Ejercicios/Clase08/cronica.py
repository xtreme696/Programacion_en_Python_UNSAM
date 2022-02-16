# cronica.py

from datetime import date

def dias_para_primavera():
    primavera = date(year = 2022, month = 9, day = 21)
    faltan = primavera - date.today()
    
    return faltan.days


if __name__ == '__main__':
    print(f'FALTAN {dias_para_primavera()} DIAS PARA LA PRIMAVERA')