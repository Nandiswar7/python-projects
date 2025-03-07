#building the tictactoe board
TheBoard = {'topL':' ','topM':' ','topR':' ','midL':' ','midM':' ','midR':' ','btmL':' ','btmM':' ','btmR':' '}

# displaying the board
def printBoard(TheBoard):
    print(TheBoard['topL']+'|'+TheBoard['topM']+'|'+TheBoard['topR'])
    print('-+-+-')
    print(TheBoard['midL']+'|'+TheBoard['midM']+'|'+TheBoard['midR'])
    print('-+-+-')
    print(TheBoard['btmL']+'|'+TheBoard['btmM']+'|'+TheBoard['btmR'])

turn = 'X'
for i in range(9):
    print('turn for',turn,'move on which space :')

    #input for position
    move = input()
    TheBoard[move] = turn

    #swapping the turns alternatively
    if turn == 'X':
        turn = 'O'
    else:
        turn = 'X'

    printBoard(TheBoard)

    #checking the which player won
    if(TheBoard['topL'] == TheBoard['topM'] == TheBoard['topR'] == ('X' or 'O')):
        print('the player',TheBoard['topL'],'won')
        break
    elif(TheBoard['midL'] == TheBoard['midM'] == TheBoard['midR'] == ('X' or 'O')):
        print('the player',TheBoard['midL'],'won')
        break
    elif(TheBoard['btmL'] == TheBoard['btmM'] == TheBoard['btmR'] == ('X' or 'O')):
        print('the player',TheBoard['btmL'],'won')
        break
    elif(TheBoard['topL'] == TheBoard['midL'] == TheBoard['btmL'] == ('X' or 'O')):
        print('the player',TheBoard['topL'],'won')
        break
    elif(TheBoard['topM'] == TheBoard['midM'] == TheBoard['btmM'] == ('X' or 'O')):
        print('the player',TheBoard['topM'],'won')
        break
    elif(TheBoard['topR'] == TheBoard['midR'] == TheBoard['btmR'] == ('X' or 'O')):
        print('the player',TheBoard['topR'],'won')
        break
    elif(TheBoard['topL'] == TheBoard['midM'] == TheBoard['btmR'] == ('X' or 'O')):
        print('the player',TheBoard['topL'],'won')
        break
    elif(TheBoard['topR'] == TheBoard['midM'] == TheBoard['btmL'] == ('X' or 'O')):
        print('the player',TheBoard['topR'],'won')
        break