import pandas as pd

def pregunta_06():
    """
    Usando `data/tbl1.tsv`, obtenga los valores distintos de la columna `c4`,
    conviértalos a mayúsculas y retórnelos como una lista ordenada
    alfabéticamente.

    Ejemplo del formato de la respuesta:

        ["A", "B", "C", "D", "E", "F", "G"]
    """
    df = pd.read_csv("data/tbl1.tsv", sep="\t")
    c4 = df['c4'].str.upper().unique()
    c4_sorted = sorted(c4)

    return c4_sorted


if __name__ == "__main__":
    print(pregunta_06())
