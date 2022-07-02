#import os    
from os import mkdir 

def create_data_lake():

    """Cree el data lake con sus capas.

    Esta función debe crear la carpeta `data_lake` en la raiz del proyecto. El data lake contiene
    las siguientes subcarpetas:

    ```
    .
    |
    \___ data_lake/
         |___ landing/
         |___ raw/
         |___ cleansed/
         \___ business/
              |___ reports/
              |    |___ figures/
              |___ features/
              |___ forecasts/

    ```


    """
    mkdir("data_lake") 
    mkdir("data_lake/landing") 
    mkdir("data_lake/raw") 
    mkdir("data_lake/cleansed") 
    mkdir("data_lake/business") 
    mkdir("data_lake/business/reports") 
    mkdir("data_lake/business/reports/figures") 
    mkdir("data_lake/business/features") 
    mkdir("data_lake/business/forecasts")


#raise NotImplementedError("Implementar esta función")
if "name" == "main":

    create_data_lake()
    import doctest
    doctest.testmod()
