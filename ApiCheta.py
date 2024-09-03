import API.consumeAPI
import UI.mostrarDatos

datosUI = UI.mostrarDatos.bienvenida()
comprobar = 0

while comprobar == 0:
    if(datosUI[1] < 204):
        datosPD = API.consumeAPI.consume("departamento_nom='"+datosUI[0]+"'", datosUI[1])
        UI.mostrarDatos.printf(datosPD)
        comprobar = 1

    else: 
        print("Numero de registros ingresados fuera de rango, ingrese un numero menor o igul a 203")
        datosUI = UI.mostrarDatos.bienvenida()