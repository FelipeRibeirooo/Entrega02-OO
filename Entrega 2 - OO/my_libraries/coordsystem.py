from my_libraries.shapes2D import *

class PlanoCartesiano():
    
    def __init__(self):
        self.shapes= []
        
        
    def InserirFormas(self,*shape):
        for i in shape:
            self.shapes.append(i)
        
        
    def RemoverFormas(self,*shape):
        for i in shape:
            self.shapes.remove(i)
        
        
    def MostrarFormas(self):
        print('Este plano cartesiano possui as formas:\n')
        for shape in self.shapes:
            print(shape)
    
    def QuantidadeDeFormas(self):
        print(f"O plano cartesiano possui {len(self.shapes)} formas geométricas")