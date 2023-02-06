w1 = [1, 2, 3]
w2 = [4, 5, 6]
w3 = [7, 8, 9]
w4 = [1, 4, 7]
w5 = [2, 5, 8]
w6 = [3, 6, 9]
w7 = [1, 5, 9]
w8 = [3, 5, 7]

g1 = []
g2 = []

img = [1, 2, 3, 4, 5, 6, 7, 8, 9]

i = 1
sk = 1

while i < 10:

    print('    ', img[0], '|', img[1], '|', img[2])
    print('     ---------')
    print('    ', img[3], '|', img[4], '|', img[5])
    print('     ---------')
    print('    ', img[6], '|', img[7], '|', img[8])

    print('')

    if i % 2 != 0:
        a = int(input('  Iveskite ( X ) : '))

    if a == 1 or a == 2 or a == 3 or a == 4 or a == 5 or a == 6 or a == 7 or a == 8 or a == 9:
        if i % 2 != 0:

            img[a - 1] = 'X'
            g1.append(a)
            g1.sort()
            if g1 == w1 or g1 == w2 or g1 == w3 or g1 == w4 or g1 == w5 or g1 == w6 or g1 == w7 or g1 == w8:
                print('')
                print('    ', img[0], '|', img[1], '|', img[2])
                print('     ---------')
                print('    ', img[3], '|', img[4], '|', img[5])
                print('     ---------')
                print('    ', img[6], '|', img[7], '|', img[8])
                print('')
                print(' Laimejo ( X )')
                break

        else:
            a = int(input('  Iveskite ( O ) : '))

            img[a - 1] = '0'
            g2.append(a)
            g2.sort()
            if g2 == w1 or g2 == w2 or g2 == w3 or g2 == w4 or g2 == w5 or g2 == w6 or g2 == w7 or g2 == w8:
                print('')
                print('    ', img[0], '|', img[1], '|', img[2])
                print('     ---------')
                print('    ', img[3], '|', img[4], '|', img[5])
                print('     ---------')
                print('    ', img[6], '|', img[7], '|', img[8])

                print('')
                print('  Laimejo ( O ) ')
                break
        i = i + 1
else:
    print('')
    print('    ', img[0], '|', img[1], '|', img[2])
    print('     ---------')
    print('    ', img[3], '|', img[4], '|', img[5])
    print('     ---------')
    print('    ', img[6], '|', img[7], '|', img[8])

    print('')

    print('lygiosios')




