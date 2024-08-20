deposito = float(input("Digite o valor do depósito: "))
taxa_juros = float(input("Digite a taxa de juros (em decimal): "))

rendimento = deposito * taxa_juros
valor_total = deposito + rendimento

print("Rendimento:", rendimento)
print("Valor total:", valor_total)