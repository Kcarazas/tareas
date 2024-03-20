print("Bienvenido a la Pizzeria di Napoli")
tarjeta=input("Tienes tarjeta de comelón frecunete (si/no)? ")
pizza=input("De que quieres tu pizza? ")
print("puedes pedir doble",pizza)
doble=input("Quieres (si/no)? ")
bebida=input("Deseas llevar combo de bebida? (si/no): ")
print("Puedes agregar un complemento: ")
print("1. Empanadas de queso")
print("2. Alitas de pollo")
print("3. Papas fritas")
print("0. nada")
opcion = input("Opcion: ")

precio=3000
if tarjeta=="si":
    descuento=precio*0.10
    precio_descuento= precio-descuento
else:
    precio_descuento=precio
#pizza vegetariana
if pizza == "pimiento" or pizza=="albahaca":
    ingredientes=500
    if opcion == "1":
            complemento=500
            nombre_complemento="empanadas de queso"
            print("Disfruta tu pizza vegetariana con mozzarella, tomate y doble",pizza,"con complemento de",nombre_complemento,"!")
    elif opcion == "2":
            complemento=500
            nombre_complemento="alitas de pollo"
            print("Disfruta tu pizza vegetariana con mozzarella, tomate y doble",pizza,"con complemento de",nombre_complemento,"!")
    elif opcion == "3":
            complemento=500
            nombre_complemento="papas fritas"
            print("Disfruta tu pizza vegetariana con mozzarella, tomate y doble",pizza,"con complemento de",nombre_complemento,"!")
    elif opcion == "0":
        complemento=0
        print("Disfruta tu pizza vegetariana con mozzarella, tomate y doble",pizza)
    if bebida=="si":
            bebida=1000
            print("No olvides la bebida de tu combo.")
    else:
        bebida = 0
    if doble == "si":
        ingrediente_doble = 2*ingredientes
    else:
        ingrediente_doble=0
    total=precio_descuento+ingrediente_doble+complemento+bebida
    print("El total de tu compra es: $",total)
    
#pizza veganas
elif pizza == "tofu" or "nueces" or "brocoli":
    ingredientes=700
    if opcion == "1":
            complemento=500
            nombre_complemento="empanadas de queso"
            print("Disfruta tu pizza vegetariana con mozzarella, tomate y doble",pizza,"con complemento de",nombre_complemento,"!")
    elif opcion == "2":
            complemento=500
            nombre_complemento="alitas de pollo"
            print("Disfruta tu pizza vegetariana con mozzarella, tomate y doble",pizza,"con complemento de",nombre_complemento,"!")
    elif opcion == "3":
            complemento=500
            nombre_complemento="papas fritas"
            print("Disfruta tu pizza vegetariana con mozzarella, tomate y doble",pizza,"con complemento de",nombre_complemento,"!")
    elif opcion == "0":
        complemento=0
        print("Disfruta tu pizza vegetariana con mozzarella, tomate y doble",pizza)
    if bebida=="si":
            bebida=1000
            print("No olvides la bebida de tu combo.")
    else:
        bebida = 0
    if doble == "si":
        ingrediente_doble = 2*ingredientes
    else:
        ingrediente_doble=0
    total=precio_descuento+ingrediente_doble+complemento+bebida
    print("El total de tu compra es: $",total)
    
    #pizza no vegetariana    
elif pizza == "pepperoni" or pizza=="jamon" or pizza=="salmon":
    ingredientes=1000
    if opcion == "1":
            complemento=500
            nombre_complemento="empanadas de queso"
            print("Disfruta tu pizza vegetariana con mozzarella, tomate y doble",pizza,"con complemento de",nombre_complemento,"!")
    elif opcion == "2":
            complemento=500
            nombre_complemento="alitas de pollo"
            print("Disfruta tu pizza vegetariana con mozzarella, tomate y doble",pizza,"con complemento de",nombre_complemento,"!")
    elif opcion == "3":
            complemento=500
            nombre_complemento="papas fritas"
            print("Disfruta tu pizza vegetariana con mozzarella, tomate y doble",pizza,"con complemento de",nombre_complemento,"!")
    elif opcion == "0":
        complemento=0
        print("Disfruta tu pizza vegetariana con mozzarella, tomate y doble",pizza)
    if bebida=="si":
            bebida=1000
            print("No olvides la bebida de tu combo.")
    else:
        bebida = 0
    if doble == "si":
        ingrediente_doble = 2*ingredientes
    else:
        ingrediente_doble=0
    total=precio_descuento+ingrediente_doble+complemento+bebida
    print("El total de tu compra es: $",total)