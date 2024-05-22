
for i in range(7):
    numero = []
    pedirNumeros = int(input("ingresa un numeros:"))
    numero.append(pedirNumeros)


    seEncontroPositivos = False
    for n in numero:

     if n > 0:
        seEncontroPositivos = True

if seEncontroPositivos:
   print("se encontro numeros positivo")
else:
   print("no")

