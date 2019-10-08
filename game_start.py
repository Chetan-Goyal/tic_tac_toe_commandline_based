from main import tic_tac_toe as ttt
from main import result_calculator

def main():
    game1 = ttt() # making a class instance
    n = 0 # setting the turn number initially as 0

    while n < game1.return_nor()*game1.return_noc(): # checking if turn number is in the range (0,nor*noc)
        n += 1
        game1.doing_turn() # invoking doing_turn() function to take a move
        game1.printing()  # printing the current structure of our game
        result_symbol = game1.winner_check()  # if winner found, getting the symbol of the winner
        result = result_calculator(result_symbol,n) # for draw, D / winning of Player A, A/ winning of player B
        if(result == None):
            continue
        elif(result == 'D'):
            print("It's a draw")
            break
        else:
            print('Player ' + result + ' Won the Game')
            break

if __name__ == '__main__':
    main()