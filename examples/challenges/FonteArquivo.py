import sys
from FonteDeDados import FonteDeDados
class FonteArquivo(FonteDeDados):
    
    lines = None
    current = None
    higher = None
    reader = None

    def __init__(self, endereco):
        super().__init__(endereco)
        self.current = 0
        self.higher = 0
        try:
            self.reader= open(self.endereco, "r") 
            self.lines = self.reader.read().splitlines()
            self.higher = len(self.lines) -1
        except FileNotFoundError:
            print(f"File {self.endereco} not found.  Aborting")
            sys.exit(1)
        except IOError as e:
            print(f"I/O error({0}): {1}".format(e.errno, e.strerror))
            sys.exit(1)
        except: #handle other exceptions such as attribute errors
            print (f"Unexpected error:", sys.exc_info()[0])
            sys.exit(1)
        
    def proximoDado(self):
        line = self.lines[self.current]
        self.current+=1
        return line
    
    
    def possuiDados(self):
        if(len(self.lines) > 0 and self.current <= self.higher):
                return True
        else:
            return False
      
    def fecharArquivo(self):
        self.reader.close()
        

