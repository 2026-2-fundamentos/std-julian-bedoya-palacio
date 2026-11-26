import pandas as pd

def pregunta_02():
    """
    ¿Cuántas columnas tiene la tabla `data/tbl0.tsv`? Retorne la cantidad
    como un número entero.

    Ejemplo del formato de la respuesta:

        4
    """
    df=pd.read_csv("data/tbl0.tsv", sep="\t")
    shape = df.shape

    return shape[1]

if __name__ == "__main__":
    print(pregunta_02())
