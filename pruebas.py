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
        jugador = l[6]
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
    top=[]
    for jugadores in resumen1:
        partidos=resumen1[jugadores]
        top.append((jugadores,partidos))
    top.sort()
    top.reverse()
    return top
print(construir_resumen("datos_atp.csv", 2003, 2004))