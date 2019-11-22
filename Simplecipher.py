# def esMayuscula(letra):
#     if letra >='A' and letra <= 'Z':
#         return True
#     else:
#         return False
# def esMinuscula(letra):
#     if letra >='a' and letra <= 'z':
#         return True
#     else:
#         return False

# impar --> siguiente
# par --> anterior

print("Ingrese una cadena")
# cadena_entrada=input()
cadena_entrada='The quick brown fox jumps over the lazy dog 12345 :) * zzzZZZAAAaaa'
esImpar = True
for caracter in cadena_entrada:
    if(caracter.isalpha()):
        if(esImpar):
            if(caracter =='Z'):
                print('A',end='')
            elif (caracter =='z'):
                print('a',end='')
            else:
                print(chr(ord(caracter)+1),end='')
        else:
            if(caracter =='A'):
                print('Z',end='')
            elif(caracter =='a'):
                print('z',end='')
            else:
                print(chr(ord(caracter)-1),end='')
    else:
        print(caracter,end='')
    esImpar = not esImpar
print('')        




