#Sabino
print("Definir situação eleitoral de um usuario")
idade=int(input("Digite a idade do usuario:")) #Valor
if idade>1 or idade<120:
    if idade<16:
        print("Não eleitor") #Final 1
    elif idade>=18 and idade<=65:
        print("eleitor obrigatorio") #final 2
    else:
        print("eleitor facultativo") #final 3
else:
    print("idade invalida") #erro