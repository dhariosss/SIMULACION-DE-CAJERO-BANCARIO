saldo = 1000

while True:
    print("\n1. Deposito")
    print("2. Retiro")
    print("3. Salir")

    opcion = input("Opcion: ")

    if opcion == "1":
        cantidad = float(input("Cantidad: "))
        Saldo = Saldo + cantidad
        print("Saldo:", Saldo)

    elif opcion == "2":
        cantidad = float(input("Cantidad: "))
        if cantidad <= Saldo:
            Saldo = Saldo - cantidad
            print("Saldo:", Saldo)
        else:
            print("No te alcanza el saldo dinero eres  pobre jj")

    elif opcion == "3":
        print("Gracias por confinar en nuestra entidad financiera ELCONDOR")
        break

    else:
        print("Opcion erronea")