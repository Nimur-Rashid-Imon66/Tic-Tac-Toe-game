
import time
print('              ___________________________________________________TEAM____________________________________________________') 
print("             |  _    _     _____     _______   _____            _         _    ___    ______   _   _   _____  ______     |")
print("             | / \  / \   /  _  \   /   _   \ /  __  \         / \  ___  / \  / _ \  /  _   \ / \ / \ /  __/ /  _   \    |")
print("             | | |__| |  /  / \  \  |  /_\  / | |  \  \        \  \/ _ \/  / | / \ | | /_\  / | |/  / |  \   | /_\  /    |")
print("             | | |__| | /  /___\  \ | |  \ \  | |__/  /_________\   / \   /  | \_/ | | |  \ \ | |\  \ |  /_  | |  \ \    |")
print("             | \_/  \_/ \_/     \_/ \_/   \_/ \______/___________\_/   \_/    \___/  \_/   \_/\_/ \_/ \____\ \_/   \_/   |")
print('             |___________________________________________________________________________________________________________|\n\n')



print('Welcome to TIC-TAC-TOE')
print(20*' ',"   reference:    ")
print(20*' ','     |    |      ')
print(20*' ','  1  | 2  | 3    ')
print(20*' ',"-----+----+----- ")
print(20*' ',"     |    |      ")
print(20*' ',"  4  | 5  | 6    ")
print(20*' ',"-----+----+----- ")
print(20*' ',"     |    |      ")
print(20*' ',"  7  | 8  | 9    \n")


def display_board():
    print()
    print(30*' ','reference:')
    print(4*' ','|    |',20*' ','|    |',4*' ',)
    print('  '+board[1]+'  | '+board[2]+'  | '+board[3]+'   ',10*' ','  1  | 2  | 3  ')
    print('-----+----+-----',10*' ',"-----+----+-----")
    print(4*' ','|    |',20*' ','|    |',4*' ',)
    print('  '+board[4]+'  | '+board[5]+'  | '+board[6]+'   ',10*' ',"  4  | 5  | 6   ")
    print('-----+----+-----',10*' ',"-----+----+-----")
    print(4*' ','|    |',20*' ','|    |',4*' ',)
    print('  '+board[7]+'  | '+board[8]+'  | '+board[9]+'   ',10*' ',"  7  | 8  | 9    \n\n")


def human_input(mark):
    while True:
        inp = input(f"[{man}] '{mark}' Enter your choice:")
        if inp.isdigit() and int(inp) <10 and int(inp) >0:
            inp = int(inp)
            if board[inp] == " ":
                return inp
            else:
                print(f"[{man}] '{mark}' place already taken.")
        else:
            print(f"[{man}] '{mark}' Enter valid option (1 - 9).")


def winning(mark,board):
    winning_place = [[1,2,3],[4,5,6],[7,8,9],[1,4,7],[2,5,8],[3,6,9],[1,5,9],[3,5,7]]
    for win_place in winning_place:
        if board[win_place[0]] == board[win_place[1]] == board[win_place[2]] == mark:
            return True


def win_move(i,board,mark):
    temp_board = list(board)
    temp_board[i] = mark
    if winning(mark,temp_board):
        return True
    else:
        return False


def cpu_input(cpu , human , board):
    print("Wait for CPU....",end="")
    print("\r", end="")
    time.sleep(1)

    for i in range(1,10):
        if board[i] == ' ' and win_move(i,board,cpu):
            return i
    for i in range(1,10):
        if board[i] == ' ' and win_move(i,board,human):
            return i
    for i in [5,1,9,3,2,7,8,6,4]:
        if board[i] == ' ':
            return i

def new_game():
    while True:
        nxt = input(f'[{man}] Do you want to play again?(y/n):')
        if nxt in['y','Y']:
            again = True
            break
        elif nxt in ['n','N']:
            print(f'Have a great day {man}.')
            again = False
            break
        else:
            print('Enter correct input')
    if again:
        print('__________NEW GAME__________')
        main_game()
    else:
        return False


def win_check(human , cpu):
    winning_place = [[1,2,3],[4,5,6],[7,8,9],[1,4,7],[2,5,8],[3,6,9],[1,5,9],[3,5,7]]
    for win_place in winning_place:
        if board[win_place[0]] == board[win_place[1]] == board[win_place[2]] == human:
            print(f'[{man}] wins the match!')
            if not new_game():
                return False
        elif board[win_place[0]] == board[win_place[1]] == board[win_place[2]] == cpu:
                print('[CPU] wins the match!')
                if not new_game():
                    return False
    if ' ' not in board:
        print('MATCH DRAW!!')
        if not new_game():
            return False
    return True


def user_choice():
    while True:
        inp = input(f'[{man}]Choose your mark[x/o]: ')
        if inp in ['x' , 'X']:
            print(f'[{man}]You choose "X".\n[{man}]You play first.')
            return 'x','o'
        elif inp in ['O','o']:
            print(f'[{man}] You choose "O".\n[{man}] CPU plays first.')
            return 'o','x'
        else:
            print(f'[{man}] Enter correct input!')


def main_game():
    global board
    global man 
    play = True
    board =['',' ',' ',' ',' ',' ',' ',' ',' ',' ']
    human , cpu = user_choice()
    display_board()
    while play:
        if human == 'x':
            x = human_input(human)
            board[x] = human
            display_board()
            play = win_check(human , cpu)
            if play:
                o = cpu_input(cpu , human , board)
                print(f'[CPU] Entered:{o}')
                board[o] = cpu
                display_board()
                play = win_check(human , cpu)
        else:
            x = cpu_input(cpu , human , board)
            print(f'[CPU] Entered:{x}')
            board[x] = cpu
            display_board()
            play = win_check(human , cpu)
            if play:
                o = human_input(human)
                board[o] = human
                display_board()
                play = win_check(human , cpu)


if __name__ == '__main__':
    man = input('Enter Your Name: ')
    print(f'Hello {man}!!!\n')
    print('How to paly :\n',15*' ','You need to choose your mark[x or o]. After that in your turn you have to chose a number for set your mark on an empty place in')
    print(12*' ','the game board which is not used by any of you. You can take help from reference board to know the value of your chosing position on the game board.')
    print(12*' ','And then wait a few second for CPUs turn.')
    print(12*' ','Reference board will be showed in each turn.')

    main_game()

