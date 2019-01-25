#Autor: Roberto Castro Barrios A01748559
#Problema que calcula el área de un terreno de forma trapezoidal

a= int(input("Ingresa el largo del lado a en metros enteros: "))
b= int(input("Ingresa el largo del lado b en metros enteros: "))
c= int(input("Ingresa el largo del lado c en metros enteros: "))
d= int(input("Ingresa el largo del lado d en metros enteros: "))

p1= (b*d)/2
p2= (b*c)/2
p3= (b*a)-(p1 + p2)
areaTotal= p1 + p2 + p3
print("El área de tu terreno es de: ", areaTotal, " m^2")

