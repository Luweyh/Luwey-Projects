# Author: Luwey Hon
# Date: 3/1/20
# Description: This program plays the Tic Tac Toe game.
# It will consist of a 3x3 board and move a current state.

class TicTacToe:
    """ This class represents the Tic Tac Toe game """

    def __init__(self):
        """ Initializes the board and current state"""
        self._current_state = 'UNFINISHED'
        self._board = [['' for _ in range(3)] for _ in range(3)]

    def get_current_state(self):
        """ Gets the current state"""
        return self._current_state

    def print_state(self):
        print(self._current_state)

    # printing board for debugging purposes
    def print_board(self):
        """ Prints the board out"""
        for row in self._board:
            print(row)

    def make_move(self, row, column, player):
        """ This functions makes the move for the Tic Tac Toe game"""

        # check to make sure game is not finished
        if self._current_state != 'UNFINISHED':
            return False

        # check to make sure valid index
        if not (0 <= row <= 2) or not (0 <= column <= 2):
            return False

        # check to make sure player is valid
        if player != 'x' and player != 'o':
            return False

        # check to make sure a spot isn't occupied
        if self._board[row][column] != '':
            return False

        # makes the move for the play
        self._board[row][column] = player

        # runs the check for winner function
        self.check_for_winner()

        return True

    def check_for_winner(self):
        """ This checks for the winning combinations """

        # check for row wins
        for row in self._board:
            if row[0] == row[1] == row[2] == 'x':
                self._current_state = 'X_WON'
                return
            if row[0] == row[1] == row[2] == 'o':
                self._current_state = 'O_WON'
                return

        # check columns wins
        for i in range(3):
            if self._board[0][i] == self._board[1][i] == self._board[2][i] == 'x':
                self._current_state = 'X_WON'
                return

            if self._board[0][i] == self._board[1][i] == self._board[2][i] == 'o':
                self._current_state = 'O_WON'
                return

        # check for diagonal win going top left to bottom right
        if self._board[0][0] == self._board[1][1] == self._board[2][2] == 'x':
            self._current_state = 'X_WON'
            return

        if self._board[0][0] == self._board[1][1] == self._board[2][2] == 'o':
            self._current_state = 'O_WON'
            return

        # checks for diagonal win going top right to bottom left
        if self._board[0][2] == self._board[1][1] == self._board[2][0] == 'x':
            self._current_state = 'X_WON'
            return

        if self._board[0][2] == self._board[1][1] == self._board[2][0] == 'o':
            self._current_state = 'O_WON'
            return

        # check for draw
        for row in self._board:
            for i in range(3):
                if row[i] == '':
                    return
        self._current_state = 'DRAW'

# The code below is for debugging purposes


if __name__ == '__main__':
    ttt = TicTacToe()
    # ttt.check_for_winner()

    while 1:
        row = int(input('Row input:'))
        col = int(input('Col input:'))
        player = input('Player:')
        ttt.make_move(row, col, player)
        ttt.print_board()
        ttt.print_state()
