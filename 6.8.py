#Sabino
print("calcular o peso ideal entre dois sexos")
sexo=input("digite o sexo F/M>:").upper() #Escolher genero
if sexo=="F" or sexo=="M":
    altura=float(input("digite a altura:")) #Altura
    if altura>=0.4 or altura<=3:
        if sexo=="F" or sexo=="f": #feminino
            peso=62.1*altura-44.7
        else: #masculino 
            peso=72.7*altura-58
        print(f"Seu peso ideal seria: {peso}")
    else: #erro
        print("altura invalida")   
else: #erro
    print("sexo invalido") 
