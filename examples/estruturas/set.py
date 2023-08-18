########## Set são estruturas que não se repetem ############
frutas_set = {"maça", "banana", "morango"}

print(type(frutas_set))
print("Dados de frutas: "+str(frutas_set))

######### a fruta duplicada é ignorada #######################
frutas_set.add("maça")
print("Dados de frutas: "+str(frutas_set))