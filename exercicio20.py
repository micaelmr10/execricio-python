turno = input("Em que turno você estuda? (M-matutino, V-Vespertino, N-Noturno): ").upper()

if turno == "M":
  print("Bom dia!")
elif turno == "V":
  print("Boa tarde!")
elif turno == "N":
  print("Boa noite!")
else:
  print("Turno inválido!")