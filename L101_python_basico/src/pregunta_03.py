import gzip

def pregunta_03():
    """
    Sume los valores de la segunda columna (`value`) para cada letra de la
    primera columna (`letter`). Retorne una lista de tuplas `(letra, suma)`
    ordenada alfabéticamente por la letra.

    Ejemplo del formato de la respuesta:

        [("A", 53), ("B", 36), ("C", 27), ...]
    """
    sumas = {}
    with gzip.open("data/data.csv.gz", "rt") as f:
        for line in f:
            line = line.strip().split("\t")
            if line[0] not in sumas:
                sumas[line[0]] = int(line[1])
            else:
                sumas[line[0]] += int(line[1])

    sumas= sorted(sumas.items(), key=lambda x:x[0])

    sumas = [(key, value) for key, value in sumas]
    return sumas


