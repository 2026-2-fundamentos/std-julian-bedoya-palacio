import gzip

def pregunta_09():
    """
    Cuente cuántas veces aparece cada clave en la quinta columna (`metrics`)
    de todo el archivo. Retorne un diccionario `{clave: cantidad}` con las
    claves en orden alfabético.

    Ejemplo del formato de la respuesta:

        {"aaa": 13, "bbb": 16, "ccc": 23, ...}
    """
    dic = {}

    with gzip.open("data/data.csv.gz", "rt") as f:
        for line in f:
            registro = line.strip().split("\t")
            metrics = registro[4].split(",")
            for metric in metrics:
                metric=metric[:3]
                if metric not in dic:
                    dic[metric] = 1
                else:
                    dic[metric] += 1

    dic = dict(sorted(dic.items()))

    return dic
