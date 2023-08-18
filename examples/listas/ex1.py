lista_frutas = ["maça","laranja","uva","pera","banana"]
print("A lista e: "+str(lista_frutas))
print("Fruta na posição 3: "+str(lista_frutas[2]))
print("4 primeiros elementos"+str(lista_frutas[0:4]))

#Adicionando elementos na lista
lista_frutas =lista_frutas+["tangerina"]
lista_frutas.append("tamarindo")

lista_frutas.remove("uva")
del lista_frutas[1]
print("Lista atualizada: "+str(lista_frutas))

print("O tamanho da lista e: "+str(len(lista_frutas)))

print("O a lista ordenada e: "+str(sorted(lista_frutas)))
lista_frutas.reverse()
print("O a lista inversa e: "+str(lista_frutas))


