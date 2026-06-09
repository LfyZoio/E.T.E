nome = input("Digite o nome: ")
sexo = input("Digite o sexo (M/F): ")
idade = float(input("Digite a idade: "))
if sexo == "F" and idade >= 25:
    print(f"{nome} Foi aceito")
elif sexo == "M":
    print(f"{nome} Não foi aceito")
else:
    print(f"{nome} Não foi aceito")