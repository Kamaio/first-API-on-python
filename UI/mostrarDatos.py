import pandas as pd

def printf(datosPD):

    df = pd.DataFrame(datosPD)
    datosFlitr = df[["edad", "departamento_nom", "ciudad_municipio_nom", "fuente_tipo_contagio", "estado"]]
    print(datosFlitr)