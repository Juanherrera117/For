"""Generar la siguiente serie: 2,4,8,16,32,64,...n"""

n = int(input("Digite el valor de n: "))
s = "Serie: "
for i in range(1,n+1):
    t = ((i**2)+1)
    if i < n: 
        s = s + "1/" + str(t) + ", "
    else:
        s = s + "1/" + str(t)

print("---Resultado---")
print(s)