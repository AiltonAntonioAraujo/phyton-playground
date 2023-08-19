import pandas as pd

idades = [23,34,56,28]

idades_pd = pd.Series(idades)

print(idades_pd)

### Você pode alterar os indices de uma Series
idades_pd.index = ["roger","luana","jack","lala"]

print(idades_pd)

##### Multiplicado todos os valores da Series #########
# Não altera os dados da Series a estrutura é imutável
print(idades_pd *2)
print(idades_pd / 3)

#filtrando por indice
print(idades_pd[["roger", "lala"]])

#Slice
print(idades_pd[0:2])

#Convertendo todos os elementos para inteiro
idades_pd.apply(int)

#Usando expressão Lambda
idades_pd = idades_pd/3
print(idades_pd.apply(lambda x : str(x).replace(".",",")))