numeros = []

while True:
    num = (input("""Digite os números:
Digite X se quiser finalizar """))
    if num.upper() == "X":
        break
    try:
        num = int(num)
        numeros.append(num)
    except ValueError:
        print("""Digite apenas numeros ou "X""")

for i in range (len(numeros)):
    for n in range (len(numeros)-1):
        if numeros[n+1] < numeros[n]:
            temp = numeros[n+1]
            numeros[n+1] = numeros[n]
            numeros[n] = temp
print(f"Os números em ordem crescente são: {numeros}")










































