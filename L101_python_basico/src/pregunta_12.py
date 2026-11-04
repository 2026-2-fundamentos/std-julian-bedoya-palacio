import gzip

def pregunta_12():
    """
    Para cada letra de la primera columna (`letter`), sume todos los valores
    numéricos de los pares `clave:valor` de la quinta columna (`metrics`).
    Retorne un diccionario `{letra: suma}` con las letras en orden alfabético.

    Ejemplo del formato de la respuesta:

        {"A": 177, "B": 187, "C": 114, ...}
    """
    dic={}
    with gzip.open("data/data.csv.gz", "rt") as f:
        for line in f:
            registro = line.strip().split("\t")
            letra = registro[0]
            metrics = registro[4].split(",")
            suma = sum(int(metric.split(":")[1]) for metric in metrics)
            if letra in dic:
                dic[letra] += suma
            else:
                dic[letra] = suma

    ordenado = dict(sorted(dic.items()))

    return ordenado
