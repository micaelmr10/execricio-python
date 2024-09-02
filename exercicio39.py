numero = int(input("Digite um número inteiro menor que 1000: "))

centenas = numero // 100
dezenas = (numero % 100) // 10
unidades = numero % 10

if centenas > 0:
    print(f"{centenas} centena{'s' if centenas > 1 else ''}", end="")
    if dezenas > 0 or unidades > 0:
        print(", ", end="")
if dezenas > 0:
    print(f"{dezenas} dezena{'s' if dezenas > 1 else ''}", end="")
    if unidades > 0:
        print(" e ", end="")
if unidades > 0:
    print(f"{unidades} unidade{'s' if unidades > 1 else ''}")