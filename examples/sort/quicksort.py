#Algoritmo de ordenação de um array de Chars

# Classe que implementa o algoritmo de chamada
# recursiva para ordenação através de divisão para 
# conquista
class quickSort():
    def __init__(self):
        pass
    #Método de chamada recursiva
    #para ordenação de um array de Chars
    def quickSort(self, arr, begin, end):
        if( begin < end):
            pivot = self.partition(arr, begin, end)
            self.quickSort(arr, begin, pivot - 1)
            self.quickSort(arr, pivot + 1, end)
    
    #Método de partição de um array
    def partition(self, arr, begin, end):
        pivot = arr[begin]
        i = begin+1
        j = end
        while ( i <= j):
            while( i <= j and arr[i] <= pivot):
                i+=1
            while( j >= i and arr[j] > pivot):
                j-=1
            if(i < j):
                self.change(arr, j, i)
                i+=1
                j-=1
                
        self.change(arr, begin, j)
        return j
    
    #Método que altera a posição com pivot 
    #com a nova posição de parada do indice
    def change(self, arr, left, right):
        aux = arr[left]
        arr[left] = arr[right]
        arr[right] =  aux
    
    #Método de execução do método de ordenação
    #passando selecionando o pivot como a 
    #primeira posição do array a ser ordenado
    def sortWithQS(self, arr):
        self.quickSort(arr, 0, len(arr) -1)
        


################ Programa ordena um array especificado #############
#array especificado
arr = ['B','C','E','D','A']

#ordenando array com QuickSort (QS)
qs = quickSort()

#exibindo o array em ordem alfabética
qs.sortWithQS(arr)
print(arr)















