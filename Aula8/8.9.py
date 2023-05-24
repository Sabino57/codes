s=0
for i in range(1,4,1):
    print(i,"º Aluno: ")
    n1=float(input("Digite a primeira nota: "))
    n2=float(input("Digite a segunda nota: "))
    media = (n1+n2)/2
    print(f"A sua media é de: {media:.1f}")
    s=s+media
mediasala=s/3
print(f"A media da sala seria: {mediasala:.2f}")