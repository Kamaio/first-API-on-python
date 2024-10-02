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
    return datosPD



def graficaFallecidos(datosPD):
    fallecidos = datosPD[datosPD['estado'] == 'Fallecido']
    moda_edad = fallecidos['edad'].mode().values[0] if not fallecidos['edad'].empty else None

    fallecidos['edad'].hist(color='blue')
    plt.title('Fallecimientos x edad')
    plt.xlabel('Edad')
    plt.ylabel('Nro.Fallecidos')
    plt.grid(True)
    if moda_edad is not None:
        plt.axvline(moda_edad, color='blue', linestyle='dashed', linewidth=1, label=f'Moda: {moda_edad}')
        plt.legend()
    plt.show()


def graficaCasos(datosPD):
    datosPD['edad'].value_counts().plot(kind='bar')
    plt.xlabel('Edad')
    plt.ylabel('Casos')
    plt.title("Casos x Edad")
    plt.show()

def graficaCircular(datosPD):
    plt.figure(figsize=(10, 6))
    plt.pie(datosPD['ciudad_municipio_nom'].value_counts(), labels=datosPD['ciudad_municipio_nom'].value_counts().index, autopct='%1.1f%%', startangle=140, colors=plt.cm.Paired(range(len(datosPD['ciudad_municipio_nom'].value_counts()))))
    plt.title('Distribución de Casos por Municipio')
    plt.axis('equal')
    plt.show()


def bienvenida():
    departamento_usuario = input("Bienvenido al programa de consulta de casos de covid\nIngrese el departamento del que desea consultar los registros: ")
    limite = int(input("Ingrese la cantidad de registros que desea consultar: "))

    return departamento_usuario, limite