#nombres
nombre = input("Nombre: ")
mascota = input("Nombre de su mascota: ")
contraseña = ""

#complementos
caracteres = "¡!¿?@#$%&_-+*=|}{[].,;:<>'"
letra="abcdefghijklmnñopqrstuvwxyz"
letras = letra.upper()
numero="0123456789"

#ciclo
contra = True
while contra:
    contraseña = input("Contraseña propuesta (FIN para terminar): ")
    if contraseña == "FIN":
        contra = False
    else:
        valido = True
        if len(contraseña) < 10:
            print("Contraseña muy corta, debe tener al menos 10 caracteres.")
        else:
            #minusculas
            minus=False
            for b in contraseña:
                for v in letra:
                    if v in b:
                        minus=True
            #mayusculas
            mayus=False
            for p in contraseña:
                for a in letras:
                    if a in p:
                        mayus=True
            #caracteres
            caracter=False            
            for m in contraseña:
                for x in caracteres:
                    if x in m:
                        caracter = True  
            #numeros
            num=False
            for o in contraseña:
                for n in numero:
                    if n in o:
                        num=True
            #patrones
            patron=False
            contador = 1
            i = 0
            while i < len(contraseña)-1:
                if contraseña[i] == contraseña[i+1]:
                    contador += 1
                    if contador >= 5:
                        patron = True
                else:
                    contador = 1
                i+=1   
                       
            #verificaciones
            if not minus:
                print("Debe incluir letras minusculas.")
                valido=False
            elif not mayus:
                print("Debe incluir letras mayúsculas.")
                valido=False
            elif not num:
                print("Debe incluir dígitos numéricos.")
                valido=False
            elif not caracter:
                print("Debe incluir caracteres especiales válidos.")
                valido=False                             
            elif nombre in contraseña:
                print("Contraseña no debe incluir su nombre.")
                valido=False
            elif mascota in contraseña:
                print("Contraseña no debe incluir el nombre de su mascota.")
                valido=False
                
            if patron:
                print("Contraseña no debe contener patrones:")
                valido=False
                
            #valida
            if valido:
                print("contraseña valida")
            
            
                