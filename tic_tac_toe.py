from random import randint


##### INITIAL PARAMETERS FOR PLAYERS #####


print('\n'*2)

print('-----Tic-Tac-Toe-----')
print('\n')
p = {11:'',22:'',111:0,222:0,'choose':None,'no_choose':None,'choice':None}
start_bit = 0
pick = None
recent_winner = None
recent_loser = None
player_1_name = ''
player_2_name = ''


while True:

    p['first'] = recent_winner
    p['second'] = recent_loser

    if start_bit == 0:
        print("Player 1, please enter your name: ")
        while player_1_name == '':
            player_1_name = input()
        print()

        print("Player 2, please enter your name: ")
        while player_2_name == '' or player_2_name == player_1_name:
            player_2_name = input()
        print()
        if randint(1,2) == 1:
            p['first'] = player_1_name
            recent_winner = player_1_name
            p['second'] = player_2_name
            start_bit += 1
        else:
            p['first'] = player_2_name
            recent_winner = player_2_name
            p['second'] = player_1_name
            start_bit += 1

    print(p['first'] + " chooses X's or O's first!", end='\n'*2)

    if p['first'] == player_1_name:
        while p[11] != 'X' and p[11] != 'O':
            print("Hey " + p['first'] + "!  Choose X or O.  (Tip:  X goes first!)")
            p[11] = input().upper()
            p['choice'] = p[11]
            if p[11] == 'X':
                p[22] = 'O'
                break
            elif p[11] == 'O':
                p[22] = 'X'
                p['first'] = player_2_name
                p['second'] = player_1_name
                break
    else:
        while p[22] != 'X' and p[22] != 'O':
            print("Hey " + p['first'] + "!  Choose X or O.  (Tip:  X goes first!)")
            p[22] = input().upper()
            p['choice'] = p[22]
            if p[22] == 'X':
                p[11] = 'O'
                break
            elif p[22] == 'O':
                p[11] = 'X'
                p['first'] = player_1_name
                p['second'] = player_2_name
                break

    print(recent_winner + " chose " + p['choice'])
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
    turn = 1
    while recent_winner != 'X' and recent_winner != 'O':
        print('\n'*20)
        print_board()
        print('\n'*5)
        if turn%2 != 0:
            print(p['first']+', pick a location: ')
            pick = input()
            while pick not in keypad or keypad[pick] != ' ':
                print(pick)
                print("NOPE!  Either you didn't pick a number 1 through 9 or \n something is already in this location.  Try again: ")
                pick = input()
            if p['first'] == player_1_name:
                keypad[pick] = p[11]
            else:
                keypad[pick] = p[22]
        else:
            print(p['second']+', pick a location: ')
            pick = input()
            while pick not in keypad or keypad[pick] != ' ':
                print(pick)
                print("NOPE!  Either you didn't pick a number 1 through 9 or \n something is already in this location.  Try again: ")
                pick = input()
            if p['second'] == player_1_name:
                keypad[pick] = p[11]
            else:
                keypad[pick] = p[22]
        turn += 1
        print(winning_condition())
        recent_winner = winning_condition()
    if recent_winner == p[11]:
        recent_winner = player_1_name
        recent_loser = player_2_name
        p['first'] = player_1_name
        p['second'] = player_2_name
        p[111] += 1
    else:
        recent_winner = player_2_name
        recent_loser = player_1_name
        p['first'] = player_2_name
        p['second'] = player_1_name
        p[222] += 1
    p[11] = ''
    p[22] = ''
    print('\n'*20)
    print_board()
    print('\n'*10)
    print("CONGRATULATIONS " + recent_winner + "!")
    print()
    print("Current score is:")
    print(player_1_name + " " + str(p[111]))
    print(player_2_name + " " + str(p[222]))
    print()
    print("Input 'Q' to quit, or any other input to continue playing: ")
    if input().lower() == 'q':
        break
