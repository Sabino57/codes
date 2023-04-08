#arthur
print("cálcular um aumento no salário")

Sal=float(input("digite o valor do salário atual: "))
Por=float(input("digite o aumento em %: "))

aumen_novoSal=float(Sal*Por/100)
novo_salario=float(aumen_novoSal+Sal)
print("a soma é de: ",novo_salario)