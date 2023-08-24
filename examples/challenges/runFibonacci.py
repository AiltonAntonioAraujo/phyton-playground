from fibonacci import Fibonacci

numero = int(input("Informe um valor para calculo da Sequencia de Fibonacci:"))

print(f"Imprimindo os valores até a {numero} posição:")
print([Fibonacci.sum(i) for i in range(numero)])
