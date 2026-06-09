name1 = float(input("Digite um número: "))
name2 = float(input("Digite outro número: "))
name3 = float(input("Digite mais um número: "))
if name1 > name2 and name1 > name3:
    print(f"O número {name1} é maior que os números {name2} e {name3}")
elif name2 > name1 and name2 > name3:
    print(f"O número {name2} é maior que os números {name1} e {name3}")
elif name3 > name1 and name3 > name2:
    print(f"O número {name3} é maior que os números {name1} e {name2}")
else:
    print("Os números são iguais")