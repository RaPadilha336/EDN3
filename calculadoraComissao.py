nome = input("Digite o nome do vendedor: ")
salario_fixo = float(input("Digite o salário fixo: R$ "))
vendas = float(input("Digite o total de vendas do mês: R$ "))

comissao = vendas * 0.15
total = salario_fixo + comissao

print(f"TOTAL = R$ {total:.2f}")

