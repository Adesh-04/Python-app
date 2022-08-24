## Board Setup:
## 1. Put white corner in right side
## 2. Put Pawns in second and seventh rank
## 3. Put Rooks in the corner
## 4. Put Knights and Bishops
## 5. Put Queen on their color i.e. white Q on white square
## 6. Put King on remaining Tile


## result [0][0][x]   for rounding up see in display()
##        [0][0][x]
##        [x][x][x]

class Chess:
    def __init__(self):
        self.rank = 8  ## [1,2,3,4,5,6,7,8]
        self.file = 8
        self.file_notation = ['0','H','G','F','E','D','C','B','A']
        self.board = self.createBoard()
        self.side = 'White'
        self.move_count = 0

    def createBoard(self):
        ## Ranks are horizontal and Files are Vertical
        ## +1 for rounding up indexes as ranks
        return [ ['00']*(self.rank+1) for _ in range(self.file+1) ]

    def putPieces(self):
        ## board[rank][file]
        ## Put Pawns
        for file in range(1,self.rank+1):
            self.board[2][file] = 'WP'
            self.board[7][file] = 'BP'

        ## Put Rooks
        self.board[1][1],self.board[1][8] = 'WR','WR'
        self.board[8][1],self.board[8][8] = 'BR','BR'

        ## Put Knights
        self.board[1][2],self.board[1][7] = 'WN','WN'
        self.board[8][2],self.board[8][7] = 'BN','BN'

        ## Put Bishops
        self.board[1][3],self.board[1][6] = 'WB','WB'
        self.board[8][3],self.board[8][6] = 'BB','BB'

        ## Put Queen and King
        self.board[1][4],self.board[1][5] = 'WK','WQ'
        self.board[8][4],self.board[8][5] = 'BK','BQ'

    def take_input(self):
        var = input("{}'s Move :".format(self.side))
        var = list(var)
        return self.move(var)

    def move(self,arr):
        if arr:
            ## E5 have [file][rank]
            if len(arr) == 2:
                if arr[0] in self.file_notation and int(arr[1]) < self.rank:
                    self.move_pawn(arr)

    def move_pawn(self,arr):
        rank_index = int(arr[1]) 
        file_index = self.file_notation.index(arr[0])
        print(self.board[rank_index][file_index])  ## Getting Location
        
        

    def display(self):
        print('\n\t   *** Black Side ***')
        for i in range(8,0,-1):
            print('',end='\n')
            for j in range(8,0,-1):
                print('|',self.board[i][j],'|',end='')
            print('   {}'.format(i),end='')
        print('\n\n  A{s}B{s}C{s}D{s}E{s}F{s}G{s}H  '.format(s='     '))
        print('\n\t   *** White Side ***\n')


if __name__ == '__main__':

    obj = Chess()
    obj.putPieces()
    obj.display()
    obj.take_input()


