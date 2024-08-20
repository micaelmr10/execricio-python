salario = float(input("Digite o salário do funcionário: "))
percentual_aumento = float(input("Digite o percentual de aumento: "))

aumento = salario * (percentual_aumento / 100)
novo_salario = salario + aumento

print("Valor do aumento:", aumento)
print("Novo salário:", novo_salario)