import API.consumeAPI
import UI.mostrarDatos

departamento_usuario = input("Bienvenido al programa de consulta de casos de covid\nIngrese el departamento del que desea consultar los registros: ")
limite = int(input("Ingrese la cantidad de registros que desea consultar: "))

datosPD = API.consumeAPI.consume("departamento_nom='"+departamento_usuario+"'", limite)

UI.mostrarDatos.printf(datosPD)