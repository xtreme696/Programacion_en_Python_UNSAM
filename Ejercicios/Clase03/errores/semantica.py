def tiene_a(expresion):
    n = len(expresion)
    i = 0
    tiene = False
    while i<n:
        if expresion[i] == 'a' or expresion[i] == 'A':
            tiene = True
        i += 1

    return tiene

print(tiene_a('UNSAM 2020'))
print(tiene_a('abracadabra'))
print(tiene_a('La novela 1984 de George Orwell'))
