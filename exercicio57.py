suspeito = 0
print("Responda as seguintes perguntas com 'sim' ou 'não':")
print("a. Telefonou para a vítima?")
resposta = input().lower()
if resposta == "sim":
  suspeito += 1
print("b. Esteve no local do crime?")
resposta = input().lower()
if resposta == "sim":
  suspeito += 1
print("c. Mora perto da vítima?")
resposta = input().lower()
if resposta == "sim":
  suspeito += 1
print("d. Devia para a vítima?")
resposta = input().lower()
if resposta == "sim":
  suspeito += 1
print("e. Já trabalhou com a vítima?")
resposta = input().lower()
if resposta == "sim":
  suspeito += 1
if suspeito == 2:
  print("Classificação: Suspeita")
elif 3 <= suspeito <= 4:
  print("Classificação: Cúmplice")
elif suspeito == 5:
  print("Classificação: Assassino")
else:
  print("Classificação: Inocente")