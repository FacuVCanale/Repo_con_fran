
numeros = []
prom = 0
num = abs(int(input('Cuantos numeros queres promediar2? ')))
if num == 0:
   print('No hay ningún número')
else:
    for i in range(num): 
        cant = 0   
        cant = int(input('Pone los números '))
        prom += 1
        numeros.append(cant)
        promedio = sum(numeros)//prom
        
print(promedio)

# Deberás hacer algo más así:

 ##                                                          TRABAJO PRÁCTICO 1


## CAMBIO DIARIO DE PECES:

y = 22031            #es la cantidad de peces                                                        SIEMPRE >= 0
alpha = 0.000082     #es la tasa de reproducción de los peces                                        SIEMPRE >= 0
beta = 24487         #es la capacidad del lago (para contener a la población de peces)               MAXIMO 50.000
gamma = 0.1          #es la proporción de peces que son comidos por otros depredadores en el lago    SIEMPRE >= 0
x = 0              #es la cantidad de pesca diaria                                                 

cambio_diario = alpha * y * (beta - y) - gamma * y - x

## Evolución temporal de la población:
# y(t+1) = yt + cambio_diario(yt)

y2 = y + cambio_diario


###                                                 SIMULADOR DE POBLACIÓN

while True:
    y0 = int(input("Ingrese y0: "))
    if y0 < 0 or y0 > 50000:
        print("Ingrese un valor válido.")
        continue
    break

while True:
    x = int(input("Ingrese x: "))
    if x < 0:
        print("Ingrese un valor válido.")
        continue
    break

while True:
    alpha = float(input("Ingrese alfa: "))
    if alpha < 0:
        print("Ingrese un valor válido.")
        continue
    break

while True:
    beta = int(input("Ingrese beta: "))
    if beta > 50000 or beta < 0:
        print("Ingrese un valor válido.")
        continue
    break

while True:
    gamma = float(input("Ingrese gama: "))
    if gamma < 0.0:
        print("Ingrese un valor válido.")
        continue
    break

while True:
    n = int(input("Ingrese N: "))
    if n < 0:
        print("Ingrese un valor válido.")
        continue
    break

cambio_diario = 0

y0lenght= len(str(y0))

print("Tabla de valores:\n t_i    |  y_i\n--------+--------\n 0      |" + " " * (6 - y0lenght) + str(y0))

for i in range(1,n+1):
    if len(str(i)) == 1:
        print(" " + str(i) + " " * 6, end= "|")
    else:
        print(str(i) + " " * (8 - len(str(i))), end= "|")
    cambio_diario = alpha * y0 * (beta - y0) - gamma * y0 - x
    y0 += cambio_diario
    if y0 <= 0:
        print(" " * 5 + "0")
        y0 = 0
    else:
        print(" " * (6 -len(str(int(y0)))) + str(int(y0)))
    
## ALGUNAS DUDAS:
#     if y0 > 50000:
#        print(" 50000")
#        y0 = 50000"
# Es necesario? Parece compensarse sólo. No Facu, no es necesario. Debes hacerlo con furrys.

# Si pongo y0 mayor a beta medio que no tiene sentido que de un 
# inicio haya más peces que los posibles del lago, pero bueno, 
# en el siguiente día ya se acomoda, pero de entrada no tiene sense.

# Cuando ponen un y0 negativo no dice que es negativo, sólo que no es válido. Hace falta ponerlo igual?


## CHEQUEAR VARIABLES SI SON NEGATIVAS CON UNA SOLA FUNCIÓN QUE DEVUELVA UN BOOLEANO.


 