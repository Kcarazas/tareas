import random
import math
a = random.randint(0,2)
b = random.randint(0,2)
print("¿donde está el tesoro?")
i=True
while i:
    x = int(input("ingrese posicion x: "))
    y = int(input("ingrese posicion y: "))
    if x == a and y == b:
        print("tesoro encontrado")
        i=False
    else:
        d = math.sqrt((a-x)**2+(b-y)**2)
        print("la distancia del tesoro es",d)
        

