class poligono:
    def __int__(self, numlado,sizelado):
        self.numlado = numlado
        self.sizelado = sizelado
        pass
    def __str__(self):
        return f"Numero de lados: {self.numlado} y tamaño del lado: {self.sizelado}"
    def nompoly(self):
        match self.numlado:
            case 3:
                return " Tu poligono es un triangulo "
            case 4:
                return"Tu poligono es un cuadrado"
            case 5:
                return"Tu poligono es un pentagono"
            case 6:
                return"Tu poligono es un hexagono"
            case 7:
                return"Tu poligono es un eptangono"
            case 8:
                return"Tu poligono es un octagono"
            case 9:
                return"Tu poligono es un eneágono"
            case 10:
                return"Tu poligono es un decágono"

            case _:
                return"Tu poligono no loidentifica"
    def peripoly (self):
        return(self.numlado + self.sizelado)
class poligonoregular:
    def __int__(self):
        pass
class poligonoregular( poligono):
    
    def __int__(self, numlado, sizelado, apotema):
        super().__int__(numlado, sizelado)  
        self.apotema = apotema
        pass
    def __str__(self):
        return f"numlado:{self.numlado},sizelado:{self.sizelado}, apotema:{self.apotema}"
