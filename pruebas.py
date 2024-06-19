def ganadores_tipo_torneo(nombre_archivo, tipo, año):
    archivo = open(nombre_archivo, "r")
    lista={}
    for linea in archivo:
            l=linea.strip().split(";")
            if int(l[0])==año and l[4] == tipo and l[3]=="The Final":
                sub_lista=[]
                sub_lista.append(l[1])
                sub_lista.append(l[5])
                sub_lista.append(l[7] + "-" + l[2]) 
                lista[l[-2]] = sub_lista
    archivo.close()
    return lista

def construir_resumen(nombre_archivo, año1, año2):
    leer=open(nombre_archivo,"r")
    resumen1={}
    resumen2={}
    for linea in leer:
        l = linea.strip().split(";")
        año = int(l[0])
        jugador = l[6].strip()
        if año == año1:
            if jugador in resumen1:
                resumen1[jugador]+=1
            else:
                resumen1[jugador]=1
        elif año == año2:
            if jugador in resumen2:
                resumen2[jugador]+=1
            else:
                resumen2[jugador]=1
    leer.close    
    nombre_resumen="resumen_ATP_"+str(año1)+"-"+str(año2)+".txt"  
    archivo=open(nombre_resumen,"w") 
    archivo.write("Asociación de Tenis de Pythonia\n")
    archivo.write("Resumen " +str(año1)+"-"+str(año2)+"\n")
    archivo.write("\n")
    archivo.write("Jugadores con más partidos ganados en " +str(año1)+"\n")
    archivo.write("\n")
    top1=[]
    for jugadores in resumen1:
        partidos=resumen1[jugadores]
        top1.append((partidos, jugadores))
        top1.sort()
        top1.reverse()
        lista_top=top1
        top_1=[]
        for top10 in lista_top:
            if len(top_1)<10:
                top_1.append(top10)
    i=0
    while i < len(top_1):
        x = top_1[i]
        archivo.write(str(i + 1) + ". " + str(x[1]) + " con " + str(x[0]) + " triunfos\n")
        i += 1
    archivo.write("\n")
    archivo.write("Jugadores con más partidos ganados en " +str(año2)+"\n")
    archivo.write("\n")
    top2=[]
    for jugadores in resumen2:
        partidos=resumen2[jugadores]
        top2.append((partidos, jugadores))
        top2.sort()
        top2.reverse()
        lista_top=top2
        top_2=[]
        for top10x in lista_top:
            if len(top_2)<10:
                top_2.append(top10x)
    p=0
    while p < len(top_2):
        x2 = top_2[p]
        archivo.write(str(p + 1) + ". " + str(x2[1]) + " con " + str(x2[0]) + " triunfos\n")
        p += 1
    archivo.close
    
    total_jugadores=top_1+top_2 
    contador=[]
    for total in total_jugadores:
        nombre=total[1]
        if nombre not in contador:
            contador.append(nombre)
    contador_total=len(contador)
    
    return len(contador)

print(construir_resumen("datos_atp.csv", 2003, 2004))