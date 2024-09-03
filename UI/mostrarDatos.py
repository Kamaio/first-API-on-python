import pandas as pd

def printf(datosPD):

    df = pd.DataFrame(datosPD)
    datosFlitr = df[["edad", "departamento_nom", "ciudad_municipio_nom", "fuente_tipo_contagio", "estado"]]
    print(datosFlitr)

def bienvenida():
    departamento_usuario = input("Bienvenido al programa de consulta de casos de covid\nIngrese el departamento del que desea consultar los registros: ")
    limite = int(input("Ingrese la cantidad de registros que desea consultar: "))

    return departamento_usuario, limite