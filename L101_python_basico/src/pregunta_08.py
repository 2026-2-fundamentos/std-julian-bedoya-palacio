import gzip
def pregunta_08():
    """
    Repita la pregunta 7, pero ahora cada lista de letras debe contener cada
    letra una sola vez y estar ordenada alfabéticamente. Retorne una lista de
    tuplas `(valor, letras)` ordenada por el valor.

    Ejemplo del formato de la respuesta:

        [(0, ["C"]), (1, ["B", "E"]), (2, ["A", "E"]), ...]
    """
    dic = {}
    with gzip.open("data/data.csv.gz", "rt") as f:
        for line in f:
            registro = line.strip().split("\t")
            valor = int(registro[1])
            if valor not in dic:
                dic[valor] = set([registro[0]])
            else:
                dic[valor].add(registro[0])
    
    for key in dic:
        dic[key] = sorted(list(dic[key]))

    dic = sorted(dic.items())


    return dic


