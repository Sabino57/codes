#Sabino
print("Definir situação de uma media definida pelo o usuario")
media=int(input("Digite a media:")) #Valor
if media>=0 and media<=10:
    if media>=5:
        print("aprovado") #Final 1
    elif media>=3:
        print("exame") #Final 2
    else:
        print("reprovado") #Final 3
else:
    print("invalido") #Erro