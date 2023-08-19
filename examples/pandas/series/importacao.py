#### Importação de dados de CSV ou Excel ###########
import pandas as pd
df = pd.read_csv("examples/pandas/series/pbf2021.csv", encoding = "latin1", sep=";")

#####dados estatíciscos do DataFrame ##########
df.shape

#### tipo de dados de um DF ##############
df.info()

#### corrigir o tipo de dado da coluna Valor Parcela de String para Numerico #####
print(df["VALOR PARCELA"])
df["VALOR PARCELA"]= df["VALOR PARCELA"].apply(lambda x : float(x.replace(",",".")))

df.info()

#print(df)
df.describe()

#### qual foi o maior valor pago em 2021 ########
print(df["VALOR PARCELA"].max())

### exportando paraum arquivo .CSV
df[["UF","NOME MUNICÍPIO","VALOR PARCELA"]].to_csv("examples/pandas/series/tabela_pbf.csv")
