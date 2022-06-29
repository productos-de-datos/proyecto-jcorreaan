def ingest_data():
    """Ingeste los datos externos a la capa landing del data lake.
    
    Del repositorio jdvelasq/datalabs/precio_bolsa_nacional/xls/ descarge los
    archivos de precios de bolsa nacional en formato xls a la capa landing. La
    descarga debe realizarse usando únicamente funciones de Python.
  
    """
from ast import Try
from distutils.log import Log
import logging
from urllib import request


def ingest_data():
    """Ingeste los datos externos a la capa landing del data lake.
    
    Del repositorio jdvelasq/datalabs/precio_bolsa_nacional/xls/ descarge los
    archivos de precios de bolsa nacional en formato xls a la capa landing. La
    descarga debe realizarse usando únicamente funciones de Python.
    >>> ingest_data()
    """

    import urllib.request
    import datetime
    import logging
    from os import remove

    fecha = datetime.datetime.now()

    total_anios = fecha.year - 1995

    anios = list(range(1995, 1995 + total_anios, 1))

    for anio in anios:
        f = open(f"data_lake/landing/{anio}.xlsx", "wb")
        try:
            f.write(
                request.urlopen(
                    f"https://github.com/jdvelasq/datalabs/raw/master/datasets/precio_bolsa_nacional/xls/{anio}.xlsx"
                ).read()
            )
            f.close()
        except Exception:

            f.close()

            remove(f"data_lake/landing/{anio}.xlsx")

            f = open(f"data_lake/landing/{anio}.xls", "wb")
            f.write(
                request.urlopen(
                    f"https://github.com/jdvelasq/datalabs/raw/master/datasets/precio_bolsa_nacional/xls/{anio}.xls"
                ).read()
            )
            f.close()
        except:
            logging.exception("Error con el archivo: " & anio)


if __name__ == "_main_":
    import doctest

    doctest.testmod()