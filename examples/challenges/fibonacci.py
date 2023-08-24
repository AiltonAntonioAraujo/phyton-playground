### Implementação da sequencia de Fibonnaci Recursivo
class Fibonacci():
    def __init__(self):
        pass

    @staticmethod    
    def sum(numero):
        if(numero == 0 or numero == 1):
            return numero
        else:
            return Fibonacci.sum(numero-1) + Fibonacci.sum(numero -2)
        
        
        
    
