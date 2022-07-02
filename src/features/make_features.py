import pandas as pd
import numpy as np
    
def make_features():
    """Prepara datos para pronóstico.

    Cree el archivo data_lake/business/features/precios-diarios.csv. Este
    archivo contiene la información para pronosticar los precios diarios de la
    electricidad con base en los precios de los días pasados. Las columnas
    correspoden a las variables explicativas del modelo, y debe incluir,
    adicionalmente, la fecha del precio que se desea pronosticar y el precio
    que se desea pronosticar (variable dependiente).

    En la carpeta notebooks/ cree los notebooks de jupyter necesarios para
    analizar y determinar las variables explicativas del modelo.

    """

    #df = pd.read_csv("precios-diarios_2.csv", index_col=None, header=0)
    df = pd.read_csv("./data_lake/business/precios-diarios.csv")
    df['log_precio'] =np.log(df['precio'])


    df.to_csv('precios-diarios_fe.csv', index=False)

    #return

    #raise NotImplementedError("Implementar esta función")



if __name__ == "__main__":
    import doctest
    make_features()
    doctest.testmod()
