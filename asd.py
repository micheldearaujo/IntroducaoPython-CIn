numeros = [89]
inicio = 89
contador1= 30
contador2 = -23
for i in range(1, 1000):
    if i % 2 == 0:
        numeros.append(inicio + contador2)
        inicio = inicio+contador2
        contador2 -=1
    else:
        numeros.append(inicio + contador1)
        inicio=inicio+contador1
        contador1 +=1


c = 0
for elemento in numeros:
    if elemento > 1000 and elemento < 1500:
        c+=1

print(c)