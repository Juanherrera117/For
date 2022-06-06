"""Hacer el diagrama de flujo y el programa en python que genere 1000 numeros aleatorios y que averigue e imprima 
cuantos son pares y cuantos son impares"""
import random
n = int(input("Digite la cantidad de numeros: "))

pares = 0
impares = 0
rta = "Numeros = ("

for i in range(n):
    num_aleatorio = random.randint(1,200)
    if num_aleatorio % 2 == 0:
        pares += 1
    else:
        impares += 1
    if i < n-1:
        rta = rta + str(num_aleatorio) + ", "
    else:
         rta = rta + str(num_aleatorio)
rta = rta + ")"

print("----Resultado----")
print(rta)
print(f"cantidad de pares = {pares}")
print(f"cantidad de impares = {impares}")
