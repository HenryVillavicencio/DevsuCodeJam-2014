def invertir_cadena(cadena):
    cadena_invertida=''
    longitud_cadena=len(cadena)   
    for index in range(longitud_cadena-1,-1,-1):
        cadena_invertida+=cadena_minuscula[index]
    return cadena_invertida

def dividir_cadena(cadena):
    palabra=''
    vector_palabras=list()
    for caracter in cadena:
        if(caracter == ' '):
            vector_palabras.append(palabra)
            palabra = ''
        else:
            palabra+= caracter
    vector_palabras.append(palabra)
    return vector_palabras

def primera_palabra_cadena_mayuscula(cadena):
    cadena_primera_mayuscula=''
    for palabra in cadena:
        cadena_primera_mayuscula += palabra.capitalize() + ' '
    return cadena_primera_mayuscula

print("Ingrese una cadena")
cadena_entrada=input()
cadena_minuscula=cadena_entrada.lower()
cadena_invertida=invertir_cadena(cadena_minuscula)
vector_palabras=dividir_cadena(cadena_invertida)
cadena_primera_mayuscula = primera_palabra_cadena_mayuscula(vector_palabras)
print(cadena_primera_mayuscula)


