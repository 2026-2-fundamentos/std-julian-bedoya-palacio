import gzip

def pregunta_11():
    """
    La cuarta columna (`codes`) contiene letras minúsculas separadas por
    comas. Para cada una de esas letras, sume los valores de la segunda
    columna (`value`) de los registros en los que aparece. Retorne un
    diccionario `{letra: suma}` con las letras en orden alfabético.

    Ejemplo del formato de la respuesta:

        {"a": 122, "b": 49, "c": 91, ...}
    """
    dic={}
    with gzip.open("data/data.csv.gz", "rt") as f:
        for line in f:
            registro = line.strip().split("\t")
            valor = int(registro[1])
            letras = registro[3].split(",")
            for letra in letras:
                if letra in dic:
                    dic[letra] += valor
                else:
                    dic[letra] = valor

    ordenado = dict(sorted(dic.items()))


    return ordenado

