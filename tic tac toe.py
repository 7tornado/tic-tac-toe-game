import numpy as np

game = np.array([['_', '_', '_'], ['_', '_', '_'], ['_', '_', '_']]) #создал матрицу
print(game)

print('----')

def move_player1(): #функция хода первого игрока
   step = int(input('В какую позицию поставить x? Ответьте - строка столбец '))
   if step == 11:
       game[0][0] = 'x'
   elif step == 12:
       game[0][1] = 'x'
   elif step == 13:
       game[0][2] = 'x'
   elif step == 21:
       game[1][0] = 'x'
   elif step == 22:
       game[1][1] = 'x'
   elif step == 23:
       game[1][2] = 'x'
   elif step == 31:
       game[2][0] = 'x'
   elif step == 32:
       game[2][1] = 'x'
   elif step == 33:
       game[2][2] = 'x'



move_player1()

print(game)

def move_player2(): #функция для хода второго игрока
    step2 = int(input('В какую позицию поставить 0? Ответьте - строка столбец '))
    if step2 == 11:
        game[0][0] = '0'
    elif step2 == 12:
        game[0][1] = '0'
    elif step2 == 13:
        game[0][2] = '0'
    elif step2 == 21:
        game[1][0] = '0'
    elif step2 == 22:
        game[1][1] = '0'
    elif step2 == 23:
        game[1][2] = '0'
    elif step2 == 31:
        game[2][0] = '0'
    elif step2 == 32:
        game[2][1] = '0'
    elif step2 == 33:
        game[2][2] = '0'



move_player2()

print(game)

move_player1()
print(game)
move_player2()
print(game)
move_player1()
print(game)
move_player2()
print(game)
move_player1()
print(game)
move_player2()
print(game)
move_player1()
print(game)
move_player2()
print(game)