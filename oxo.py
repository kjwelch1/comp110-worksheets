class OxoBoard:
    def __init__(self, x, y):

        self.Board = {(0, 0): 0, (1, 0):0, (2, 0):0, (0, 1):0, (1, 1):0, (2, 1):0, (0, 2):0, (1, 2):0, (2, 2):0}

    def get_square(self, x, y):

        return self.Board[x,y]

    def set_square(self, x, y, mark):

        if self.Board[x, y] == 0:
            self.Board[x, y] = mark
            return True

        else:
            return False

    def is_board_full(self):

        SquareSearch = 0
        for x in xrange(0, 3):

            for y in xrange(0, 3):

                if self.Board[x, y] > 0:
                    SquareSearch += 1

                if SquareSearch == 9:
                    return True

                elif [x, y] == (2, 2):
                    return False

    def get_winner(self):

        if self.Board[1,1] !=0:

            if self.Board[0,0] == self.Board[1,1]:

                if self.Board [2,2] == self.Board[1,1]:
                    return current_player


            if self.Board [2,0] == self.Board[1,1]:

                if self.Board [0,2] == self.Board[1,1]:
                    return current_player

        for i in xrange (0,3):

            if self.Board [0,i] != 0:

                if self.Board [0,i] == self.Board [1,i]:

                    if self.Board [0,i] == self.Board [2,i]:
                        return current_player

            if self.Board [i,0] != 0:

                if self.Board [i,0] == self.Board [i, 1]:

                    if self.Board [i,0] == self.Board [i,2]:
                        return current_player
        return 0
    def show(self):
        """ Display the current board state in the terminal. You should not need to edit this. """

        for y in xrange(3):

            if y > 0:
                print "--+---+--"

            for x in xrange(3):

                if x > 0:
                    print '|',

                # Print a space for empty (0), an O for player 1, or an X for player 2
                print " OX"[self.get_square(x, y)],
            print


def input_square():
    """ Prompt the player to enter a square. You should not need to edit this. """
    while True:
        input = raw_input("Enter x,y where x=0,1,2, y=0,1,2: ")
        if input.count(',') != 1:
            print "Input must contain exactly one comma!"
            continue

        x, y = input.split(',')
        try:
            x = int(x)
            y = int(y)
        except ValueError:
            print "Input must be two numbers separated by a comma!"
            continue

        if x < 0 or x > 2 or y < 0 or y > 2:
            print "Input is out of bounds!"
            continue

        return x, y


# The main game. You should not need to edit this.
if __name__ == '__main__':
    board = OxoBoard()
    current_player = 1
    while True:
        board.show()
        print "Choose a square, Player", current_player
        x, y = input_square()

        if board.set_square(x, y, current_player):
            # Move was played successfully, so check for a winner
            winner = board.get_winner()
            if winner != 0:
                print "Player", winner, "wins!"
                break   # End the game
            elif board.is_board_full():
                print "It's a draw!"
                break   # End the game
            else:
                # Switch players
                if current_player == 1:
                    current_player = 2
                else:
                    current_player = 1
        else:
            # Move was not played successfully
            print "That square is already filled!"
