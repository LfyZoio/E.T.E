nome = input("Digite o nome do funcionário: ")
salario_bruto = float(input("Digite o salário bruto do funcionário: "))
salario_liquido = salario_bruto * 0.8  
print(f"O salário líquido do funcionário {nome} é: R${salario_liquido:.2f}")
print(f"O salário bruto do funcionário {nome} é: R${salario_bruto:.2f}")