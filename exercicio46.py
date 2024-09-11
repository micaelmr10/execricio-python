numero = int(input("Digite um número entre 1 e 10: "))

print("TABUADA de", numero, ":")

for i in range(1, 11):
    print(f"{numero} X {i} = {numero * i}")