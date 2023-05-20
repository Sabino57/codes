print('preço de importação de 5 produtos')

c = 1
p1 = 0
p2 = 0
p3 = 0
p4 = 0
p5 = 0

while c <= 5:

    print('Coloque o preço unitario do produto:')
    preço = float(input())
    while preço <= 0:
        print('preço invlido\n',end=('insira novamente:'))
        preço = float(input())
    
    print('coloque o pais de origem de acordo como codigo:')
    print('1 = EUA\n',end=('2 = Mexico\n'),end=('3 = outros'))
    pais = int(input())
    while pais != 1 and pais != 2 and pais != 3:
        print('codigo invalido\n',end=('codigo invalido!\n'),end=('coloque novamente:'))
        pais = int(input())

    print('coloque o meio de transporte:')
    print('T = terrestre\n',end=('F = fluvial\n'),end=('A = aereo'))
    print('coloque o codigo:')  
    transporte = str(input())
    while transporte != 't' and transporte != 'f' and transporte != 'a':
        print('codigo invalido!\n',end=('digite novamente:'))
        transporte = str(input())

    print('a carga é perigosa? S/N')
    sn = str(input())
    while sn != 's' and sn != 'n':
        print('opção invalida\n',end=('coloque novamente: '))
        sn = str(input())

    if c == 1:
        if preço <= 100:
            p1 = preço + (preço * 0.05)
        else:
            p1 = preço + (preço * 0.1)
        if sn == 's':
            if pais == '1':
                p1 += 50
            elif pais == '2':
                p1 += 35
            else:
                p1 += 24
        else:
            if pais == '1':
                p1 += 12
            elif pais == '2':
                p1 += 35
            else:
                p1 += 60
        if pais == '2' or transporte == 'a':
            p1 += (preço / 2)
    
    elif c == 2:
        if preço <= 100:
            p2 = preço + (preço * 0.05)
        else:
            p2 = preço + (preço * 0.1)
        if sn == 's':
            if pais == '1':
                p2 += 50
            elif pais == '2':
                p2 += 35
            else:
                p2 += 24
        else:
            if pais == '1':
                p2 += 12
            elif pais == '2':
                p2 += 35
            else:
                p2 += 60
        if pais == '2' or transporte == 'a':
            p2 += (preço / 2)
        
    elif c == 3:
        if preço <= 100:
            p3 = preço + (preço * 0.05)
        else:
            p3 = preço + (preço * 0.1)
        if sn == 's':
            if pais == '1':
                p3 += 50
            elif pais == '2':
                p3 += 35
            else:
                p3 += 24
        else:
            if pais == '1':
                p3 += 12
            elif pais == '2':
                p3 += 35
            else:
                p3 += 60
        if pais == '2' or transporte == 'a':
            p3 += (preço / 2)
    
    elif c == 4:
        if preço <= 100:
            p4 = preço + (preço * 0.05)
        else:
            p4 = preço + (preço * 0.1)
        if sn == 's':
            if pais == '1':
                p4 += 50
            elif pais == '2':
                p4 += 35
            else:
                p4 += 24
        else:
            if pais == '1':
                p4 += 12
            elif pais == '2':
                p4 += 35
            else:
                p4 += 60
        if pais == '2' or transporte == 'a':
            p4 += (preço / 2)
        
    else:
        if preço <= 100:
            p5 = preço + (preço * 0.05)
        else:
            p5 = preço + (preço * 0.1)
        if sn == 's':
            if pais == '1':
                p5 += 50
            elif pais == '2':
                p5 += 35
            else:
                p5 += 24
        else:
            if pais == '1':
                p5 += 12
            elif pais == '2':
                p5 += 35
            else:
                p5 += 60
        if pais == '2' or transporte == 'a':
            p5 += (preço / 2)
    c += 1
    
print('O preço total de cada produto foi de:')
print('nº1 R${:.2f}'.format(p1))
print('nº2 R${:.2f}'.format(p2))
print('nº3 R${:.2f}'.format(p3))
print('nº4 R${:.2f}'.format(p4))
print('nº5 R${:.2f}'.format(p5))
