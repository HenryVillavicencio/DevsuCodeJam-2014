print("Ingrese una cadena")
cadena_entrada=input()
contador=1
caracter_anterior=''
for caracter in cadena_entrada:
    if(caracter_anterior==caracter):
        contador = contador + 1
    else:
        print(caracter_anterior,end='')
        if(contador != 1):
            print(contador, end='')
        contador = 1
    caracter_anterior=caracter
print(caracter_anterior, end='')
if(contador != 1):
    print(contador, end='')