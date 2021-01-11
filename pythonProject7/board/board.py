import random

class Board:

    def __init__(self,file_name):
        self.__file_name=file_name
        self.__board=[['🔲' for j in range(6)]for i in range(6)]

    def get_slot(self,x,y):
        return self.__board[x][y]

    @staticmethod
    def input_validator(row, column):
        if int(row) > 0 and int(row) <= 6 and int(column) > 0 and int(column) <= 6:
            return True
        return False

    def move_player(self, row, column, char):
        if self.input_validator(row,column)==True:
            if self.__board[row-1][column-1]=='🔲':
                self.__board[row-1][column-1]=char
            else:
                print('Slot already taken')
        else:
            print('Move not allowed')

    def is_game_won(self):
        for row in range(6):
            for column in range(0,2):
                if self.__board[row][column] != '🔲':
                    if self.__board[row][column] == self.__board[row][column + 1] == self.__board[row][column + 2]  == self.__board[row][column + 3]==self.__board[row][column + 4]:
                        return True

        for row in range(6):
            for column in range(3):
                if self.__board[column][row] != '🔲':
                    if self.__board[column][row] == self.__board[column + 1][row] == self.__board[column + 2][row] == self.__board[column + 3][row]== self.__board[column + 4][row]:
                        return True

        for row in range(3):
            for column in range(4):
                if self.__board[row][column] != '🔲':
                    if self.__board[row][column] == self.__board[row + 1][column + 1] == self.__board[row + 2][column + 2] == self.__board[row + 3][column + 3]==self.__board[row + 4][column + 4]:
                        return True

        for row in range(2):
            column = 5
            while column > 2:
                if self.__board[row][column] != '🔲':
                    if self.__board[row][column] == self.__board[row + 1][column - 1] == self.__board[row + 2][column - 2] == self.__board[row + 3][column - 3]==self.__board[row + 4][column - 4]:
                        return True
                column -= 1

        return False


    def move_computer(self):
        i=-1
        j=-1
        choices=[1,2,3,4,5,6]
        while self.input_validator(i,j)!=True or self.__board[i-1][j-1]!='🔲':
            i=random.choice(choices)
            j=random.choice(choices)

        for row in range(6):
            for column in range(0, 2):
                if self.__board[row][column] != '🔲':
                    if self.__board[row][column] == self.__board[row][column + 1] == self.__board[row][column + 2] == self.__board[row][column + 3]:
                        if self.__board[row + 4][column + 4] == '🔲':
                                i=row+1
                                j=column+5

        for row in range(6):
            for column in range(3):
                if self.__board[column][row] != '🔲':
                    if self.__board[column][row] == self.__board[column + 1][row] == self.__board[column + 2][row] == self.__board[column + 3][row]:
                        if self.__board[row + 4][column + 4] == '🔲':
                            i = column+5
                            j = row+ 1

        for row in range(3):
            for column in range(4):
                if self.__board[row][column] != '🔲':
                    if self.__board[row][column] == self.__board[row + 1][column + 1] == self.__board[row + 2][column + 2] == self.__board[row + 3][column + 3]:
                        if self.__board[row + 4][column + 4] == '🔲':
                            i = row + 4
                            j = column + 4

        for row in range(2):
            column = 5
            while column > 2:
                if self.__board[row][column] != '🔲':
                    if self.__board[row][column] == self.__board[row + 1][column - 1] == self.__board[row + 2][column - 2] == self.__board[row + 3][column - 3]:
                        if self.__board[row+3][column-3] == '🔲':
                            i = row+3
                            j = column-3
                column -= 1

        self.move_player(i,j,'O')

    def load_data(self):
        with open(self.__file_name,"w") as file:
            for i in range(6):
                for j in range(6):
                    slot=self.__board[i][j]
                    if slot=="🔲":
                        file.write('t')
                    elif slot=="O":
                        file.write('O')
                    else:
                        file.write('X')
                file.write("\n")

    def read_file(self):
        with open(self.__file_name,"r") as file:
            i=0
            lines = file.readlines()
            for line in lines:
                for j in range(6):
                    if line[j]=='t':
                        self.__board[i][j]="🔲"
                    elif line[j]=='O':
                        self.__board[i][j]="O"
                    else:
                        self.__board[i][j]='X'
                i+=1

    def is_board_full(self):
        for i in range(6):
            for j in range(6):
                if self.__board[i][j]=='🔲':
                    return False
        return True


    def __str__(self):
        string='----------------\n'
        for i in range(6):
            for j in range(6):
                string+='|'
                string+=str(self.__board[i][j])
            string+='\n'
            string+='----------------\n'
        return string

