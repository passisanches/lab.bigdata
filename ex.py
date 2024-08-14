#Faça um programa no que crie/gere uma lista capaz de armazenar 1000 idades de pessoas (valores entre 0 a 100). Mostre a idade media, a moda e a mediana. Considerando agora, que precisaremos ter apenas idades de adultos (>=21), faça com que todas as idades menores que 21 sejam substituídas pela media das idades >= 21 anos.


import random
import statistics


idades = [random.randint(0, 100) for _ in range(1000)]


media = statistics.mean(idades)
moda = statistics.mode(idades)
mediana = statistics.median(idades)

print("Média das idades:", media)
print("Moda das idades:", moda)
print("Mediana das idades:", mediana)


idades_adultos = [idade for idade in idades if idade >= 21]


media_adultos = statistics.mean(idades_adultos)


for i in range(len(idades)):
  if idades[i] < 21:
    idades[i] = media_adultos

print("Idades após substituição:", idades)