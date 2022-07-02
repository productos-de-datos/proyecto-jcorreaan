import pandas as pd

def compute_daily_prices():
    """Compute los precios promedios diarios.
    Usando el archivo data_lake/cleansed/precios-horarios.csv, compute el prcio
    promedio diario (sobre las 24 horas del dia) para cada uno de los dias. Las
    columnas del archivo data_lake/business/precios-diarios.csv son:
    * fecha: fecha en formato YYYY-MM-DD
    * precio: precio promedio diario de la electricidad en la bolsa nacional
    """

    df = pd.read_csv("data_lake/cleansed/precios-horarios.csv", index_col=None, header=0)
    df = df[["fecha", "precio"]]
    df['fecha'] =pd.to_datetime(df['fecha'], format='%Y-%m-%d')
    anios_mes_agrupada = df.groupby('fecha').mean({"precio": "precio"}).reset_index()
    #anios_mes_agrupada
    anios_mes_agrupada.to_csv("data_lake/business/precios-diarios.csv", index=None, header=True)
    
    #route_try = True
    #try:
    #    anios_mes_agrupada = pd.read_csv("./data_lake/cleansed/precios-horarios.csv")
    #except FileNotFoundError:
    # route_try = False
    #route = "data_lake/business/precios-diarios.csv" if route_try else "../../data_lake/business/precios-diarios.csv"
        #anios_mes_agrupada .to_csv(route, index=False)    
    #anios_mes_agrupada= pd.read_csv("../../data_lake/cleansed/precios-horarios.csv")



# raise NotImplementedError("Implementar esta función")

if __name__ == "__main__":

    import doctest
    compute_daily_prices()   
    doctest.testmod()
     