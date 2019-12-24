from random import randint


##### INITIAL PARAMETERS FOR PLAYERS #####


p = {1:None,2:None,11:'',22:'','choose':None,'no_choose':None,'choice':None}

print('\n'*2)

print('-----Tic-Tac-Toe-----')
print('\n')

print("Player 1, please enter your name: ")
p[1] = 'Player Wonnnnn'
print()

print("Player 2, please enter your name: ")
p[2] = 'Player Tooooo'
print()

p['choose'] = None
p['no_choose'] = None

if randint(1,2) == 1:
    p['choose'] = p[1]
    p['no_choose'] = p[2]
else:
    p['choose'] = p[2]
    p['no_choose'] = p[1]

print(p['choose'] + " chooses X's or O's first!", end='\n'*2)

while p[11] == '' or p[22] == '':
    if p['choose'] == p[1]:
        while p[11] != 'X' and p[11] != 'O':
            print("Hey " + p['choose'] + "!  Choose X or O.  (Tip:  X goes first!)")
            p[11] = input().upper()
            p['choice'] = p[11]
            if p[11] == 'X':
                p[22] = 'O'
            else:
                p[22] = 'X'
    else:
        while p[22] != 'X' and p[22] != 'O':
            print("Hey " + p['choose'] + "!  Choose X or O.  (Tip:  X goes first!)")
            p[22] = input().upper()
            p['choice'] = p[22]
            if p[22] == 'X':
                p[11] = 'O'
            else:
                p[11] = 'X'

print(p['choose'] + " chose " + p['choice'])
print()

##### THIS IS THE GAME BOARD CODE #####

keypad = {'1':' ','2':' ','3':' ','4':' ','5':' ','6':' ','7':' ','8':' ','9':' '}

def print_board():
    board = [[' ',' ',' ','|',' ',' ',' ','|',' ',' ',' '],
    [' ',keypad['7'],' ','|',' ',keypad['8'],' ','|',' ',keypad['9'],' '],
    [' ',' ',' ','|',' ',' ',' ','|',' ',' ',' '],
    ['-','-','-','|','-','-','-','|','-','-','-'],
    [' ',' ',' ','|',' ',' ',' ','|',' ',' ',' '],
    [' ',keypad['4'],' ','|',' ',keypad['5'],' ','|',' ',keypad['6'],' '],
    [' ',' ',' ','|',' ',' ',' ','|',' ',' ',' '],
    ['-','-','-','|','-','-','-','|','-','-','-'],
    [' ',' ',' ','|',' ',' ',' ','|',' ',' ',' '],
    [' ',keypad['1'],' ','|',' ',keypad['2'],' ','|',' ',keypad['3'],' '],
    [' ',' ',' ','|',' ',' ',' ','|',' ',' ',' ']]
    for x in board:
        print(' '.join(x))

pick = None
turn = 1
winner = None

def winning_condition():
        if keypad['7'] == keypad['8'] == keypad['9'] == 'X' or\
        keypad['4'] == keypad['5'] == keypad['6'] == 'X' or\
        keypad['1'] == keypad['2'] == keypad['3'] == 'X' or\
        keypad['7'] == keypad['4'] == keypad['1'] == 'X' or\
        keypad['8'] == keypad['5'] == keypad['2'] == 'X' or\
        keypad['9'] == keypad['6'] == keypad['3'] == 'X' or\
        keypad['7'] == keypad['5'] == keypad['3'] == 'X' or\
        keypad['1'] == keypad['5'] == keypad['9'] == 'X':
            return 'X'
        elif keypad['7'] == keypad['8'] == keypad['9'] == 'O' or\
        keypad['4'] == keypad['5'] == keypad['6'] == 'O' or\
        keypad['1'] == keypad['2'] == keypad['3'] == 'O' or\
        keypad['7'] == keypad['4'] == keypad['1'] == 'O' or\
        keypad['8'] == keypad['5'] == keypad['2'] == 'O' or\
        keypad['9'] == keypad['6'] == keypad['3'] == 'O' or\
        keypad['7'] == keypad['5'] == keypad['3'] == 'O' or\
        keypad['1'] == keypad['5'] == keypad['9'] == 'O':
            return 'O'
        else:
            return None

while winner != 'X' and winner != 'O':
    print('\n'*20)
    print_board()
    print('\n'*5)
    if turn%2 != 0:
        print(p['choose']+', pick a location: ')
        pick = input()
        while pick not in keypad or keypad[pick] != ' ':
            print(pick)
            print("NOPE!  Either you didn't pick a number 1 through 9 or \n something is already in this location.  Try again: ")
            pick = input()
        if p['choose'] == p[1]:
            keypad[pick] = p[11]
        else:
            keypad[pick] = p[22]
    else:
        print(p['no_choose']+', pick a location: ')
        pick = input()
        while pick not in keypad or keypad[pick] != ' ':
            print(pick)
            print("NOPE!  Either you didn't pick a number 1 through 9 or \n something is already in this location.  Try again: ")
            pick = input()
        if p['no_choose'] == p[1]:
            keypad[pick] = p[11]
        else:
            keypad[pick] = p[22]
    print(winning_condition())
    winner = winning_condition()
    turn += 1
if winner == p[11]:
    winner = p[1]
else:
    winner = p[2]
print('\n'*10)
print("CONGRATULATIONS " + winner + "!")
###THIS IS A PERSONAL TEST LINE
##NEXT TEST
###TEST NEXT NEXT
