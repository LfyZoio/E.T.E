


turno = input(f"digite o seu turno")

match turno:
    case 1:
        print("matutino")
    case 2:
        print("vespertino")
    case 3:
        print("noturno")
    case _:
        print("turno invalido")
        