import os
print("Jogo de advinha")
j1=int(input("Digite o valor entre 1 a 10 para advinhar(j1):"))
while j1<1 or j1>10:
    j1=int(input("Valor invalido, tem que ser entre 1 a 10:"))
os.system("cls")
j2=int(input("Digite o valor entre 1 a 10 para acertar(j2): "))
while j2<1 or j2>10:
    j2=int(input("Valor invalido, tem que ser entre 1 a 10:"))
tent=1
while j1!=j2:
    j2=int(input("Digite o valor entre 1 a 10 para acertar(j2): "))
    while j2<1 or j2>10:
        j2=int(input("Valor invalido, tem que ser entre 1 a 10:"))
    tent=tent+1
print(f"Você acertou {tent} tentativas")