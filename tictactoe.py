import random


class Player:
    
    def __init__(self, num):
        self.name = input('Player ' + str(num) + ', please enter your name: ')
        self.symb = input(self.name + ', please choose your symbol: ')

class TicTacToe:
    
    def __init__(self):
        self.board = []
    
    def setup_board(self):
        for i in range(3):
            row = ['-','-','-']
            self.board.append(row)
    
    def display_board(self):
        for row in self.board:
            for item in row:
                print(item, end='  ')
            print()
    
    def starting_player(self):
        return random.randint(0,1)

    def place_symbol(self,symbol,row,column):
        self.board[row][column] = symbol
    
    def is_game_won(self, symbol):
        win = None

        n = len(self.board)

        # checking rows
        for i in range(n):
            win = True
            for j in range(n):
                if self.board[i][j] != symbol:
                    win = False
                    break
            if win:
                return win

        # checking columns
        for i in range(n):
            win = True
            for j in range(n):
                if self.board[j][i] != symbol:
                    win = False
                    break
            if win:
                return win

        # checking diagonals
        win = True
        for i in range(n):
            if self.board[i][i] != symbol:
                win = False
                break
        if win:
            return win

    def is_game_draw(self):
        for row in self.board:
            for item in row:
                if item == '-':
                    return False
        return True

    def game_start(self):
        message = '''
    #########  #    ####      #########    #       ####      #########    ####    #####
        #      #   #              #       # #     #              #       #    #   #
        #      #   #     ####     #      #   #    #     ####     #       #    #   #####
        #      #   #              #     # ### #   #              #       #    #   #
        #      #    ####          #    #       #   ####          #        ####    #####
    '''
        print(message)
        print('############################################################################################')
        print('#  Welcome to Tic-Tac-Toe. This game is created and maintained by GitHub user philipp-jo.  #')
        print('############################################################################################')

        # init players
        player1 = Player(1)
        player2 = Player(2)
        
        # init gameboard
        self.setup_board()
        self.display_board()

        # determine starting player
        player_symb = player1.symb if self.starting_player == 1 else player2.symb
        player_name = player1.name if self.starting_player == 1 else player2.name

        while True:
            print('{player}\'s turn.'.format(player=player_name))
            self.display_board()

            # player should place their symbol at free location
            while True:
                row, column = list(map(int, input(player_name + ", please enter row and column numbers to fix spot: ").split()))
                if self.board[row-1][column-1] == '-':
                    self.place_symbol(player_symb, row-1, column-1)
                    break

            # check if current player has won
            if self.is_game_won(player_symb):
                print(player_name + ' has won the game!')
                break

            # check if game is draw (board full)
            if self.is_game_draw():
                print('It\'s a draw!')
                break

            # switch player if not won or draw
            if player_name == player1.name and player_symb == player1.symb:
                player_name = player2.name
                player_symb = player2.symb
            else:
                player_name = player1.name
                player_symb = player1.symb
        print()
        self.display_board()


game = TicTacToe()
game.game_start()