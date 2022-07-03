import pandas as pd
import numpy as np
#import matplotlib.pyplot as plt
#import statsmodels.api as sm
from sklearn.neural_network import MLPRegressor
import pickle
from joblib import dump, load

def train_daily_model():
    """Entrena el modelo de pronóstico de precios diarios.

    Con las features entrene el modelo de proóstico de precios diarios y
    salvelo en models/precios-diarios.pkl


    """

    df = pd.read_csv("./data_lake/business/features/precios_diarios.csv")
    #df=datos.drop(["log_precio"], axis=1)  

    # Preparación del dato
    # ==============================================================================   
        
    X = df.iloc[:, -1]
    X = np.array(X).reshape(-1, 1)
    y = df.iloc[:, 2]

    # Modelo
    # ==============================================================================   
    H=1
    modelo = MLPRegressor(
        hidden_layer_sizes=(H,),
        activation="logistic",
        learning_rate="adaptive",
        momentum=0.0,
        learning_rate_init=0.1,
        max_iter=10000,
        )

    modelo.fit(X, y)  

    # Guardar Modelo
    # ==============================================================================
    
   
    #path_parent_dir = os.path.join(os.getcwd(), "src/models")
    #joblib.dump(modelo, path_parent_dir + '/precios-diarios.pkl')

    pickle.dump(modelo, open('src/models/precios-diarios.pkl', 'wb'))  

         
    #raise NotImplementedError("Implementar esta función")


if __name__ == "__main__":
    import doctest
    train_daily_model()
    doctest.testmod()