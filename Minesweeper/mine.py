import random

def display(board):
    ## To Display the board
    val = 0
    for ele in board:
        val+=1
        print('',end='\n')
        for i in ele:
            print('| {val} |'.format(val = str(i)),end='')
        print('  {}'.format(val),end='')


def board(num):
    ## Returns the board
    return [[0]*num for i in range(num)]

def dummy(num):
    ## Returns the dummy board
    return [['-']*num for i in range(num)]
    
def put_mines(board,num):
    ## Mine Count
    mine_count = num+ (num//2)

    ## Random Mines
    for i in range(0,mine_count):
        ran = random.randrange(0,num)
        ran1 = random.randrange(0,num)
        board[ran][ran1] = 'X'
    return board    
        
def put_mark(board,num,win):
    ## Iterate through all elements of the board
    for index1,i in enumerate(board):   ## [][][x][]
        for index2,j in enumerate(i):   ## [ ,x, , ,]
            if j:
                continue
            else:
                ## Top , Bottom, Left, Right
                if index1 - 1 >= 0:                          
                    if board[index1 -1][index2] == 'X':
                        j+=1
                if index1 + 1 < num:                        
                    if board[index1 +1][index2] == 'X':
                        j+=1
                if index2 - 1 >= 0:                          
                    if board[index1][index2 - 1] == 'X':
                        j+=1
                if index2 + 1 < num:
                    if board[index1][index2 + 1] == 'X':
                        j+=1

                ## NorthWest, NorthEast, SouthWest, SouthEast
                if index1 - 1 >= 0 and index2 - 1 >= 0:
                    if board[index1 - 1][index2 - 1] == 'X':
                        j+=1
                if index1 - 1 >= 0 and index2 + 1 < num:
                    if board[index1 - 1][index2 + 1] == 'X':
                        j+=1
                if index1 + 1 < num and index2 - 1 >= 0:
                    if board[index1 + 1][index2 - 1] == 'X':
                        j+=1
                if index1 + 1 < num and index2 + 1 < num:
                    if board[index1 + 1][index2 + 1] == 'X':
                        j+=1
                if j > 0:
                    ## If Mines Nearby, used for win condition
                    win.append((index1,index2))

            ## Assign Nearby Mine Count
            board[index1][index2] = j
    return board,win

def take_input():
    val = input('\n\t row:')
    ## try for only int values
    try:
        val = int(val)
        if val > 0 and val <= num:
            val2 = input('\t column:')
            val2 = int(val2)
            if val2 <= 0 or val2 > num:
                print('Invalid')
            else:
                return (val,val2)
        else:
            print('Invalid')
        
    except:
        print('Invalid')

def check(board,inData,val,win_condition):
    ## Reduced by 1 becoz of index 0
    try:
        x = val[0] - 1
        y = val[1] - 1
    except:
        return inData,False

    ## Checking for Mine
    if board[x][y] == 'X':
        inData[x][y] = 'x'
        ## Returning Data and lose condition
        return inData,True
    else:
        inData[x][y] = board[x][y]
        win_condition.remove((x,y))
        if win_condition:
            return inData,False
        else:
            return inData,'Done'
        

if __name__ == '__main__':
    win_condition = []  ## Keeps the Record of Indexes of Safe and Counted Places
    num = 10            ## Dimension
    win = board(num)    
    inData = dummy(num)
    win = put_mines(win,num)
    win,win_condition = put_mark(win,num,win_condition)

    # display(win) ## For Debugging


    while True:
        display(inData)
        
        values = take_input()
        inData,is_finished = check(win,inData,values,win_condition)
        if is_finished == True:
            display(inData)
            print('\n\n\t*** Game OVER ***\n')
            display(win)
            break
        elif is_finished == 'Done':
            display(inData)
            print('\n\n\t *** Victory ***\n\n')
            break
        # print(win_condition) ## For Debugging
        
   

    