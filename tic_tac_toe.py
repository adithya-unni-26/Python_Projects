board={'7':' ', '8':' ','9':' ',
'4':' ','5':' ','6':' ',
'1':' ','2':' ','3':' '}
def print_board():
    print('Game Board\n')
    print(board['7']+  '| '+ board['8']+  '|'+ board['9'])
    print('---------')
    print(board['4']+  '| '+ board['5']+  '|'+ board['6'])
    print('---------')
    print(board['1']+  '| '+  board['2']+  '|'+ board['3'])

board_keys=[]
for key in board:
    board_keys.append(key)
    
def game():
    print_board()
    turn='X'
    count=0
    while count<10:
        x_o = input(f"Its {turn}'s turn now. Where would you like to place your marker:\t")
        if board[x_o]==' ':
            board[x_o]=turn
            count+=1
            print_board()
        else:
            print('The place is occupied.Try another place')

    
        if count>=5:
            if board['1']==board['2']==board['3']!=' ':
                print(f'Game over The winner is {turn}')
                break
            if board['4']==board['5']==board['6']!=' ':
                print(f'Game over The winner is {turn}')
                break
            if board['7']==board['8']==board['9']!=' ':
                print(f'Game over The winner is {turn}')
                break
            if board['1']==board['4']==board['7']!=' ':
                print(f'Game over The winner is {turn}')
                break
            if board['2']==board['5']==board['8']!=' ':
                print(f'Game over The winner is {turn}')
                break
            if board['3']==board['6']==board['9']!=' ':
                print(f'Game over The winner is {turn}')
                break
            if board['7']==board['5']==board['3']!=' ':
                print(f'Game over The winner is {turn}')
                break
            if board['1']==board['5']==board['9']!=' ':
                print(f'Game over The winner is{turn}')
                break
        if turn=='X':
            turn='O'
        else:
            turn='X'
    
    if count==9:
        play_again=input('Game over.Its a TIE!!')
        
    
    restart = input("Do want to play Again?(y/n):\t")
    if restart == "y" or restart == "Y":  
        for key in board_keys:
            theBoard[key] = " "
        game()
    if restart == "n" or restart == "N":
        pass
            
if __name__=="__main__":
    game()