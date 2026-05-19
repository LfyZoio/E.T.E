usuario = input("Digite o nome de usuário: ")
senha = input("Digite a senha: ")
print(f"Usuário: {usuario}")
print(f"Senha: {senha}")
if usuario == "admin" and senha == "1234":
    print("Acesso concedido!") 
else:    print("Acesso negado!")
str(input("Pressione Enter para sair..."))
loop = True
while loop:
    resposta = input("Deseja tentar novamente? (s/n): ")
    if resposta.lower() == "s":
        usuario = input("Digite o nome de usuário: ")
        senha = input("Digite a senha: ")
        print(f"Usuário: {usuario}")
        print(f"Senha: {senha}")
        if usuario == "admin" and senha == "1234":
            print("Acesso concedido!") 
            loop = False
        else:
            print("Acesso negado!")
    elif resposta.lower() == "n":
        print("Encerrando o programa.")
        loop = False
    else:
        print("Resposta inválida. Por favor, digite 's' para sim ou 'n' para não.")
