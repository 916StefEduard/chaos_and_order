class Controller:

    def __init__(self,board):
        self.__board=board

    def __print_menu(self):
        print('\n')
        print('1.New Game.')
        print('2.Load Game.')
        print('3.exit')

    def __ui_move(self):
        row=int(input("row="))
        column=int(input("column="))
        return row,column

    def __ui_command(self):
        print('Save game')
        print('1)Yes or 2)No!!')

    def human_vs_computer(self):
        first_done=False
        while not first_done:
            self.__print_menu()
            command=input(">>>>")
            if command=='3':
                first_done=True
            else:
                if command=='2':
                    self.__board.read_file()
                second_done=False
                human_turn =1
                while not second_done:
                    print(self.__board)
                    if human_turn==1:
                        row,column=self.__ui_move()
                        self.__board.move_player(row, column, 'X')
                        self.__ui_command()
                        input_command = input(">>>")
                        if input_command == '1':
                            self.__board.load_data()
                    else:
                        self.__board.move_computer()
                    if self.__board.is_game_won()==True:
                            second_done=True
                            print(self.__board)
                            print('Game is won!!')
                    if self.__board.is_board_full()==True:
                            second_done=True
                            print(self.__board)
                            print("Board is full,chaos wins!!")
                    human_turn=-1*human_turn



