

turno = input("Digite o seu turno: ").strip().upper()

while turno not in ("M", "V", "N"):
    print("Valor inválido!")
    turno = input("Digite o seu novo turno: ").strip().upper()

if turno == "M":
    print("Bom dia!")
elif turno == "V":
    print("Boa tarde!")
elif turno == "N":
    print("Boa noite!")
    while  turno not in ("M", "V", "N"):
        print("Valor inválido!")
        turno = input("Digite o seu novo turno: ").strip().upper()        
    





