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

precio_pizza=3000
if tarjeta=="si":
    dc=precio_pizza*0.10
    descuento=precio_pizza-dc
    if pizza == "pimiento" or pizza=="albahaca":
        ingredientes=500
        if doble == "si":
            ingrediente_doble = 2*ingredientes
            if opcion == "1" or "2" or "3":
                complemento=500
                print("disfruta tu pizza",pizza,"con mozzarella, tomate y doble",pizza,"con complemento de",)
                if bebida == "si":
                    bebida=1000
                    print("No olvides la bebida de tu combo ")
                    total=descuento+ingrediente_doble+complemento+bebida
                    print("El total de tu compra es: %",total)
                else:
                    print("disfruta tu pizza",pizza,"con mozzarella, tomate y doble",pizza,"con complemento de empanadas de queso !")
                    total=descuento+ingrediente_doble+complemento
                    print("El total de tu compra es: %",total)
        else:
            if opcion == "1" or "2" or "3":
                complemento=500
                print("disfruta tu pizza",pizza,"con mozzarella, tomate",pizza,"con complemento de empanadas de queso !",)
                if bebida == "si":
                    bebida=1000
                    print("No olvides la bebida de tu combo ")
                    total=descuento+complemento+bebida
                    print("El total de tu compra es: %",total)
                else:
                    print("disfruta tu pizza",pizza,"con mozzarella, tomate y doble",pizza,"con complemento de empanadas de queso !")
                    total=descuento+complemento
                    print("El total de tu compra es: %",total)
    elif pizza == "tofu" or "nueces" or "brocoli":
        ingredientes=700
        if doble == "si":
            ingrediente_doble = 2*ingredientes
            if opcion == 1:
                complemento=500
                print("disfruta tu pizza",pizza,"con mozzarella, tomate y doble",pizza,"con complemento de empanadas de queso !",)
            if bebida == "si":
                bebida=1000
                print("No olvides la bebida de tu combo ")
                total=descuento+ingrediente_doble+complemento+bebida
            print("El total de tu compra es: %",total)
    elif pizza == "pepperoni" or pizza=="jamón" or pizza=="salmón":
        print("h")