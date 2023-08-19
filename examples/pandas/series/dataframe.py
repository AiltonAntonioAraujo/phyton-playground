#Dataframes - dados tabulares
#É uma estrutura mais robusta que Series
#Bidimensional - linha, coluna
#Eixos rotulados
#Dados heterogêneos
#Manipulação de dados faltantes
#Agrupamento
#Fusão
#Estatísticas
import pandas as pd
import numpy as np 

dados = {
    "nome":["Roger", "Jack","Luana","Lavinia"],
    "idade":[25,56,37,2],
    "cidade":["Marabá","Palmas","Palmas","Marabá"]
}

df = pd.DataFrame(dados)

print(df)

######## Array NumPy ##############
array = np.array([[1,2,3],[4,5,6],[7,8,9]])
print(array)

df = pd.DataFrame(array, columns=["A","B","C"])
print(df)

