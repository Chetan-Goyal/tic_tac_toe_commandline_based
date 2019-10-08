from config import *  # for default values for our program
import random        # for making the toss
import time         # for sleep() function

class tic_tac_toe:

    def __init__(self):
        '''
        Initializing the Toss,choosing winner,assigning symbol and turn
        Variables Assigned Here: symbol(list) , turn(list)
        '''
        print('Welcome Champions\n')
        time.sleep(2)
        print('''Here are the instructions about the game:
        1. Toss will be entirely based on random value generated by the computer
        2. Toss Winner will get first turn with choice to choose between 'O' and 'X' 
        3. Position of move would be like - (row_number)(column_number) eg- 13 (1st row and 3rd column)

        Let's get started!!!
        ''')
        winner = random.randint(0,1)  # Toss
        time.sleep(5)
        if(winner == 0): # when player A wins
            print('Player A won the Toss')
        else: # when player B wins
            print('Player B won the Toss')

        symbol[winner] = input('Please choose your symbol(O or X): ') 
        
        # assigning turn to the winner
        if(winner == 0):
            turn[0] = True
            symbol[1] = ''.join([sy for sy in ['O','X'] if sy != symbol[winner] ])
        else:
            symbol[0] = ''.join([sy for sy in ['O','X'] if sy != symbol[winner] ])
            turn[1] = True
    
    def doing_turn(self):
        '''
        1. If user chooses an invalid box id, asking him to do again
        2. Updating the move of the Player in the list
        3. Reversing the turns of the Players
        '''

        # informing Players about the turn
        if(turn[0] == True):
                print('\nPlayer A is going to make a move')
        else:
            print('\nPlayer B is going to make a move')

        i = int(input('Enter the box id: '))

        # checking if player entered a reserved index
        if(  l[int(i/10)][i%10] != None  ):
            print('Try Again')
            self.doing_turn()
        else: # if not
            if(turn[0] == True):  # if it is Player A's turn 
                l[int(i/10)][i%10] = symbol[0]
            else:    # if it is Player B's turn 
                l[int(i/10)][i%10] = symbol[1]

        #reverting the turns
        turn[0] = not turn[0]
        turn[1] = not turn[1]


    def printing(self):
        '''
        Printing the tic tac toe board
        '''
        for i in range(nor):
            for j in range(noc):
                if(l[i][j]):
                    print(str(l[i][j]).center(5),end='')
                else:
                    print(' '*5,end='')
                if(j != noc-1):
                    print('|',end='')
            print()
            if(i!=nor-1):
                print( (noc*5 + 2)*'-')
        print('\n')
    
    def return_nor(self):
        # returning number of rows
        return nor

    def return_noc(self):
        # returning number of columns
        return noc
    
    def winner_check(self):
        '''
            Use       : Checking whether any player won the game and returning the Symbol of the winner
        
        Variables Used: 1. d_1 and d_2 representing diagonal element 
                        2. d1_won and d2_won representing whether diagonal contains same element 
                        3. flag_r and flag_c representing whether a row or column contains same element
        '''

        '''
        Checking if any player won Diagonally
        '''
        d_1 = l[0][0]
        d_2 = l[noc-1][0]
        d1_won, d2_won = True, True
        
        # diagonal-> top-left  to  bottom-right
        for i in range(nor):
            if(l[i][i] != d_1):
                d1_won = False
                break
        if(d1_won == True):
            return d_1
        
        # diagonal-> top-right to botton-left
        i, j = 0, noc-1
        while j >= 0:
            if(l[i][j] != d_2):
                d2_won = False
                break
            i += 1
            j -= 1
        if(d2_won == True):
            return d_2
        
        '''
        1. If player didn't won diagonally
        2. Checking if any Player won row-wise or column-wise
        '''
        for i in range(nor):
            r, c = l[i][0], l[0][i]
            flag_r, flag_c = True, True

            for j in range(noc):
                if(l[i][j] != r and flag_r):
                    flag_r = False
                if(l[j][i] != c and flag_c):
                    flag_c = False
            
            # returning the symbol of the winning Player
            if(flag_r == True):
                return l[i][j]
            elif(flag_c == True):
                return l[j][i]
            
        return None # if there is no win

def result_calculator(result, n):
    '''
    Checking whether it's draw(returns D) or a winner(returns winner code( A or B))
    '''
    if(result == None and n != nor*noc-1):
        return None
    elif(result == None and n == nor*noc-1):
        return 'D'
    elif(result == symbol[0]):
        return 'A'
    elif(result == symbol[1]):
        return 'B' 

