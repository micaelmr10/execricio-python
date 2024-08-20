salario_base = float(input("Digite o salário-base do funcionário: "))
gratificacao = salario_base * 0.05
imposto = salario_base * 0.07
salario_a_receber = salario_base + gratificacao - imposto
print(f"O salário a receber é: R$ {salario_a_receber:.2f}")