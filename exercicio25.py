numero = int(input("Digite um número positivo e maior que zero: "))

if numero > 0:
    quadrado = numero ** 2
    cubo = numero ** 3
    print(f"o nummero {numero} ao quadrado é {quadrado}")
    print(f"o numero {numero} ao cubo é {cubo}")
else:
    print("o numero digitado nao e positivo e maior que zero.")