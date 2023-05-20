print("Calculo do tempo necessario para a população A ultrapassar a população B")
popa=98000000
popb=200000000
anos=0
while popa<popb:
    popa=popa+popa*3.5/100
    popb=popb+popb*1.5/100
    anos=anos+1
print(f"Sera em torno de {anos} anos para alcançar")