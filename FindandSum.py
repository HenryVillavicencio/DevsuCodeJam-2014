print("Ingrese una cadena")
cadena_entrada=input()
total = 0
numero = ''
for caracter in cadena_entrada:
    if (caracter.isdigit()):
        numero += caracter
    elif (numero != ''):
        total += int(numero)
        numero = ''
if (numero != ''):
    total += int(numero)
print(total)
        
        
