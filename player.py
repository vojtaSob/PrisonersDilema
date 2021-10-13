class MyPlayer:
    myMoves = []
    opponentMoves = []

    def __init__(self, matrix, numOfGames=0):
        self.matrix = matrix
        self.numOfGames = numOfGames

    def move(self):
        return True

    def record_last_moves(self, my_last_move, opponent_last_move):
        self.myMoves.append(my_last_move)
        self.myMoves.append(opponent_last_move)
