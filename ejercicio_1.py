nombre = input("Digite su nombre: ")
suma = 0
s1 = 0
s2 = 0
s3 = 0
s4 = 0
for letra in nombre:
    if letra == "a":
        suma = suma + 1
        print("La vocal a sale: " + str(suma))
    elif letra == "e":
        s1 = s1 + 1
        print("La vocal e sale: " + str(s1))
    elif letra == "i":
        s2 = s2 + 1
        print("La vocal i sale: " + str(s2))
    elif letra == "o":
        s3 = s3 + 1
        print("La vocal o sale: " + str(s3))
    elif letra == "u":
        s4 = s4 + 1
        print("La vocal u sale: " + str(s4))