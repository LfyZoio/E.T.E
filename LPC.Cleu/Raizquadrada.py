numero = float(input("digite um numero"))
raiz = numero ** (1/2)  
print(f"a raiz quadrada de {numero} é: {raiz}")

if raiz <= 0:
    print("Não é possível calcular a raiz quadrada de um número negativo.")
else:
    print(f"A raiz quadrada de {numero} é: {raiz}")
