
'''compra = input('compra:')
compras =[]
compras.append(compra)
print(f'suas compras compras:{compras}')'''
'''
i = 0 #i recebe o valor 0 para começar com esse valor
compras = [] #compras receber uma lista vazia
while i <10: #enquanto repetir até a ser saciada o valor 10
    compra = input('compras:') #compra recebe input
    compras.append(compra) #adicionando na lista que foi criada
    i +=1 #soma mais uma
    print(compras) #printa a lista


print(f'compras{compras}')#exibe a lista de compras com as compras adicionadas'''


class venda():
    def __init__(self, produto, compras):
        self.produto = produto
        self.compras = compras

    compras = []
    i = 0
    while i < 10:
        produto = input("compras:")
        compras.append(produto)
        i += 1
        print(f'voce comprou {produto}')
        print(compras)
    print(f'Total de todas as compras: {compras}')

    ans = True
    while ans:
        print("""
        1.compras
        2.excluir 
        3.somar
        4.quit
        """)
        ans = input('What do you do?')
        if ans == '1':
            print(f'todos as compras{compras}')



        elif ans == '2':
            print(f'{compras}')
            del_compras = int(input('Qual voce quer excluir:'))
            del_compras.pop(del_compras)
            print(compras.replace(del_compras))
        elif ans == '3':
            print('somar')
        else:
            print('quit')
        break



