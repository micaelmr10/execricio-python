
idade = int(input("que ano voce nasceu: "))
ant = 2024
anm = 2019
meses = 12
sema = 52
dias = 365
idant = ant-idade
idan = anm-idade
idme = idade*meses
idse = idade*sema
iddia = idade*dias
print("voce tem", idant, "anos")
print(f"voce tinha {idan} em 2019")
print(f"voce tinha {idme} meses de vida")
print(f"voce tinha {idse} semanas de vida")
print(f"voce tinha {iddia} dias de vida")