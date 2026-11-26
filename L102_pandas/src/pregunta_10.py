import pandas as pd


def format_c2_values(values):

    sorted_values = sorted(values)

    return ':'.join(str(value) for value in sorted_values)


def pregunta_10():
    """
    Usando `data/tbl0.tsv`, construya para cada categoría de la columna `c1`
    un texto con todos sus valores de la columna `c2`, ordenados de menor a
    mayor y separados por `:`. Retorne un DataFrame cuyo índice son las
    categorías, en orden alfabético, con una única columna llamada `c2`.

    Ejemplo del formato de la respuesta:

                           c2
        c1
        A     1:1:2:3:6:7:8:9
        B       1:3:4:5:6:8:9
        C           0:5:6:7:9
        ...
    """
    df = pd.read_csv("data/tbl0.tsv", sep="\t")
    resultado = df.groupby('c1')['c2'].apply(format_c2_values)

    return resultado.to_frame()

if __name__ == "__main__":
    print(pregunta_10())
