"""Diagrama y programa para averiguar e imprimir cuantos multiplos de 7 y 9 hay en lso numeros comprendidos entre 1000 y 5000"""

from re import M


m = int(input("Digite el valor de m: "))
n = int(input("Digite el valor de n: "))

m_7 = 0
m_9 = 0
for i in range (1000, 5001, 1):
    if i%7 == 0:
        m_7 += 1
    if i%9 == 0:
        m_9 += 1

print
print(f"Entre {m} y {n} hay: ")
print(f"{m_7} multiplos de 7")
print(f"{m_9} multiplos de 9")