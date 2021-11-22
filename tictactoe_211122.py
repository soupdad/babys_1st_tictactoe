def display_game(board):
    '''
    displays game board
    '''
    print(*board[7:10],sep = " | ")
    print('--|---|--')
    print(*board[4:7],sep =" | ")
    print('--|---|--')
    print(*board[1:4],sep =" | ")

def choose_icon():
    '''
    player chooses if they are X or O
    '''
    
    player1_icon = "bad"
    
    while player1_icon not in ['x','X','o','O']:
        player1_icon = input("Player 1, do you want to be X's or O's?: ")
        
        if player1_icon not in ['x','X','o','O']:
            print("Invalid Responce")
            
    return player1_icon.upper()

def game_start():
    '''
    player inputs if they want to start game
    '''
    
    start = "bad"
    
    while start not in ['y','Y','n','N']:
        start = input("Ready to Start?(y or n): ")
        
        if start not in ['y','Y','n','N']:
            print("Invalid Responce")
            
    return (start in ['y','Y'])

def game_position(board):
    '''
    players input where they want to place their piece on board
    '''
    
    position = "bad"
    
    good_positions = [1,2,3,4,5,6,7,8,9]
    
    while (position not in good_positions) or (board[position] in ['X','O']):
        position = int(input("Choose your Position (1-9): "))
        
        if board[position] in ['X','O']:
            print("Space Taken")
        elif position not in good_positions:
            print("Invalid Responce")
    
    return position

def replace(position,board,icon,turn):
    '''
    replaces blank space with players marker
    '''
    if turn%2 == 1:
        board[position] = icon
    else:
        if icon == 'X':
            board[position] = 'O'
        else:
            board[position] = 'X'
            
    return turn +1

def check_winner(board,turn):
    '''
    check if there is a winner
    '''
    
    return (board[1::3].count('X') == 3) or (board[2::3].count('X') == 3) or (board[3::3].count('X') == 3) or (board[1::3].count('O') == 3) or (board[2::3].count('O') == 3) or (board[3::3].count('O') == 3) or (board[1:4].count('X') == 3) or (board[4:7].count('X') == 3) or (board[7:].count('X') == 3) or (board[1:4].count('O') == 3) or (board[4:7].count('O') == 3) or (board[7:].count('O') == 3) or (board[1::4].count('X') == 3) or (board[3:8:2].count('X') == 3) or (board[1::4].count('O') == 3) or (board[3:8:2].count('O') == 3)

def game_again():
    '''
    player inputs if they want to play another game
    '''
    
    start = "bad"
    
    while start not in ['y','Y','n','N']:
        start = input("Play Again?(y or n): ")
        
        if start not in ['y','Y','n','N']:
            print("Invalid Responce")
            
    return (start in ['y','Y'])

from random import randint

def starting_player():
    return randint(1,2)

#COMPUTER FUNCTION

def comp_pvp():
    '''
    player chooses if they want to play another person or the computer, bool
    '''
    
    comp_pvp = "bad"
    
    while comp_pvp not in ['comp','p']:
        comp_pvp = input("Choose whether to play against computer or another human - you have to provide the human: (comp or p) ").lower()
        
        if comp_pvp not in ['comp','p']:
            print("Invalid Responce")
            
    return (comp_pvp == 'p')

from random import randint

def comp_move(board):
    '''
    returns int of where computer wants to place icon
    '''
    comp_valid = True
    
    while comp_valid:
        comp_move = randint(1,9)
    
        if board[comp_move] in ['X','O']:
            continue
        else:
            return comp_move 
            comp_valid = False

#GAME

game_starting = True

while game_starting:
    game_on = False
    whos_turn = 0
    game_board = ['#',' ',' ',' ',' ',' ',' ',' ',' ',' ']
    
    #P VS P
    
    if comp_pvp():
    
        p1_icon = choose_icon()
        whos_turn = starting_player()
        
        if whos_turn == 1:
            print('Player 1 goes first')
        else:
            print('Player 2 goes first')
        
        if game_start():
            game_on = True
        else:
            game_starting = False

        while game_on:
    
            display_game(game_board)
            position = game_position(game_board)
            whos_turn = replace(position,game_board,p1_icon,whos_turn)
            
            if check_winner(game_board,whos_turn):
                display_game(game_board)
                if whos_turn%2 == 0:
                    print('Congrats Player 1, You Win!')
                elif whos_turn%2 == 1:
                    print('Congrats Player 2, You Win!')
            elif any([item in ' ' for item in game_board]) == False:
                display_game(game_board)
                print("Aw damn, It's a Draw :(")
            else:
                continue
            if game_again():
                game_on = False
            else:
                game_on = False
                game_starting = False
        
    #P VS COMP
        
    else:
        p1_icon = choose_icon()
        whos_turn = starting_player()
        
        if whos_turn == 1:
            print('Player goes first')
        else:
            print('Computer goes first')
        
        if game_start():
            game_on = True
        else:
            game_starting = False

        while game_on:
        
            #PLAYER
        
            if whos_turn%2 == 1:
                display_game(game_board)
                position = game_position(game_board)
                whos_turn = replace(position,game_board,p1_icon,whos_turn)
        
                if check_winner(game_board,whos_turn):
                    display_game(game_board)
                    if whos_turn%2 == 0:
                        print('Congrats Player, You Win!')
                elif any([item in ' ' for item in game_board]) == False:
                    display_game(game_board)
                    print("Aw damn, It's a Draw :(")
                else:
                    continue
                if game_again():
                    game_on = False
                else:
                    game_on = False
                    game_starting = False
                    
            #COMP
                    
            elif whos_turn%2 == 0:
                position = comp_move(game_board)
                whos_turn = replace(position,game_board,p1_icon,whos_turn)
                
                if check_winner(game_board,whos_turn):
                    display_game(game_board)
                    if whos_turn%2 == 1:
                        print('Sorry Player, You Lose')
                elif any([item in ' ' for item in game_board]) == False:
                    display_game(game_board)
                    print("Aw damn, It's a Draw :(")
                else:
                    continue
                if game_again():
                    game_on = False
                else:
                    game_on = False
                    game_starting = False