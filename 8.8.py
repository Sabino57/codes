print(f"\nCalculadora aritimetica ")
n=int(input(f"\n\nDigite a quantidade de repetições:"))
c=1
x=0
while c<= n:
    n1 =float(input(f"\nColoque o numero: "))
    x += n1
    c += 1
n2 = x / n
print(f"A media aritimetica é de: {n2}")