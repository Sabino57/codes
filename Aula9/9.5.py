print('<Preço de importação de 5 produtos>')

j=int(input("<Digite o valor 5: "))

c = 1
p1 = 0
p2 = 0
p3 = 0
p4 = 0
p5 = 0
if j==5:

    while c <= j:

        print('\n<Coloque o preço unitario do produto:')
        preco = float(input())
        while preco <= 0:
            print('preço invalido\n insira novamente:')
            preco = float(input())
        
        print('<coloque o pais de origem de acordo como codigo:')
        print('\n1 = EUA', ('\n2 = Mexico'), ('\n3 = outros'))
        pais = int(input())
        while pais != 1 and pais != 2 and pais != 3:
            print('codigo invalido\n',('codigo invalido!\n'),('coloque novamente:'))
            pais = int(input())

        print('<coloque o meio de transporte:')
        print('\nT = terrestre',('\nF = fluvial'),('\nA = aereo'))
        print('coloque o codigo:')  
        transporte = (input()).upper()
        while transporte != 'T' and transporte != 'F' and transporte != 'A':
            print('codigo invalido!\n',('digite novamente:'))
            transporte = (input()).upper()

        print('a carga é perigosa? S/N')
        sn = (input()).upper()
        while sn != 'S' and sn != 'N':
            print('opção invalida\n',('coloque novamente: '))
            sn = (input()).upper()

        if c == 1:
            if preco <= 100:
                p1 = preco + (preco * 0.05)
            else:
                p1 = preco + (preco * 0.1)
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
                p1 += (preco / 2)
        
        elif c == 2:
            if preco <= 100:
                p2 = preco + (preco * 0.05)
            else:
                p2 = preco + (preco * 0.1)
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
                p2 += (preco / 2)
            
        elif c == 3:
            if preco <= 100:
                p3 = preco + (preco * 0.05)
            else:
                p3 = preco + (preco * 0.1)
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
                p3 += (preco / 2)
        
        elif c == 4:
            if preco <= 100:
                p4 = preco + (preco * 0.05)
            else:
                p4 = preco + (preco * 0.1)
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
                p4 += (preco / 2)
            
        else:
            if preco <= 100:
                p5 = preco + (preco * 0.05)
            else:
                p5 = preco + (preco * 0.1)
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
                p5 += (preco / 2)
        c += 1
        
    print('\n<O preço total de cada produto foi de:')
    print('nº1 R${:.2f}'.format(p1))
    print('nº2 R${:.2f}'.format(p2))
    print('nº3 R${:.2f}'.format(p3))
    print('nº4 R${:.2f}'.format(p4))
    print('nº5 R${:.2f}'.format(p5))
else:
    print("Valor invalido")
