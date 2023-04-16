#sabino
print(f"\n\ndefinir o maior numero, menor e media>") #introdução
n1=int(input("Digite o primeiro numero:")) 
n2=int(input("Digite o segundo numero:")) 
n3=int(input("Digite o terceiro numero:")) 
if n1>0 and n2>0 and n3>0:
    if n1>n2 and n1>n3:
        maior=n1 #maior
    elif n2>n3:
        maior=n2 #maior
    else:
        maior=n3 #maior
    if n1<n2 and n1<n3:
        menor=n1 #menor
    elif n1<n3:
        menor=n2 #menor
    else:
        menor=n3 #menor
    media=(n1+n2+n3)/3 #media
    print(f"maior:{maior}, menor:{menor} e media:{media}") #Resultado Final
else:
    print("Não foi possivel realizar a operação") #Erro
