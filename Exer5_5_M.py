print("""
Escolha um item e do lado a quantide:

1 - Cachorro-Quente     R$ 4,00
2 - X-Salada            R$ 4,50
3 - X-Bacon             R$ 5,00
4 - Torrada simples     R$ 2,00
5 - Refigerante         R$ 1,50

""")
item = map(int, input("Item/Quantidae: ").split())
n1, n2 = item
if n1 == 1:
    n = 4.00 * n2
    print("{} Cachorro-Quente, Total: R$ {:.2f}".format(n2,n))
elif n1 == 2:
    n = 4.50 * n2
    print("{} X-Salada, Total: R$ {:.2f}".format(n2,n))
elif n1 == 3:
    n = 5.00 * n2
    print("{} X-Bacon, Total: R$ {:.2f}".format(n2,n))
elif n1 == 4:
    n = 2.00 * n2
    print("{} Torrada simples, Total: R$ {:.2f}".format(n2,n))
elif n1 == 5:
    n = 1.50 * n2
    print("{} Refigerante, Total: R$ {:.2f}".format(n2,n))
else:
    n1 == 0 or n1 > 5
    print("Item Inválido!")