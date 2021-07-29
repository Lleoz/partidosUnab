import math

partidos = []


# MENU---------------------------------------------------------------------
def menu():
    print("Bienvenido al menú de partidos del equipo de futbol del torneo")
    print("¿Qué desea realizar?")
    print("1. Registrar equipos")
    print("2. Registrar partido")
    print("3. Estadisticas del torneo.")
    print("4. Tabla de Clasificación.")
    print("5. Salir")
    opc = int(input("Digite su opción: "))
    if opc == 1:
        registrar_equipos(equipos)
    elif opc == 2:
        registrar_partido(partidos)
    elif opc == 3:
        estadisticas(partidos)
    elif opc == 4:
        tablaDeClasificacion(partidos, equipos)
    elif opc == 5:
        print("Adiós")
        exit(0)
    else:
        print("Opción no valida")
        menu()
# --------------------------------------------------------------------------


# REGISTRAR EQUIPOS---------------------------------------------------------
def registrar_equipos(equipos):
    print("Estos son los equipos ya registrados:")
    print(equipos)
    print("Ingrese el número de equipos que quiere registrar")
    nom = int(input())
    print("Ingrese el nombre de los equipos que desee inscribir")
    for i in range(nom):
        z = input()
        equipos.append(z)
        print(equipos)
    menu()
# --------------------------------------------------------------------------


# VALIDAR GOLES-------------------------------------------------------------
def validar_goles(goles):
    while goles < 0:
        print("Ingrese una cantidad de goles mayor o igual a 0: ")
        goles = int(input())
    return goles
# --------------------------------------------------------------------------


# FECHAS--------------------------------------------------------------------
def definir_fecha():
    print("Vamos a registrar la fecha!")
    anio = int(input("Ingrese el año en formato AAAA: "))
    while anio < 0 or anio > 2021:
        anio = int(input("Año incorrecto, ingrese el año en formato AAAA: "))
    mes = int(input("Ingrese el mes en formato MM: "))
    while mes <= 0 or mes > 12:
        mes = int(input("Mes incorrecto, ingrese el mes en formato MM: "))
    dia = int(input("Ingrese el día en formato DD: "))
    if mes == 2:
        if dia == 29 and not (anio % 4 == 0 and (not (anio % 100 == 0) or anio % 400 == 0)):
            dia = int(input("Día erróneo, ingrese el día en formato DD: "))
        while dia <= 0 or dia > 29:
            dia = int(input("Día erróneo, ingrese el día en formato DD: "))
    if mes == 1 or mes == 3 or mes == 5 or mes == 7 or mes == 8 or mes == 10 or mes == 12:
        while dia <= 0 or dia > 31:
            dia = int(input("Día erróneo, ingrese el día en formato DD: "))
    if mes == 4 or mes == 6 or mes == 9 or mes == 11:
        while dia <= 0 or dia > 30:
            dia = int(input("Día erroneo, ingrese el día en formato DD: "))
    return dia, mes, anio
# --------------------------------------------------------------------------


# REGISTRAR PARTIDOS--------------------------------------------------------
def registrar_partido(partidos):
    print("Vamos a registrar un partido")
    try:
        dia, mes, anio = definir_fecha()
        print("Estos son los equipos ya registrados:")
        print(equipos)
        print("Ingrese el nombre del equipo local: ")
        nombre_local = input()
        if nombre_local in equipos:
            pass
        else:
            print("El equipo que marcó no se encuentra registrado")
            menu()
        print("ingrese el nombre del equipo visitante: ")
        nombre_rival = input()
        if nombre_rival in equipos:
            pass
        else:
            print("El equipo que marcó no se encuentra registrado")
            menu()
        print("Ingrese la cantidad de goles hechos por el equipo local: ")
        goles_visitante = int(input())
        goles_visitante = validar_goles(goles_visitante)
        print("Ingrese la cantidad de goles hechos por el equipo visitante: ")
        goles_local = int(input())
        goles_local = validar_goles(goles_local)
        partidos.append([dia, mes, anio, nombre_local, nombre_rival, goles_local, goles_visitante])
        print(partidos)
        print("¿Desea ingresar otro partido?")
        cond = str(input("S/N"))
    except:
        print("Alguno de los datos esta mal registrado, intente de nuevo")
        registrar_partido(partidos)
    if cond == "S" or cond == "s":
        registrar_partido(partidos)
    menu()
# --------------------------------------------------------------------------


# ESTADISTICAs---------------------------------------------------------------
def estadisticas(partidos):
    suma_local = 0
    suma_visitante = 0
    suma_total = 0
    cuenta = 0
    promedio1 = 0
    promedio2 = 0
    part = 0
    par_jug = len(partidos)
    print("Seleccione el tipo de dato que desee consultar")
    print("1. Estadísticas del torneo")
    print("2. Estadísticas por equipos")
    print("3. Regresar al menú principal")
    opc2 = int(input())
    if opc2 == 1:
        print("1. Media de goles por partido")
        print("2. Desviación estandar por goles")
        print("3. Regresar al menú anterior")
        opc3 = int(input("Digite su opción: "))
        if opc3 == 1:
            for i in partidos:
                suma_total = suma_total+i[6]+i[5]
            promedio = suma_total/par_jug
            print("La media de goles por partidos es: "+str(promedio))
            estadisticas(partidos)
        elif opc3 == 2:
            for i in partidos:
                suma_total = suma_total+i[6]+i[5]
            promedio = suma_total/par_jug
            for i in partidos:
                stdr = (i[6]+i[5]-promedio)**2
                cuenta = stdr+cuenta
            devs = math.sqrt(cuenta/par_jug)
            print("La desviación de los goles por partido en el torneo es: "+str(devs))
            estadisticas(partidos)
        elif opc3 == 3:
            estadisticas(partidos)
        else:
            estadisticas(partidos)
    # ACA EMPIEZA LA ESTADISTICA POR EQUIPOS
    elif opc2 == 2:
        pass
    elif opc2 == 3:
        menu()
    else:
        print("Opción inexistente")
        estadisticas(partidos)
    print("Estos son los equipos ya registrados:")
    print(equipos)
    print("Ingrese al equipo que quiere consultar")
    team = str(input())
    if team in equipos:
        pass
    else:
        print("El equipo marcado no se encuentra registrado")
        menu()
    for i in partidos:
        if i[3] == team:
            part = part+1
        if i[4] == team:
            part = part+1
    print(part)
    print("¿Qué desea consultar?")
    print("1. Goles anotados por partido")
    print("2. Goles recibidos por partido")
    print("3. Promedio de goles anotados y desviación estándar")
    print("4. Promedio de goles recibidos y desviación estándar")
    print("5. Cantidad de partidos ganados, perdidos y empatados.")
    opc4 = int(input("Digite su opción: "))
    if opc4 == 1:
        for i in partidos:
            if i[3] == team:
                suma_local = suma_local+i[6]
            if i[4] == team:
                suma_visitante = suma_visitante+i[5]
        puntos = suma_visitante+suma_local
        print("Los goles totales del equipo " + team+" " + str(puntos))
    elif opc4 == 2:
        for i in partidos:
            if i[3] == team:
                suma_local = suma_local+i[5]
            if i[4] == team:
                suma_visitante = suma_visitante+i[6]
        puntos = suma_visitante+suma_local
        print("Los goles recibidos por el equipo " + team+"son: " + str(puntos))
    elif opc4 == 3:
        for i in partidos:
            if i[3] == team:
                suma_local = suma_local + i[6]
            promedio1 = suma_local
            if i[4] == team:
                suma_visitante = suma_visitante + i[5]
            promedio2 = suma_visitante
        media1 = (promedio1+promedio2)/part
        print("La media de goles anotados por partido del equipo " + str(team)+"es: " + str(media1))
        puntos = suma_visitante + suma_local
        for i in partidos:
            if i[3] == team:
                stdr = (i[6]-puntos)**2
                cuenta = stdr+cuenta
            if i[4] == team:
                stdr = (i[5]-puntos)**2
                cuenta = stdr+cuenta
            devs = math.sqrt(cuenta/part)
            print("La desviación estándar por partidos para el equipo: " + str(team)+"es: " + str(devs))
        estadisticas(partidos)
    elif opc4 == 4:
        for i in partidos:
            if i[3] == team:
                suma_local = suma_local + i[5]
            promedio1 = suma_local
            if i[4] == team:
                suma_visitante = suma_visitante + i[6]
            promedio2 = suma_visitante
        media1 = (promedio1+promedio2)/part
        print("La media de goles recibidos por partido del equipo " + str(team) + "es: " + str(media1))
        puntos = suma_visitante + suma_local
        for i in partidos:
            if i[3] == team:
                stdr = (i[5]-puntos)**2
                cuenta = stdr+cuenta
            if i[4] == team:
                stdr = (i[6]-puntos)**2
                cuenta = stdr+cuenta
            devs = math.sqrt(cuenta/part)
            print("La desviación estándar por partidos para el equipo: " + str(team) + "es: " + str(devs))
        estadisticas(partidos)
    elif opc4 == 5:
        ganados = 0
        perdidos = 0
        empatados = 0
        for i in partidos:
            if i[3] == team:
                if i[6] < i[5]:
                    ganados = ganados+1
                elif i[6] > i[5]:
                    perdidos = perdidos+1
                elif i[6] == i[5]:
                    empatados = empatados+1
                print("Partidos ganados: " + str(ganados))
                print("Partidos perdidos: " + str(perdidos))
                print("Partidos empatados: " + str(empatados))
                menu()
    else:
        print("seleccion no válida")
        estadisticas(partidos)
# --------------------------------------------------------------------------


# ORGANIZAR TABLA POR PUNTAJE------------------------------------------------
def ordenarTabla(tblDeClasificacion):
    n = len(tblDeClasificacion)
    for i in range(n - 1):
        for j in range(n - i - 1):
            if tblDeClasificacion[j][1] < tblDeClasificacion[j + 1][1]:
                tblDeClasificacion[j], tblDeClasificacion[j + 1] = tblDeClasificacion[j + 1], tblDeClasificacion[j]
# --------------------------------------------------------------------------


# FORMATO IMPRESION TABLA CLASIFICACION--------------------------------------
def darFormato(i, posicion):
    return (str(i[1]) + "\t" + str(i[2]) + "\t" + str(i[3]) + "\t" + str(i[4]) + "\t"
            + str(i[5]) + "\t" + str(i[6]) + "\t" + str(i[7]) + "\t" + str(i[8]) + "\t" + str(posicion) + "\t" + i[0])
# --------------------------------------------------------------------------


# TABLA DE CLASIFICACIÓN-----------------------------------------------------
def tablaDeClasificacion(partidos, equipos):
    tablaDeClasificacion = []
    for team in equipos:
        ganadosLocal = 0
        perdidosLocal = 0
        empatadosLocal = 0
        ganadosVisitante = 0
        perdidosVisitante = 0
        empatadosVisitante = 0
        golesAFavor = 0
        golesEnContra = 0
        for i in partidos:
            if i[3] == team:
                if i[6] < i[5]:
                    ganadosLocal = ganadosLocal + 1
                    golesAFavor = golesAFavor + i[5]
                    golesEnContra = golesEnContra + i[6]
                elif i[6] > i[5]:
                    perdidosLocal = perdidosLocal + 1
                    golesAFavor = golesAFavor + i[5]
                    golesEnContra = golesEnContra + i[6]
                elif i[6] == i[5]:
                    empatadosLocal = empatadosLocal + 1
                    golesAFavor = golesAFavor + i[5]
                    golesEnContra = golesEnContra + i[6]
            elif i[4] == team:
                if i[6] > i[5]:
                    ganadosVisitante = ganadosVisitante + 1
                    golesAFavor = golesAFavor + i[6]
                    golesEnContra = golesEnContra + i[6]
                elif i[6] < i[5]:
                    perdidosVisitante = perdidosVisitante + 1
                    golesAFavor = golesAFavor + i[6]
                    golesEnContra = golesEnContra + i[6]
                elif i[6] == i[5]:
                    empatadosVisitante = empatadosVisitante + 1
                    golesAFavor = golesAFavor + i[6]
                    golesEnContra = golesEnContra + i[6]
        ganados = ganadosLocal + ganadosVisitante
        perdidos = perdidosLocal + perdidosVisitante
        empatados = empatadosLocal + empatadosVisitante
        jugados = ganados + perdidos + empatados
        diferenciaDeGoles = golesAFavor - golesEnContra
        puntaje = (ganados * 3) + (empatados * 1)
        tablaDeClasificacion.append([team, puntaje, jugados, ganados, empatados, perdidos,
                                     golesAFavor, golesEnContra, diferenciaDeGoles])
    ordenarTabla(tablaDeClasificacion)
    print("Tabla de Clasificación: ")
    print("Ptj\tPJ\tPG\tPE\tPP\tGF\tGC\tDif\tPos\tEquipo")
    posicion = 1
    for i in tablaDeClasificacion:
        print(darFormato(i, posicion))
        posicion = posicion + 1
    menu()
# --------------------------------------------------------------------------


# MAIN-----------------------------------------------------------------------
if __name__ == '__main__':
    equipos = []
    menu()
