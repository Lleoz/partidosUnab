partidos=[]
import math
#MENU---------------------------------------------------------------------
def menu():
    print("Bienvenido al menú de partidos del equipo de futbol del torneo")
    print("¿Qué desea realizar?")
    print("1. Registrar equipos")
    print("2. Registrar partido")
    print("3. Estadisticas del torneo:")
    print("4. Salir")
    opc = int(input("digite su opción: "))
    if opc == 1:
        registrar_equipos(equipos)
    elif opc== 2:
        registrar_partido(partidos)
    elif opc == 3:
        estadisticas(partidos)
    elif opc ==4:
        print("Adiós")
        exit()
    else:
        print("Opción no valida")
        menu()
#--------------------------------------------------------------------------





#REGISTRAR EQUIPOS---------------------------------------------------------
def registrar_equipos(equipos):
    print("Ingrese el numero de equipos que quiere registrar")
    nom = int(input())
    print("ingrese el nombre de los equipos que desee inscribir")
    for i in range(nom):
        z = input()
        equipos.append(z)
        print(equipos)
    menu()
#--------------------------------------------------------------------------





#VALIDAR GOLES-------------------------------------------------------------
def validar_goles(goles):
    while(goles < 0):
        print("Ingrese una cantidad de goles mayor o igual a 0: ")
        goles = int(input())
    return goles
#--------------------------------------------------------------------------




#FECHAS--------------------------------------------------------------------
def definir_fecha():
    print("vamos a registrar la fecha")
    anio = int(input("Ingrese el año en formato AAAA: "))
    while(anio < 0 or anio > 2021):
        anio = int(input("Año incorrecto, ingrese el año en formato AAAA: "))
    mes = int(input("Ingrese el mes en formato MM: "))
    while(mes <= 0 or mes > 12):
        mes = int(input("Mes incorrecto, ingrese el mes en formato MM: "))
    dia = int(input("Ingrese el dia en formato DD: "))
    if(mes == 2):
        while(dia <= 0 or dia > 28):
            dia = int(input("dia erroneo, ingrese el dia en formato DD: "))
    if(mes == 1 or mes == 3 or mes == 5 or mes == 7 or mes == 8 or mes == 10 or mes == 12):
        while(dia <= 0 or dia > 31):
            dia = int(input("dia erroneo, ingrese el dia en formato DD: "))
    if(mes == 4 or mes == 6 or mes == 9 or mes == 11):
        while(dia <= 0 or dia > 31):
            dia = int(input("dia erroneo, ingrese el dia en formato DD: "))
    return dia, mes, anio
#--------------------------------------------------------------------------





#REGISTRAR PARTIDOS--------------------------------------------------------
def registrar_partido(partidos):
    print("Vamos a registrar un partido")
    try:
        dia, mes, anio = definir_fecha()
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
        print("ingrese la cantidad de goles hechos por el equipo local: ")
        goles_visitante = int(input())
        goles_visitante = validar_goles(goles_visitante)
        print("ingrese la cantidad de goles hechos por el equipo visitante: ")
        goles_local = int(input())
        goles_local= validar_goles(goles_local)
        partidos.append([dia, mes, anio,nombre_local, nombre_rival, goles_local, goles_visitante])
        print(partidos)
        print("¿Desea ingresar otro partido?")
        cond = str(input("S/N"))
    except:
        print("Alguno de los datos estan mal registrado, intente de nuevo")
        registrar_partido(partidos)
    if(cond == "S" or cond == "s"):
        registrar_partido(partidos)
    menu()
#--------------------------------------------------------------------------





#ESTADISTICAs---------------------------------------------------------------
def estadisticas(partidos):
    suma_local=0
    suma_visitante=0
    suma_total=0
    cuenta=0
    promedio1=0
    promedio2=0
    part=0
    par_jug = len(partidos)
    print("Seleccione el tipo de dato que desee consultar")
    print("1. Estadísticas del torneo")
    print("2. Estadísticas por equipos")
    print("3. Regresar al menú principal")
    opc2=int(input())
    if opc2==1:
        print("1. Media de goles por partido")
        print("2. Desviación estandar por goles")
        print("3. Regresar al menú anterior")
        opc3=int(input())
        if opc3==1:
            for i in partidos:
                suma_total = suma_total+i[6]+i[5]
            promedio = suma_total/par_jug
            print("La media de goles por partidos es: "+str(promedio))
            estadisticas(partidos)
        elif opc3==2:
            for i in partidos:
                suma_total=suma_total+i[6]+i[5]
            promedio=suma_total/par_jug
            for i in partidos:
                stdr=(i[6]+i[5]-promedio)**2
                cuenta=stdr+cuenta
            devs=math.sqrt(cuenta/par_jug)
            print("La desviacion de los goles por partido en el torneo es: "+str(devs))
            estadisticas(partidos)
        elif opc3==3:
            estadisticas(partidos)
        else:
            estadisticas(partidos)
    #ACA EMPIEZA LA ESTADISTICA POR EQUIPOS        
    elif opc2==2:
        pass
    elif opc2==3:
        menu()
    else:
        print("Opción inexistente")
        estadisticas(partidos)
    print("Seleccione al equipo que quiera consultar")
    team=str(input())
    if (team) in equipos:
        pass
    else:
        print("El equipo marcado no se encuentra registrado")
        menu()
    for i in partidos:
        if i[3]==team:
            part=part+1
        if i[4]==team:
            part=part+1
    print(part)
    print("Qué desea consultar?")
    print("1. Goles anotados por partido")
    print("2. Goles recibidos por partido")
    print("3. Promedio de goles anotados y desviación estándar")
    print("4. Promedio de goles recibidos y desviación estándar")
    opc4=int(input())
    if opc4==1:
        for i in partidos:
            if i[3]==team:
                suma_local=suma_local+i[6]
            if i[4]==team:
                suma_visitante=suma_visitante+i[5]
        puntos= suma_visitante+suma_local
        print("Los goles totales del equipo "+ team+" " + str(puntos))
    elif opc4==2:
        for i in partidos:
            if i[3]==team:
                suma_local=suma_local+i[5]
            if i[4]==team:
                suma_visitante=suma_visitante+i[6]
        puntos= suma_visitante+suma_local
        print("Los goles recibidos por el equipo "+ team+"son: " + str(puntos))
    elif opc4==3:
        for i in partidos:
            if i[3] == team:
                suma_local = suma_local + i[6]
            promedio1=suma_local
            if i[4] == team:
                suma_visitante = suma_visitante + i[5]
            promedio2=suma_visitante
        media1=(promedio1+promedio2)/part
        print("La media de goles anotados por partido del equipo "+ str(team)+"es: "+ str(media1))
        puntos = suma_visitante + suma_local
        for i in partidos:
            if i[3]==team:
                stdr=(i[6]-puntos)**2
                cuenta=stdr+cuenta
            if i[4]==team:
                stdr=(i[5]-puntos)**2
                cuenta=stdr+cuenta
            devs=math.sqrt(cuenta/part)
            print("La desviación estandar por partidos para el equipo: "+ str(team)+"es: "+ str(devs))
        estadisticas(partidos)
    elif opc4==4:
        for i in partidos:
            if i[3] == team:
                suma_local = suma_local + i[5]
            promedio1=suma_local
            if i[4] == team:
                suma_visitante = suma_visitante + i[6]
            promedio2=suma_visitante
        media1=(promedio1+promedio2)/part
        print("La media de goles recibidos por partido del equipo "+ str(team) +"es: "+ str(media1))
        puntos = suma_visitante + suma_local
        for i in partidos:
            if i[3]==team:
                stdr=(i[5]-puntos)**2
                cuenta=stdr+cuenta
            if i[4]==team:
                stdr=(i[6]-puntos)**2
                cuenta=stdr+cuenta
            devs=math.sqrt(cuenta/part)
            print("La desviación estandar por partidos para el equipo: "+ str(team) +"es: "+ str(devs))
        estadisticas(partidos)
    elif opc4==5:
        ganados=0
        perdidos=0
        empatados=0
        for i in partidos:
            if i[3]==team:
                if i[6]<i[5]:
                    ganados=ganados+1
                elif i[6]>i[5]:
                    perdidos=perdidos+1
                elif i[6]==i[5]:
                    empatados=empatados+1
                print("Partidos ganados: "+ str(ganados))
                print("Partidos perdidos: "+ str(perdidos))
                print("Partidos empatados: "+str(empatados)) 
                menu()
    else:
        print("seleccion no válida")
        estadisticas(partidos)

#--------------------------------------------------------------------------






if __name__ == '__main__':
    equipos = []
    menu()
