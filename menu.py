def menu():
    print("Bienvenido al menú de partidos del equipo de futbol UNAB.")
    print("¿Qué desea realizar?")
    print("1. Registrar partido")
    print("2. Ver resultados")
    print("3. Tabla de clasificación")
    print("4. Salir")
    opc = int(input("Digite su opción: "))
    if opc == 1:
        registrar_partido(partidos)
    elif opc == 2:
        ver_resultados(partidos)
    elif opc == 3:
        ver_tabla_clasi(partidos)
    elif opc == 4:
        print("adios")
        exit(1)
    else:
        print("Opción no valida, intente de nuevo")
        menu()

def validar_goles(goles):
    while(goles < 0):
        print("Ingrese una cantidad de goles mayor o igual a 0: ")
        goles = int(input())
    return goles

def definir_fecha():
    print("Vamos a registrar la fecha!")
    anio = int(input("Ingrese el año en formato AAAA: "))
    while(anio < 0 or anio > 2021):
        anio = int(input("Año incorrecto, ingrese el año en formato AAAA: "))
    mes = int(input("Ingrese el mes en formato MM: "))
    while(mes <= 0 or mes > 12):
        mes = int(input("Mes incorrecto, ingrese el mes en formato MM: "))
    dia = int(input("Ingrese el día en formato DD: "))
    if (mes == 2):
        if (dia == 29):
            while not (anio % 4 == 0 and (not (anio % 100 == 0) or anio % 400 == 0)):
                dia = int(input("Día erróneo, ingrese el día en formato DD: "))
        while (dia <= 0 or dia > 29):
            dia = int(input("Día erróneo, ingrese el día en formato DD: "))
    if(mes == 1 or mes == 3 or mes == 5 or mes == 7 or mes == 8 or mes == 10 or mes == 12):
        while(dia <= 0 or dia > 31):
            dia = int(input("Día erróneo, ingrese el día en formato DD: "))
    if(mes == 4 or mes == 6 or mes == 9 or mes == 11):
        while(dia <= 0 or dia > 30):
            dia = int(input("Día erroneo, ingrese el día en formato DD: "))
    return dia, mes, anio

def registrar_partido(partidos):
    print("Vamos a registrar un partido!")
    try:
        dia, mes, anio = definir_fecha()
        print("Ingrese el nombre del equipo rival: ")
        nombre_rival = input()
        print("Ingrese la cantidad de goles hechos por el rival: ")
        goles_rival = int(input())
        goles_rival = validar_goles(goles_rival)
        print("Ingrese la cantidad de goles hechos por UNAB: ")
        goles_unab = int(input())
        goles_unab= validar_goles(goles_unab)
        partidos.append([dia, mes, anio, nombre_rival, goles_rival, goles_unab])
        print(partidos)
        print("¿Desea ingresar otro partido?")
        cond = str(input("S/N"))
    except:
        print("Alguno de los datos estan mal registrado, intente de nuevo")
        registrar_partido(partidos)
    if(cond == "S" or cond == "s"):
        registrar_partido(partidos)
    menu()

def ordenar_partidos(partidos):
    n = len(partidos)
    #Organiza primero por el año
    for i in range(n-1):
        for j in range(n-i-1):
            if partidos[j][2] < partidos[j+1][2]:
                partidos[j], partidos[j+1] = partidos[j+1], partidos[j]

    #Organiza por el mes solo si los partidos son del mismo año
    for i in range(n-1):
        for j in range(n-i-1):
            if(partidos[j][2] == partidos[j+1][2]):
                if partidos[j][1] < partidos[j+1][1]:
                    partidos[j], partidos[j+1] = partidos[j+1], partidos[j]

    #Organiza por el dia si los partidos son del mismo mes y año
    for i in range(n-1):
        for j in range(n-i-1):
            if(partidos[j][2] == partidos[j+1][2]):
                if(partidos[j][1] == partidos[j+1][1]):
                    if partidos[j][0] < partidos[j+1][0]:
                        partidos[j], partidos[j+1] = partidos[j+1], partidos[j]
    return partidos

def dar_formato(partido):
    if(partido[0] < 10):
        s_dia = "0"+str(partido[0])
    else:
        s_dia = str(partido[0])
    if(partido[1] < 10):
        s_mes = "0"+str(partido[1])
    else:
        s_mes = str(partido[1])
    s_anio = str(partido[2])
    return (s_dia+"-"+s_mes+"-"+s_anio+" - UNAB ("+str(partido[5])+")"
        +" VS "+partido[3]+"("+str(partido[4])+")")

def ver_resultados(partidos):
    ordenar_partidos(partidos)
    print("Resultados de los partidos:")
    for partido in partidos:
        print(dar_formato(partido))
    menu()

def ver_tabla_clasi(partidos):
    par_jug = len(partidos)
    par_gan = 0
    par_per = 0
    par_emp = 0
    puntos = 0
    for partido in partidos:
        if(partido[5] > partido[4]):
            puntos += 3
            par_gan += 1
        elif(partido[5] < partido[4]):
            par_per += 1
        elif(partido[5] == partido[4]):
            puntos +=1
            par_emp +=1

    print("Tabla clasificación:")
    print("Jugados Ganados Perdidos Empatados Puntos")
    print(str(par_jug)+"   "+str(par_gan)+"   "+str(par_per)+"   "+str(par_emp)+
        "   "+str(puntos))
    menu()

if __name__ == '__main__':
    partidos = []
    menu()
