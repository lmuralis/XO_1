w1 = [1, 2, 3]    # Выигрышные комбинации
w2 = [4, 5, 6]
w3 = [7, 8, 9]
w4 = [1, 4, 7]
w5 = [2, 5, 8]
w6 = [3, 6, 9]
w7 = [1, 5, 9]
w8 = [3, 5, 7]

g1 = []           # Игроки
g2 = []

img = ['1', '2', '3', '4', '5', '6', '7', '8', '9']    # Поле

i = 1

while i < 7:

    print('    ', img[0], '|', img[1], '|', img[2])
    print('     ---------')
    print('    ', img[3], '|', img[4], '|', img[5])
    print('     ---------')
    print('    ', img[6], '|', img[7], '|', img[8])

    print('')
#---------------------------------------------------------
    if i % 2 != 0:
        a = input(' Введите ( Х ): ' )
        while a not in img:
            a = input(' Введите число: ')
        a = int(a)
#-------------------------------------------------------
    else:
        a = input(' Введите ( O ): ' )
        while a not in img:
            a = input(' Введите число: ')
        a = int(a)
#-------------------------------------------------------------------------------------------
    if a == 1 or a == 2 or a == 3 or a == 4 or a == 5 or a == 6 or a == 7 or a == 8 or a == 9:
#--------------------------------------------------------------------------------------------
        if i % 2 != 0:

            img[a - 1] = 'X'
            g1.append(a)
            g1.sort()
            print(g1)
            print('')
            if g1 == w1 or g1 == w2 or g1 == w3 or g1 == w4 or g1 == w5 or g1 == w6 or g1 == w7 or g1 == w8:
                print('')
                print('    ', img[0], '|', img[1], '|', img[2])
                print('     ---------')
                print('    ', img[3], '|', img[4], '|', img[5])
                print('     ---------')
                print('    ', img[6], '|', img[7], '|', img[8])
                print('')
                print(' Выиграл ( Х )')
                break
#---------------------------------------------------------------------------------------------
        else:

            img[a - 1] = '0'
            g2.append(a)
            g2.sort()
            print(g2)
            print('')
            if g2 == w1 or g2 == w2 or g2 == w3 or g2 == w4 or g2 == w5 or g2 == w6 or g2 == w7 or g2 == w8:
                print('')
                print('    ', img[0], '|', img[1], '|', img[2])
                print('     ---------')
                print('    ', img[3], '|', img[4], '|', img[5])
                print('     ---------')
                print('    ', img[6], '|', img[7], '|', img[8])

                print('')
                print('  Выиграл ( O ) ')
                break
        i += 1
else:
    print('')
    print('    ', img[0], '|', img[1], '|', img[2])
    print('     ---------')
    print('    ', img[3], '|', img[4], '|', img[5])
    print('     ---------')
    print('    ', img[6], '|', img[7], '|', img[8])
    print('')

    print('  Ничья в игре')
