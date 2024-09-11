n1 = int(input("Digite o primeiro número: "))
n2 = int(input("Digite o segundo número: "))

if n1 < n2:
    for i in range(n1, n2 + 1):
        print(i)
else:
    for i in range(n2, n1 + 1):
        print(i)