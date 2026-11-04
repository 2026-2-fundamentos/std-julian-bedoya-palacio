import gzip

def pregunta_05():
    """
    Para cada letra de la primera columna (`letter`), encuentre el valor
    máximo y el valor mínimo de la segunda columna (`value`). Retorne una lista
    de tuplas `(letra, máximo, mínimo)` ordenada alfabéticamente por la letra.

    Ejemplo del formato de la respuesta:

        [("A", 9, 2), ("B", 9, 1), ...]
    """
    letras = {}
    with gzip.open("data/data.csv.gz", "rt") as f:
        for line in f:
            registro = line.strip().split("\t")
            letra = registro[0]
            if letra not in letras:
                letras[letra] = [int(registro[1])]
            else:
                letras[letra].append(int(registro[1]))

    for item in letras.items():
        letras[item[0]] = (max(item[1]), min(item[1]))
        
    ordenadas = sorted(letras.items())
    ordenadas = [(item[0], item[1][0], item[1][1]) for item in ordenadas]
    

    return ordenadas
