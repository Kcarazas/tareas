valor=input("palabra:")
vocales="aeiou"
contador=0
for a in valor:
    if a in vocales:
        contador+=1
print(contador)

def get_top_10(resumen):
    top_10 = []
    for jugador in resumen:
        partidos = resumen[jugador]
        if len(top_10) < 10 or partidos > top_10[0][1]:
            if len(top_10) == 10:
                top_10.pop(0)
            top_10.append((jugador, partidos))
            top_10.sort() 
            top_10.reverse()
    return top_10