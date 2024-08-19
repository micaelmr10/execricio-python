def tipo_triangulo(a, b, c):
  """
  Esta função recebe os comprimentos dos três lados de um triângulo
  e retorna o tipo de triângulo (equilátero, isósceles ou escaleno).
  """
  if a == b == c:
    return "Equilátero"
  elif (a == b) or (a == c) or (b == c):
    return "Isósceles"
  else:
    return "Escaleno"

a = float(input("Digite o comprimento do lado A: "))
b = float(input("Digite o comprimento do lado B: "))
c = float(input("Digite o comprimento do lado C: "))

tipo = tipo_triangulo(a, b, c)

print(f"O triângulo é {tipo}.")