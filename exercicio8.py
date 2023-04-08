#arthur
import math
print("calculo da hipotenusa de um triangulo retangulo")

cat_op=float(input("digite o cateto oposto: "))
cat_adj=float(input("digite o cateto adjacente: "))

raiz=cat_op**2+cat_adj**2
hip=math.sqrt(raiz)
print("a hipotenusa desse triangulo retangulo é de",hip)