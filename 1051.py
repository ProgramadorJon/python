n = float(input())
if n <= 2000.00:
    a = 0
    print('Isento')
if 2000.00 < n <= 3000.00:
    ir = n - 2000.00
    a = ir * (8 / 100)
if 3000.00 < n <= 4500.00:
    ir = (8 / 100) * (1000.00)
    ir1 = n - 3000.00
    a = ir1 * (18 / 100) + ir
if n > 4500.00:
    ir = (8 / 100) * (1000.00)
    ir1 = (18 / 100) * (1500.00)
    ir2 = n - 4500.00
    a = ir1 + ir + ir2 * (28 / 100)
if n > 2000.00:
    a = float(a)
    print('R$ {:.2f}'.format(a))