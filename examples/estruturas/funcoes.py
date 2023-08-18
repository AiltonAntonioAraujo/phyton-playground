########## funcao que retorna a soma de 2 valores ##########
def soma(a, b):
    resultado = a + b
    return resultado

def soma_multiplica(valor1, valor2, operacao):
    if(operacao =="somar"):
        resultado = valor1+valor2
    if(operacao == "multiplicar"):
        resultado = valor1*valor2
    return resultado


print("Dois valores somados: "+str(soma(4,10)))
print("Dois valores somados: "+str(soma_multiplica(4,10, "somar")))
print("Dois valores multiplicados: "+str(soma_multiplica(4,10, "multiplicar")))



