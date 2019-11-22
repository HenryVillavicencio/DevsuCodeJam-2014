from math import sqrt

def esEntero(numero):
    if(numero%1 == 0):
        return True
    else:
        return False

print('ingrese x')
x = int(input())
print('ingrese y')
y = int(input())
r = sqrt(x**2+y**2)

if(esEntero(r)):
    print('Black')
else:
    r_entero = r - r%1
    cuadrante = x*y
    if(cuadrante > 0):
        if(r_entero%2 == 0 ):
            print('Black')
        else:
            print('White')
    else:
        if(r_entero%2 == 0 ):
            print('White')
        else:
            print('Black')
        

