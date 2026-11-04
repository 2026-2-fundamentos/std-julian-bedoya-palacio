import gzip

def pregunta_07():
    """
    Para cada valor distinto de la segunda columna (`value`), construya la
    lista de letras de la primera columna (`letter`) que aparecen con ese
    valor. Conserve las letras repetidas y el orden en que aparecen en el
    archivo. Retorne una lista de tuplas `(valor, letras)` ordenada por el
    valor.

    Ejemplo del formato de la respuesta:

        [(0, ["C"]), (1, ["E", "B", "E"]), (2, ["A", "E"]), ...]
    """
    dic = {}
    with gzip.open("data/data.csv.gz", "rt") as f:
        for line in f:
            registro = line.strip().split("\t")
            valor = int(registro[1])
            if valor not in dic:
                dic[valor] = [registro[0]]
            else:
                dic[valor].append(registro[0])

    ordenado = sorted(dic.items())


    return ordenado
