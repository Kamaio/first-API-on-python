import API.consumeAPI
import UI.mostrarDatos

datosUI = UI.mostrarDatos.bienvenida()
comprobar = 0
revisar = 0

while comprobar == 0:
    if datosUI[0].upper() in API.consumeAPI.lista:
        if(datosUI[1] < 204):
            datosPD = API.consumeAPI.consume("departamento_nom='"+datosUI[0]+"'", datosUI[1])
            UI.mostrarDatos.printf(datosPD)
            comprobar = 1

        else: 
            print("\nNumero de registros ingresados fuera de rango, ingrese un numero menor o igual a 203")
            datosUI = UI.mostrarDatos.bienvenida()
        
    else: 
        print("\nEl departamento introducido no existe, ingrese un departamento valido")
        datosUI = UI.mostrarDatos.bienvenida()