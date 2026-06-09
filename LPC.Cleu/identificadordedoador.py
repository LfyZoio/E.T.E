nome = str(input("Digite o nome: "))
idade = int(input("Digite a idade: "))
peso = float(input("Digite o peso: "))
if idade >=16 and idade <=69 and peso >=50:
    print(f"{nome} é um doador de sangue apto")
else:
    print(f"{nome} não é um doador de sangue apto")
    print("O doador deve ter entre 16 e 69 anos e pesar mais de 50 kg")