import os
print("analise de peças aprovadas e reprovadas")
conta=0
contb=0
for i in range(1,4):
    print(f"peça nº{i}")
    codig=int(input("digite o codigo: "))
    estado=input("digite o estado da peça A/R: ").upper()
    while estado!= "A" and estado!= "R":
        estado=input("dado invalido, regedite A/R: ").upper()
    if estado=="A":
        conta=conta+1
    else:
        contb=contb+1
        print(f"A peça de{codig} está reprovada")
print(f"{conta} peças foram aprovadas, {contb} foram reprovadas")