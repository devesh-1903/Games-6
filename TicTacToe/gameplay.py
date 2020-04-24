
from math import inf as infinity
import time


class game:
    def __init__(self, mode, p1):
        # self.grid=[['1','2','3'],['4','5','6'],['7','8','9']]
        self.grid = [['  ', '  ', '  '], [
            '  ', '  ', '  '], ['  ', '  ', '  ']]
        self.playing = True
        self.turn = 1
        self.mode = mode
        self.stat = "Player1 turn "
        self.winner = None

        self.available = [(0, 0), (0, 1), (0, 2), (1, 0),
                          (1, 1), (1, 2), (2, 0), (2, 1), (2, 2)]

        if p1 == 1:
            self.marker = ['', 'X', 'O']
        else:
            self.marker = ['', 'O', 'X']
        self.scores = {self.marker[1]: 1, self.marker[2]: -1, 'tie': 0}
        print(self.scores['X'])

    def minimax(self, board, depth, ismaximizing):

        self.check_winner()
        if self.winner != None:
            return self.scores[self.winner]
        if ismaximizing:
            best_score = -infinity
            for i in range(3):
                for j in range(3):
                    if board[i][j] == '  ':
                        board[i][j] = self.marker[2]
                        score = self.minimax(board, depth+1, False)
                        board[i][j] = "  "
                        best_score = max(score, best_score)
            return best_score
        else:
            best_score = infinity
            for i in range(3):
                for j in range(3):
                    if board[i][j] == "  ":
                        board[i][j] = self.marker[1]
                        score = self.minimax(board, depth+1, True)
                        board[i][j] = '  '
                        best_score = min(score, best_score)
            return best_score

    def ai_update(self, i, j):

        if (i, j) in self.available:
            if self.turn == 2:
                # turn_value=False
                self.grid[i][j] = self.marker[1]
                self.status("Computer turn")
                self.available.remove((i, j))
                self.turn = 1
        if self.turn == 1:
            best_score = -infinity
            for i in range(3):
                for j in range(3):
                    if self.grid[i][j] == "  ":
                        self.grid[i][j] = self.marker[2]
                        score = self.minimax(self.grid, 0, False)
                        self.grid[i][j] = '  '

                        if score > best_score:
                            best_score = score
                            a = (i, j)

            self.grid[a[0]][a[1]] = self.marker[2]
            # self.available.remove(a)
            self.status("Player1 turn")
            self.turn = 2

    def update(self, j, i):
        if (j, i) in self.available:
            if self.turn == 1:
                self.grid[j][i] = self.marker[1]
                self.status("Player2 turn")
                self.turn = 2
            else:
                self.grid[j][i] = self.marker[2]
                self.status("Player1 turn")
                self.turn = 1
            self.available.remove((j, i))
            self.check_winner()

    def status(self, msg):
        # try to keep message len between 8 to 12
        self.stat = msg

    def the_winner(self, win):
        if win == 't':
            self.status('Its a Tie!')
        # for pvp
        if self.mode == 1:
            if self.marker[1] == win:
                self.status('Player1 Won')
            elif self.marker[2] == win:
                self.status('Player2 Won')
        elif self.mode == 2:
            if self.marker[1] == win:
                self.status('Player1 Won')
            elif self.marker[2] == win:
                self.status("Computer Won")

    def check_winner(self):
        # across
        for i in range(3):
            if (self.grid[i][0] == self.grid[i][1] == self.grid[i][2]) and self.grid[i][0] != '  ':
                self.winner = self.grid[i][0]
                self.the_winner(self.grid[i][0])
                self.playing = False
        # down
        for i in range(3):
            if (self.grid[0][i] == self.grid[1][i] == self.grid[2][i]) and self.grid[i][i] != '  ':
                self.winner = self.grid[0][i]
                self.the_winner(self.grid[0][i])
                self.playing = False
        # diagnal
        if (self.grid[0][0] == self.grid[1][1] == self.grid[2][2])and self.grid[0][0] != '  ':
            self.winner = self.grid[1][1]
            self.the_winner(self.grid[1][1])
            self.playing = False

        if (self.grid[2][0] == self.grid[1][1] == self.grid[0][2])and self.grid[1][1] != '  ':
            self.winner = self.grid[1][1]
            self.the_winner(self.grid[1][1])
            self.playing = False

        # tie
        if len(self.available) == 0 and self.winner == None:

            self.winner = 'tie'
            self.the_winner('t')
            self.playing = False
