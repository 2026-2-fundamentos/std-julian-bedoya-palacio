import gzip

def pregunta_06():
    """
    La quinta columna (`metrics`) contiene pares `clave:valor` separados por
    comas. Para cada clave, encuentre el valor mínimo y el valor máximo que
    aparecen en todo el archivo. Retorne una lista de tuplas
    `(clave, mínimo, máximo)` ordenada alfabéticamente por la clave.

    Observe que el orden es mínimo y luego máximo, al contrario de la
    pregunta 5.

    Ejemplo del formato de la respuesta:

        [("aaa", 1, 9), ("bbb", 1, 9), ...]
    """

    with gzip.open("data/data.csv.gz", "rt") as f:
        metrics_dict = {}
        for line in f:
            registro = line.strip().split("\t")
            metrics = registro[4].split(",")
            for metric in metrics:
                clave, valor = metric.split(":")
                valor = int(valor)
                if clave not in metrics_dict:
                    metrics_dict[clave] = [valor]
                else:
                    metrics_dict[clave].append(valor)

    for item in metrics_dict.items():
        metrics_dict[item[0]] = (min(item[1]), max(item[1]))

    ordenadas = sorted(metrics_dict.items())
    ordenadas = [(item[0], item[1][0], item[1][1]) for item in ordenadas]

    return ordenadas

