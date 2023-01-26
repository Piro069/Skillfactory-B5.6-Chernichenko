print('Добро пожаловать в игру крестики нолики. Игра предназначена для двоих игроков. Нашли соперника? Тогда начнём!!!')
gamer1 = input("Введите имя игрока играющего х ")
gamer2 = input("Введите имя игрока играющего о ")
matrix = [
    ['-', '-', '-'],               # 0
    ['-', '-', '-'],               # 1
    ['-', '-', '-'],               # 2
]
matrix1 = [
    ['x', 'x', 'x'],
    ['x', 'x', 'x'],
    ['x', 'x', 'x'],
]
matrix2 = [
    ['o', 'o', 'o'],
    ['o', 'o', 'o'],
    ['o', 'o', 'o'],
]

while True:
    print('+ 0 1 2 ')
    print('0', *matrix[0])
    print('1', *matrix[1])
    print('2', *matrix[2])
    print(gamer1, 'Ваш ход')


    def fhod1v():                             # начало ходов
        hod1v = int(input("Цифра по вертикали"))
        return hod1v


    def fhod1g():
        hod1g = int(input("Цифра по горизонтали"))
        return hod1g


    while True:
        matrix[fhod1v()][fhod1g()] = 'x'
        break
    for i in matrix:
        break
    print('+ 0 1 2 ')
    print('0', *matrix[0])
    print('1', *matrix[1])
    print('2', *matrix[2])
    a = bool(matrix[0] == matrix1[0])  # 0 строка для х
    b = bool(matrix[0] == matrix2[0])  # 0 строка для о
    c = bool(matrix[1] == matrix1[1])  # 1 строка для х
    d = bool(matrix[1] == matrix2[1])  # 1 строка для о
    e = bool(matrix[2] == matrix1[2])  # 2 строка для х
    f = bool(matrix[2] == matrix2[2])  # 2 строка для о
    g1 = bool(matrix[0][0] == matrix1[0][0])
    g2 = bool(matrix[1][0] == matrix1[0][0])
    g3 = bool(matrix[2][0] == matrix1[2][0])
    g = g1 and g2 and g3  # 0 столбик для х
    k1 = bool(matrix[0][0] == matrix2[0][0])
    k2 = bool(matrix[1][0] == matrix2[0][0])
    k3 = bool(matrix[2][0] == matrix2[2][0])
    k = k1 and k2 and k3  # 0 столбик для о
    t1 = bool(matrix[0][1] == matrix1[0][1])
    t2 = bool(matrix[1][1] == matrix1[1][1])
    t3 = bool(matrix[2][1] == matrix1[2][1])
    t = t1 and t2 and t3  # 1 столбик для х
    m1 = bool(matrix[0][1] == matrix2[0][1])
    m2 = bool(matrix[1][1] == matrix2[1][1])
    m3 = bool(matrix[2][1] == matrix2[2][1])
    m = m1 and m2 and m3  # 1 столбик для о
    n1 = bool(matrix[0][2] == matrix1[0][2])
    n2 = bool(matrix[1][2] == matrix1[1][2])
    n3 = bool(matrix[2][2] == matrix1[2][2])
    n = n1 and n2 and n3  # 2 столбик для х
    o1 = bool(matrix[0][2] == matrix2[0][2])
    o2 = bool(matrix[1][2] == matrix2[1][2])
    o3 = bool(matrix[2][2] == matrix2[2][2])
    o = o1 and o2 and o3  # 2 столбик для о
    p1 = bool(matrix[0][0] == matrix1[0][0])
    p2 = bool(matrix[1][1] == matrix1[1][1])
    p3 = bool(matrix[2][2] == matrix1[2][2])
    p = p1 and p2 and p3  # диагональ x
    q1 = bool(matrix[0][0] == matrix2[0][0])
    q2 = bool(matrix[1][1] == matrix2[1][1])
    q3 = bool(matrix[2][2] == matrix2[2][2])
    q = q1 and q2 and q3  # диагональ o
    r1 = bool(matrix[0][2] == matrix1[0][2])
    r2 = bool(matrix[1][1] == matrix1[1][1])
    r3 = bool(matrix[2][0] == matrix1[2][0])
    r = r1 and r2 and r3  # диагональ / для х
    s1 = bool(matrix[0][2] == matrix1[0][2])
    s2 = bool(matrix[1][1] == matrix1[1][1])
    s3 = bool(matrix[2][0] == matrix1[2][0])
    s = s1 and s2 and s3  # диагональ / для o
    win = bool(a or b or c or d or e or f or g or k or t or m or n or o or p or q or r or s)
    if win is True:
        print('Победитель-', gamer1)
        break
    print(gamer2, 'Ваш ход')


    def fhod2v():
        hod2v = int(input("Цифра по вертикали"))
        return hod2v


    def fhod2g():
        hod2g = int(input("Цифра по горизонтали"))
        return hod2g


    while True:
        matrix[fhod2v()][fhod2g()] = 'o'
        break
    for j in matrix:
        break
    print('+ 0 1 2 ')
    print('0', *matrix[0])
    print('1', *matrix[1])
    print('2', *matrix[2])
    a = bool(matrix[0] == matrix1[0])  # 0 строка для х
    b = bool(matrix[0] == matrix2[0])  # 0 строка для о
    c = bool(matrix[1] == matrix1[1])  # 1 строка для х
    d = bool(matrix[1] == matrix2[1])  # 1 строка для о
    e = bool(matrix[2] == matrix1[2])  # 2 строка для х
    f = bool(matrix[2] == matrix2[2])  # 2 строка для о
    g1 = bool(matrix[0][0] == matrix1[0][0])
    g2 = bool(matrix[1][0] == matrix1[0][0])
    g3 = bool(matrix[2][0] == matrix1[2][0])
    g = g1 and g2 and g3  # 0 столбик для х
    k1 = bool(matrix[0][0] == matrix2[0][0])
    k2 = bool(matrix[1][0] == matrix2[0][0])
    k3 = bool(matrix[2][0] == matrix2[2][0])
    k = k1 and k2 and k3  # 0 столбик для о
    t1 = bool(matrix[0][1] == matrix1[0][1])
    t2 = bool(matrix[1][1] == matrix1[1][1])
    t3 = bool(matrix[2][1] == matrix1[2][1])
    t = t1 and t2 and t3  # 1 столбик для х
    m1 = bool(matrix[0][1] == matrix2[0][1])
    m2 = bool(matrix[1][1] == matrix2[1][1])
    m3 = bool(matrix[2][1] == matrix2[2][1])
    m = m1 and m2 and m3  # 1 столбик для о
    n1 = bool(matrix[0][2] == matrix1[0][2])
    n2 = bool(matrix[1][2] == matrix1[1][2])
    n3 = bool(matrix[2][2] == matrix1[2][2])
    n = n1 and n2 and n3  # 2 столбик для х
    o1 = bool(matrix[0][2] == matrix2[0][2])
    o2 = bool(matrix[1][2] == matrix2[1][2])
    o3 = bool(matrix[2][2] == matrix2[2][2])
    o = o1 and o2 and o3  # 2 столбик для о
    p1 = bool(matrix[0][0] == matrix1[0][0])
    p2 = bool(matrix[1][1] == matrix1[1][1])
    p3 = bool(matrix[2][2] == matrix1[2][2])
    p = p1 and p2 and p3  # диагональ x
    q1 = bool(matrix[0][0] == matrix2[0][0])
    q2 = bool(matrix[1][1] == matrix2[1][1])
    q3 = bool(matrix[2][2] == matrix2[2][2])
    q = q1 and q2 and q3  # диагональ o
    r1 = bool(matrix[0][2] == matrix1[0][2])
    r2 = bool(matrix[1][1] == matrix1[1][1])
    r3 = bool(matrix[2][0] == matrix1[2][0])
    r = r1 and r2 and r3  # диагональ / для х
    s1 = bool(matrix[0][2] == matrix1[0][2])
    s2 = bool(matrix[1][1] == matrix1[1][1])
    s3 = bool(matrix[2][0] == matrix1[2][0])
    s = s1 and s2 and s3  # диагональ / для o
    win = bool(a or b or c or d or e or f or g or k or t or m or n or o or p or q or r or s)
    if win is True:
        print('Победитель-', gamer2)
        break
    print(gamer1, 'Ваш ход')             # конец ходов
