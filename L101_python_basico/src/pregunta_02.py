import gzip

def pregunta_02():
    """
    Cuente cuántos registros hay para cada letra de la primera columna
    (`letter`). Retorne una lista de tuplas `(letra, cantidad)` ordenada
    alfabéticamente por la letra.

    Ejemplo del formato de la respuesta:

        [("A", 8), ("B", 7), ("C", 5), ...]
    """
    with gzip.open("data/data.csv.gz", "rt") as f:
        registros ={}
        for line in f:
            line = line.strip().split("\t")
            letra = line[0]
            if letra not in registros:
                registros[letra] = 1
            else:
                registros[letra] +=1

    registros = sorted(registros.items(), key=lambda x: x[0])
    registros = [(key, value) for key, value in registros]
        

    return registros
