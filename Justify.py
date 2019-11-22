longitud = 50
parrafo = 'Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.'
parrafo_separado = parrafo.split(' ')

lineas = []
linea = []
contador_longitud = 0

for palabra in parrafo_separado:
    if(contador_longitud+len(palabra)+1 < longitud+2):
        linea.append(palabra)
        contador_longitud += len(palabra)+1
    else:
        lineas.append(linea)
        linea = [palabra]
        contador_longitud = len(palabra)+1 
lineas.append(linea)

for linea in lineas:
    num_palabras = len(linea)
    longitud_linea = len(''.join(linea))
    espacios = longitud - longitud_linea
    if(num_palabras > 1):
        espacios_por_palabra = espacios//(num_palabras-1)
        relleno = espacios - espacios_por_palabra*(num_palabras-1)
        for palabra in linea:
            print(palabra,end='')
            if(espacios > 0):
                print(' '*espacios_por_palabra, end='')
                espacios -= espacios_por_palabra
            if(relleno > 0 ):
                print(' ',end='')
                relleno -= 1
                espacios -= 1
        print('')
    else:
        print(linea[0]+' '*espacios)
