import gzip

def pregunta_04():
    """
    Cuente cuántos registros hay en cada mes, usando la fecha de la tercera
    columna (`date`). Represente el mes como un texto de dos dígitos y retorne
    una lista de tuplas `(mes, cantidad)` ordenada por el mes.

    Ejemplo del formato de la respuesta:

        [("01", 3), ("02", 4), ("03", 2), ...]
    """
    meses = {}
    with gzip.open("data/data.csv.gz", "rt") as f:
        for line in f:
            registro = line.strip().split("\t")
            fecha = registro[2]
            mes = fecha.split("-")[1]
            if mes not in meses:
                meses[mes] = 1
            else:
                meses[mes] +=1

    meses_ordenados = sorted(meses.items())



    return meses_ordenados

