####### Dicionário são estruturas Chave-Valor #########

pessoa = {"nome":"Ailton", "idade":40}

print(type(pessoa))

print("Dados de uma pessoa"+str(pessoa))

print("Nome da pessoa: "+str(pessoa["nome"]))
print(str(pessoa.keys()))
print(str(pessoa.items()))
print(str(pessoa.values()))

pessoa["peso"] = 85
print("Dados de uma pessoa"+str(pessoa))

