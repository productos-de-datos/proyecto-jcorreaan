import pandas as pd
import numpy as np
#import matplotlib.pyplot as plt
#import statsmodels.api as sm
from sklearn.neural_network import MLPRegressor
import pickle
from joblib import dump, load



def make_forecasts():
    
    """Construya los pronosticos con el modelo entrenado final.
    Cree el archivo data_lake/business/forecasts/precios-diarios.csv. Este
    archivo contiene tres columnas:

    * La fecha.

    * El precio promedio real de la electricidad.

    * El pronóstico del precio promedio real.
    """   
    df = pd.read_csv("./data_lake/business/features/precios_diarios.csv")
    #df=datos.drop(["log_precio"], axis=1)  

    # Pronostico
    # ==============================================================================   
    pickled_model = pickle.load(open('src/models/precios-diarios.pkl', 'rb'))
    df['pronostico'] = pickled_model.predict(np.array(df['log_precio']).reshape(-1, 1))

    df = df.drop(['log_precio'], axis = 1)
  
    # Guardar Modelo
    # ==============================================================================

    df.to_csv('data_lake/business/forecasts/precios-diarios.csv', index=False)
      
    #raise NotImplementedError("Implementar esta función")


if __name__ == "__main__":
    import doctest
    make_forecasts()
    doctest.testmod()