import numpy as np
uno = np.array([
    [' ',' ','#'],
    [' ',' ','#'],
    [' ',' ','#'],
    [' ',' ','#'],
    [' ',' ','#'],
])
dos = np.array([
    ['#','#','#'],
    [' ',' ','#'],
    ['#','#','#'],
    ['#',' ',' '],
    ['#','#','#'],
])
diccionario = { 1: uno,2:dos}
print("Ingrese un numero")
numero = '12'
primer_digito = int(numero[0])
segundo_digito = int(numero[1])
print(np.concatenate((diccionario[primer_digito],diccionario[segundo_digito]),axis=1))
