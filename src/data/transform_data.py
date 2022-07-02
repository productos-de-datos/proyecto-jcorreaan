import pandas as pd

def transform_data():
    """Transforme los archivos xls a csv.
    Transforme los archivos data_lake/landing/*.xls a data_lake/raw/*.csv. Hay
    un archivo CSV por cada archivo XLS en la capa landing. Cada archivo CSV
    tiene como columnas la fecha en formato YYYY-MM-DD y las horas H00, ...,
    H23.
    """

def data_csv(anio, header, extension):
    read_file = pd.read_excel("data_lake/landing/{}.{}".format(anio, extension), header=header)
    read_file = read_file.iloc[:, 0:25]
    read_file.columns ==['Fecha', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '10','11', '12', '13', '14', '15', '16', '17', '18', '19', '20', '21', '22', '23']       
    read_file.to_csv("data_lake/raw/{}.csv".format(anio), index=None)
    return    

for anio in range(1995, 2022):
    if anio in range(1995, 2000):
        data_csv(anio, 3, "xlsx")
    elif anio in range(2000, 2016):
        data_csv(anio, 2, "xlsx")
    elif anio in range(2016, 2018):
        data_csv(anio, 2, "xls")
    else:
        data_csv(anio, 0, "xlsx")
    
# raise NotImplementedError("Implementar esta función")


if __name__ == "__main__":
    import doctest
    doctest.testmod()
    transform_data()