#sabino
print("definir o maior numero, menor e media>")
n1=float(input("Digite o primeiro numero: ")) #Valor1
n2=float(input("Digite o segundo numero: ")) #Valor2
n3=float(input("Digite o terceiro numero: ")) #Valor3
if n1>0 and n2>0 and n3>0:
    if n1>n2 and n1>n3:
        maior=n1 #maior
    elif n2>n3:
        maior=n2 #maior
    else:
        maior=n3 #maior
    if n1<n2 and n1<n3:
        menor=n1 #maior
    elif n1<n3:
        menor=n2 #maior
    else:
        menor=n3 #maior
    media=(n1+n2+n3)/3 #media
    print(f"maior:{maior}, menor:{menor} e media:{media}") #Resultado Final
else:
    print("Não foi possivel realizar a operação") #Erro