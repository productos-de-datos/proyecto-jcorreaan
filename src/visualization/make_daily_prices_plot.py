
import pandas as pd
import matplotlib.pyplot as plt

def make_daily_prices_plot():
    """Crea un grafico de lines que representa los precios promedios diarios.
    Usando el archivo data_lake/business/precios-diarios.csv, crea un grafico de
    lines que representa los precios promedios diarios.
    El archivo se debe salvar en formato PNG en data_lake/business/reports/figures/daily_prices.png.
    """
    

    #df_daily_prices = pd.read_csv("./data_lake/business/precios-diarios.csv")
    df = pd.read_csv("precios-diarios.csv", index_col=None, header=0)
    df['fecha'] = pd.to_datetime(df['fecha'])
    #plot = df['precio'].plot(figsize=(10, 8))
    x = df['fecha']
    y = df['precio']

    plt.figure(figsize=(12, 8)) 
    plt.plot(x, y, label='Promedio Diario') 
    #plt.savefig("daily_prices.png") 
    plt.savefig(./data_lake/business/reports/figures/daily_prices.png") 
    
if __name__ == "__main__":
    import doctest
    make_daily_prices_plot()
    doctest.testmod()
