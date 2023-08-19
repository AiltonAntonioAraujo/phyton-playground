import pandas as pd
#### importa de CSV para DF ###############
df = pd.read_csv("examples/pandas/series/tabela_pbf.csv")

print(df)

####### deletando uma coluna ##############
# axis 1 = coluna; axis 0 = linha
df.drop("Unnamed: 0", axis=1, inplace=True)
print(df)

####### adicionando coluna ###############
df["Parcela Atualizada"] = df["VALOR PARCELA"] + df["VALOR PARCELA"]*0.1
print(df)


##### loc[linha, coluna] ##########
#PRIMEIRA 1000 LINHAS
print(df.loc[0:1000])
#PRIMEIRAS 1000 LINHAS DAS COLUNAS UF, VALOR PARCELA
print(df.loc[0:1000,["UF","VALOR PARCELA"]])
#TODAS AS LINHAS DA COLUNA VALOR PARCELA
print(df.loc[:,"VALOR PARCELA"]) 

#ATUALIZAR O VALOR DA PRIMEIRA LINHA PARA 200
print(df.loc[0,"VALOR PARCELA"])
df.loc[0,"VALOR PARCELA"]=200
print(df.loc[0,"VALOR PARCELA"])

### TODAS AS LINHAS DO ESTADO GO E MUNICIPIO ARENOPOLIS#####
df_go=df.loc[df["UF"]=="GO"]
naz=df_go.loc[df_go["NOME MUNICÍPIO"]=="NAZARIO"]
print(naz)
print(naz["VALOR PARCELA"].sum())

### REMOVER UMA LINHA DO DF ########
naz.drop(4438598, axis=0, inplace=True)

