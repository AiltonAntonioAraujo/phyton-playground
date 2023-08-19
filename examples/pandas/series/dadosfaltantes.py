import pandas as pd

notas = pd.read_excel("examples/pandas/series/estudantes.xlsx")

print(notas)
print(notas.isnull().sum())
#### retirnado todos os que estão faltando NaN
print(notas.dropna())

#### pode substituir o valor, por Zero
print(notas.fillna(0, inplace=True))

### subistituir valores
notas["Matemática"] = notas["Matemática"].fillna(notas["Matemática"].mean())
print (notas)
