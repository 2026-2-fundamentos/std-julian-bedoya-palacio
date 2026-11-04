import gzip

def pregunta_01():
    """
    Calcule la suma de los valores de la segunda columna (`value`) del
    archivo `data/data.csv.gz` y retorne el resultado como un número entero.

    Ejemplo del formato de la respuesta:

        214
    """
    sumacolumna = 0
    with gzip.open("data/data.csv.gz", "rt") as f:
        for line in f:
            line = line.strip().split("\t")
            sumacolumna += int(line[1])
            

    return sumacolumna

