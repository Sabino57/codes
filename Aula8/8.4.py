print ("exibe o algoritimo e imprimo o quadrado")
n=int(input("Digite o numero:"))
for j in range(1,n+1,1):
    print("Digite o",j,"º numero: ",end="")
    num = int(input())
    quad=num*num
    print(f"o quadrado de {num} seria: {quad}")