
import pandas as pd
import glob

def clean_data():
    """Realice la limpieza y transformación de los archivos CSV.
    Usando los archivos data_lake/raw/*.csv, cree el archivo data_lake/cleansed/precios-horarios.csv.
    Las columnas de este archivo son:
    * fecha: fecha en formato YYYY-MM-DD
    * hora: hora en formato HH
    * precio: precio de la electricidad en la bolsa nacional
    Este archivo contiene toda la información del 1997 a 2021.
    """    

    path_file = glob.glob(r"data_lake/raw/*.csv")
    archivos = []

for filename in path_file:
    df = pd.read_csv(filename, index_col=None, header=0)
    archivos.append(df)
    file = pd.concat(archivos, axis=0, ignore_index=True)
    file = file[file['Fecha'].notnull()]

    anios = file.iloc[:, 0]
    #file

    data_1 = pd.melt(file, id_vars=['Fecha'])
    data_2 = data_1.rename(columns={'Fecha': 'fecha', 'variable': 'hora', 'value': 'precio'})
    data_3 = data_2[data_2["precio"].notnull()]
    data_3.to_csv("data_lake/cleansed/precios-horarios.csv", index=None, header=True)


# raise NotImplementedError("Implementar esta función")


if __name__ == "__main__":

    import doctest
    clean_data()
    doctest.testmod()