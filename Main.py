from lib import *

#hw()

"""obj_rect_3= Rectangulo()
obj_rect_3.ancho =75
obj_rect_3.largo =55
print("Ancho: "+str(obj_rect_3.ancho))
print("Largo: "+str(obj_rect_3.largo))
print("perimetro: "+str(obj_rect_3.perimetro())+"[cm]")
print("Area: "+str(obj_rect_3.area())+"[cm^2]")"""
obj_poly_1 = poligono()
obj_poly_1.numlado = 5
obj_poly_1.sizelado = 18
print(obj_poly_1)
print(f"Num lados: {obj_poly_1.numlado}")
print(obj_poly_1.nompoly())
print(obj_poly_1.peripoly())
obj__poly__2 = poligonoregular()
obj__poly__2.numlado = 5
obj__poly__2.sizelado = 15
obj__poly__2.apotema =10 
print(obj__poly__2)
print(obj__poly__2.nompoly())
print(f"El area es : {obj__poly__2.getarea()}")
print(f"El area es mayor a 200?: {obj__poly__2.chkarea()}")
print(obj__poly__2.setcolor("Verde vejiga"))
try:
    sum = 10/0
except ZeroDivisionError:
    print("No puesdes dividir entre cero. . .")
except TypeError:
    print("No puedes dividir strings entre numeros")
except Exception as e:
    print(f"Error desconocido: {e}")
print("Hellow")
