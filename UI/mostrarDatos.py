import pandas as pd
from tabulate import tabulate as tabla
import numpy as np
import matplotlib.pyplot as plt

def printf(datosPD):

    df = pd.DataFrame(datosPD)
    pd.set_option('display.max_rows', None)
    pd.set_option('display.max_columns', None)
    datosFlitr = df[["edad", "departamento_nom", "ciudad_municipio_nom", "fuente_tipo_contagio", "estado"]]
    print(tabla(datosFlitr, headers=('EDAD', 'DEPARTAMENTO', 'CIUDAD', 'TIPO', 'ESTADO'), tablefmt='github', showindex=True))
    
    
    print("Numero de Filas: ", datosFlitr.shape[0])
    print("Numero de columnas: ", datosFlitr.shape[1])
    print("Nombre columnas: ", datosFlitr.columns.values.tolist())
    print("\nTipo de datos columnas:\n", datosFlitr.dtypes)
    datosFlitr.replace("N/A", np.nan, inplace=True)
    print("\nColumnas con datos faltantes: ",datosFlitr.columns[datosFlitr.isnull().any()].tolist())
    print("\nIndices con datos faltantes: ", datosFlitr[datosFlitr.isnull().any(axis=1)].index.tolist())
    print("\n\nEstadisticas generales:\n")
    print(datosFlitr.info())
    print("\nResumen de estadisticas:\n" )
    print(datosFlitr.describe())
    datosFlitr = datosFlitr.dropna(subset=["edad", "departamento_nom", "ciudad_municipio_nom", "fuente_tipo_contagio", "estado"])
    print("Datos limpios: \n", tabla(datosFlitr, headers=('EDAD', 'DEPARTAMENTO', 'CIUDAD', 'TIPO', 'ESTADO'), tablefmt='github', showindex=True))


def graficas(datosPD):
    datosPD['edad'].value_counts().plot(kind='bar')
    plt.xlabel('edad')
    plt.ylabel('Numero de casos')
    plt.title('Edad x Nro.Casos')
    plt.show()


def bienvenida():
    departamento_usuario = input("Bienvenido al programa de consulta de casos de covid\nIngrese el departamento del que desea consultar los registros: ")
    limite = int(input("Ingrese la cantidad de registros que desea consultar: "))

    return departamento_usuario, limite