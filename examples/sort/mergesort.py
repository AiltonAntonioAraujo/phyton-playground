class MergeSort():
   
    def __init__(self):
        pass

    def sortArrayWithMergeSort(self, array, begin, end):

        if( begin < end):
            # Divide para conquistar
            middle = self.getMiddleElement(begin, end)
            # Divide lado direito recursivamente
            self.sortArrayWithMergeSort(array, begin, middle)
            # Divide lado esquerdo recursivamente
            self.sortArrayWithMergeSort(array, middle +1, end)

            # Faz a juncao de forma ordenada
            self.merge(array,  begin, end, middle)
            
        
    def merge(self, array, begin, end, middle):
        i= begin
        j= middle + 1
        k = begin
        aux = array[:]

        # realiza a juncao dos array direito e esquerdo
        while( i <= middle and j <= end ):
            if(aux[i] < aux[j]):
                array[k] = aux[i]
                i+=1
            else:
                array[k] = aux[j]
                j+=1

            k+=1
        
        # adiciona o elemento menor a direita do array esquerdo    
        while (i <= middle):
            array[k] = aux[i]
            i+=1
            k+=1

        # adiciona o elemento menor a direita do array direito
        while (j <= end):
            array[k] = aux[j]
            j+=1
            k+=1
    
    
    def sortArray(self,array):
        self.sortArrayWithMergeSort(array, 0, len(array)-1)

    def getMiddleElement(self,begin, end):
        return int((begin+end)//2)
