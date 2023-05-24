#Sabino
print("Definir se o usuario possui obsedidade")
peso=float(input("Digite seu peso em kg:")) #peso em kg
if peso>=0.4 and peso<=300:
    altura=float(input("<Digite a altura do usuario em metros:"))#altura em metros
    if altura>=0.4 and altura<=3:
        massa=peso/(altura*altura) #valor da massa
        if massa<=26:
            print("<Massa ideal>")#Resultado 1
        elif massa<=30:
            print("<Obeso>")#Resultado 2
        else:
            print("<Obsedidade morbida>") #Resultado 3
    else:
        print("<Altura invalida>") #erro
else:
    print("<Peso invalido>") #erro