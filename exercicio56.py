numero = int(input("Digite um número entre 0 e 99: "))
if 0 <= numero <= 99:
  unidades = ["", "um", "dois", "três", "quatro", "cinco", "seis", "sete", "oito", "nove", "dez", "onze", "doze", "treze", "quatorze", "quinze", "dezesseis", "dezessete", "dezoito", "dezenove"]
  dezenas = ["", "", "vinte", "trinta", "quarenta", "cinquenta", "sessenta", "setenta", "oitenta", "noventa"]
  if numero < 20:
    print(unidades[numero])
  else:
    dezena = numero // 10
    unidade = numero % 10
    print(dezenas[dezena], end="")
    if unidade != 0:
      print(" e", unidades[unidade])
else:
  print("Número inválido. Digite um número entre 0 e 99.")