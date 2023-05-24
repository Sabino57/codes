#sabino
print("Definir valor de multa perante ao peso em KG do peixe.")
peso=float(input(f"\nDigite o peso:")) #Valor do peso
if peso>=0:
    if peso>50:
        e=peso-50
        m=e*4 #Valor Multa
        print(f"Valor da multa seria de: {m}") #final 1
    else:
        e=0
        m=0
        print("Sem multa a pagar") #final 2
else:
    print("Dados invalidos") #Erro