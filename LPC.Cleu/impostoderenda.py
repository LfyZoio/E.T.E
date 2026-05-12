nome = input("Digite o seu nome: ")
salario = float(input("Digite o valor do seu salário: "))
if salario <= 1903.98:
    print(f"{nome}, você está isento do imposto de renda.")
elif salario <= 2826.65:
    imposto = salario * 0.075
    print(f"{nome}, o valor do imposto de renda é: R${imposto:.2f}")
elif salario <= 3751.05:
    imposto = salario * 0.15
    print(f"{nome}, o valor do imposto de renda é: R${imposto:.2f}")
elif salario <= 4664.68:
    imposto = salario * 0.225
    print(f"{nome}, o valor do imposto de renda é: R${imposto:.2f}")
else:
    imposto = salario * 0.25  
    print(f"{nome}, o valor do imposto de renda é: R${imposto:.2f}")