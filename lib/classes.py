class Rectangulo:
    def __int__(self,largo,ancho):
        self.largo=largo
        self.ancho=ancho
        pass
    def __str__(self):
        return f"Rectangulo de largo {self.largo} y ancho{self.ancho}"
    def area(self): 
        pass
    def perimetro(self):
        return 2*(self.largo+self.ancho)
    
    
    
