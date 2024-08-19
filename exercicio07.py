nome_diciplinas=input("digite o nome das diciplinas:")

nota1=float(input("digite a nota 1:"))
nota2=float(input("digite a nota 2:"))
nota3=float(input("digite a nota 3:"))
nota4=float(input("digite a nota 4:"))
media=(nota1+nota2+nota3+nota4)/4

if media >= 7:
  condicao = "aprovado"
else:
  condicao = "reprovado"

print(f"disiplina: {nome_diciplinas}")
print(f"media: {media}")
print(f"condicao:{condicao}")
