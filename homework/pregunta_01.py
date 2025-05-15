"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta.
"""

# pylint: disable=import-outside-toplevel


def pregunta_01():
    """
    Construya y retorne un dataframe de Pandas a partir del archivo
    'files/input/clusters_report.txt'. Los requierimientos son los siguientes:

    - El dataframe tiene la misma estructura que el archivo original.
    - Los nombres de las columnas deben ser en minusculas, reemplazando los
      espacios por guiones bajos.
    - Las palabras clave deben estar separadas por coma y con un solo
      espacio entre palabra y palabra.


    """

    import re
    import pandas as pd

    with open("files/input/clusters_report.txt", "r") as f:
        contenido = f.readlines()

    inicio = 0
    for idx, linea in enumerate(contenido):
        if "----------" in linea:
            inicio = idx + 1
            break

    cl, cant, porc, claves = [], [], [], []
    i = inicio
    while i < len(contenido):
        if contenido[i].strip():
            m = re.match(r"\s*(\d+)\s+(\d+)\s+([\d,\.]+)\s*%\s*(.*)", contenido[i].strip())
            if m:
                a, b, c, txt = m.groups()
                cl.append(int(a))
                cant.append(int(b))
                porc.append(float(c.replace(",", ".")))
                desc = txt.strip()
                j = i + 1
                while j < len(contenido) and not re.match(r"\s*\d+\s+\d+", contenido[j]) and contenido[j].strip():
                    desc += " " + contenido[j].strip()
                    j += 1
                desc = re.sub(r"\s+", " ", desc)
                desc = re.sub(r"\s*,\s*", ", ", desc)
                if desc.endswith("."):
                    desc = desc[:-1]
                claves.append(desc)
                i = j
            else:
                i += 1
        else:
            i += 1

    return pd.DataFrame({
        "cluster": cl,
        "cantidad_de_palabras_clave": cant,
        "porcentaje_de_palabras_clave": porc,
        "principales_palabras_clave": claves
    })