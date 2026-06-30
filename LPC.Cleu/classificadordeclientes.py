#ler o valor do faturamento e classificar o cliente
name = float(input("digite seu nome: "))
gasto = float(input("Digite o valor do gasto: "))
#classificar o cliente com base no faturamento
if gasto > 5000:
    print(f"{name}, Categoria Diamante (15% de desconto)")
elif gasto > 3000:
    print(f"{name}, Categoria Ouro (10% de desconto)")
elif gasto > 1000:
    print(f"{name}, Categoria Prata (5% de desconto)")
else:
    print(f"{name}, Categoria Bronze (sem desconto)")