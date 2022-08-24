## Board Setup:
## 1. Put white corner in right side
## 2. Put Pawns in second and seventh rank
## 3. Put Rooks in the corner
## 4. Put Knights and Bishops
## 5. Put Queen on their color i.e. white Q on white square
## 6. Put King on remaining Tile


class Chess:
    def __init__(self):
        self.rank = 8
        self.file = 8
        self.board = self.createBoard()
        self.side = 'White'
        self.move_count = 0

    def createBoard(self):
        ## Ranks are horizontal and Files are Vertical
        return [ [0]*self.rank for _ in range(self.file) ]

    def putPieces(self):
        ## Put Pawns
        for file in range(self.rank):
            self.board[1][file] = 'P'
            self.board[6][file] = 'P'

        ## Put Rooks
        self.board[0][0],self.board[0][7] = 'R','R'
        self.board[7][0],self.board[7][7] = 'R','R'

        ## Put Knights
        self.board[0][1],self.board[0][6] = 'N','N'
        self.board[7][1],self.board[7][6] = 'N','N'

        ## Put Bishops
        self.board[0][2],self.board[0][5] = 'B','B'
        self.board[7][2],self.board[7][5] = 'B','B'

        ## Put Queen and King
        self.board[0][3],self.board[0][4] = 'K','Q'
        self.board[7][3],self.board[7][4] = 'K','Q'

    def display(self):
        ## To Display the board
        print('\n\t *** Black Side ***')
        for ele in self.board:
            print('',end='\n')
            for i in ele:
                print('| {val} |'.format(val = str(i)),end='')
        print('\n\n\t *** White Side ***\n')

    def take_input(self):
        var = input("{}'s Move :".format(self.side))
        return var

    def move(self,var):
        print(var)

if __name__ == '__main__':

    obj = Chess()
    obj.putPieces()
    obj.display()
    obj.take_input()


