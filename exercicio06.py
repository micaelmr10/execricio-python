n1 = float(input("digite o primeiro numero:"))
n2 = float(input("digite o segundo numero:"))

operacao = input("digite a operação desejada(soma ou subtração)")
resultado=0
if (operacao == '+'):
  resultado = n1 + n2
  print(f"o resultado é {resultado}")
elif (operacao == '-'):
  resultado = n1 - n2
  print(f"o resultado é {resultado}")
else:
  print("operação invalida")

