anonascimentoatleta = int(input("Digite o ano de nascimento do atleta: "))
idade = 2026 - anonascimentoatleta
if idade < 9:
    print("Atleta infantil") 
elif idade >= 10 and idade <= 14:
    print("Atleta juvenil") 
elif idade >= 15 and idade <= 19:
    print("Atleta junior")
elif idade >= 20 and idade <= 25:
    print("Atleta sênior")
else:
    print("Atleta master")