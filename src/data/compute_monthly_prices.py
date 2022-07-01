def compute_monthly_prices():
    """Compute los precios promedios mensuales.

    Usando el archivo data_lake/cleansed/precios-horarios.csv, compute el prcio
    promedio mensual. Las
    columnas del archivo data_lake/business/precios-mensuales.csv son:

    * fecha: fecha en formato YYYY-MM-DD

    * precio: precio promedio mensual de la electricidad en la bolsa nacional



    """
import pandas as pd
df = pd.read_csv("data_lake/cleansed/precios-horarios.csv", index_col=None, header=0)
df = df[["fecha", "precio"]]
df['fecha'] =pd.to_datetime(df['fecha'], format='%Y-%m-%d')
anios_mes_agrupada=df.groupby(df['fecha'].dt.to_period('M'))[ 'precio'].mean().reset_index()
#anios_mes_agrupada.head(4)
anios_mes_agrupada['fecha'] =pd.to_datetime(anios_mes_agrupada["fecha"].astype(str), format='%Y-%m-%d')
anios_mes_agrupada.to_csv('data_lake/business/precios-mensuales.csv', index=None)
    
    # raise NotImplementedError("Implementar esta función")


if __name__ == "__main__":

    import doctest

    doctest.testmod()
    compute_monthly_prices()    