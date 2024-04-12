def line():
import math

a=float(input("Ingrese el coeficiente A:"))
b=float (input("Ingrese el coeficiente B:"))
x1=float(input("Ingrese el coeficiente X1:"))
x2=float(input("Ingrese el coeficiente X2:")) 
print(f"El coeficiente A de su ecuación de la recta es: {a}")
print(f"El coeficiente B de su ecuación de la recta es: {b}")
print(f"El coeficiente X1 de su ecuación de la recta es: {x1}")
print(f"El coeficiente X2 de su ecuación de la recta es: {x2}")
print (f"\nPara la siguiente ecuacion:")
print(f"\tY={a}*X + {b}")
resulx1=a*x1+b
resulx2=a*x2+b

print(f"\nDados los siguientes puntos:")
print(f"\tP1 ({x1},{resulx1})")
print(f"\tP2 ({x2},{resulx2})")
difx=math.pow(x1-x2, 2)
dify=math.pow(resulx1-resulx2, 2)
ecdist=math.sqrt(difx+dify)
print(f"\nLa distancia entre ellos es:{ecdist}")
