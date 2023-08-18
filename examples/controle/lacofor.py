numero = 2

for i in [5,9,6]:
    numero = int(input("Digite um numero inteiro: "))
    if(numero % 2 == 0):
        print("O numero "+str(numero)+" é par")
    else:
        print("O numero "+str(numero)+" é impar")
    print("O valor de i é: "+str(i))

