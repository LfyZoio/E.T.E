usuario = input("Digite o nome de usuário: ")
senha = input("Digite a senha: ")
print(f"Usuário: {usuario}")
print(f"Senha: {senha}")
if usuario == "admin" and senha == "1234":
    print("Acesso concedido!") 
else:    print("Acesso negado!")
str(input("Pressione Enter para sair..."))