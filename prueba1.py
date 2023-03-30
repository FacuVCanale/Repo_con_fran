
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
 