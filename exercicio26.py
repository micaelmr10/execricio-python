num1 = int(input("Digite o primeiro número: "))
num2 = int(input("Digite o segundo número: "))

if num1 > 0 and num2 > 0 and num2 <= 10:
  resultado = num1 ** num2
  print(f"{num1} elevado a {num2} é igual a {resultado}")
else:
  print("Os números devem ser maiores que zero e o segundo número deve ser no máximo 10.")
  