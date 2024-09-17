import pandas as pd
from sodapy import Socrata

def consume(Departamento_usuario, limite):

    #para que muestre todo lo que contiene el dataframe
    pd.set_option('display.max_columns', None) 
    pd.set_option('display.max_rows', None)  

    #aca me meto a la malnacida pagina y le digo que pagina es la pagina a la que acabo de acceder
    pagina = Socrata("www.datos.gov.co", None)

    #ahora hacemos que la basura esta consiga limit registros tipo json y los meta en datos, la cosa verde es la clave a los registros segun yo 
    datos = pagina.get("gt2j-8ykr", where=Departamento_usuario.upper(), limit=limite)

    #pone los datos bien bonitos para no ver nada igual y los devuelve a main para enviarselo a la UI
    return pd.DataFrame.from_records(datos)



lista = [
  "AMAZONAS",
  "ANTIOQUIA",
  "ARAUCA",
  "ATLANTICO",
  "BOLIVAR",
  "BOYACA",
  "CALDAS",
  "CAQUETA",
  "CASANARE",
  "CAUCA",
  "CESAR",
  "CHOCO",
  "CORDOBA",
  "CUNDINAMARCA",
  "GUAINIA",
  "GUAVIARE",
  "HUILA",
  "LA GUAJIRA",
  "MAGDALENA",
  "META",
  "NARIÑO",
  "NORTE DE SANTANDER",
  "PUTUMAYO",
  "QUINDIO",
  "RISARALDA",
  "SAN ANDRAS Y PROVIDENCIA",
  "SANTANDER",
  "SUCRE",
  "TOLIMA",
  "VALLE DEL CAUCA",
  "VAUPES",
  "VICHADA"
]