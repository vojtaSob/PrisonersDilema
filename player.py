class MyPlayer:
    """Player plays cooperate if it is worth and opponent plays too, otherwise it plays dominant strategy"""

    myMoves = []
    opponentMoves = []
    dominantStrategy = bool
    round = 0

    def __init__(self, matrix, numOfGames=0):
        self.matrix = matrix
        self.numOfGames = numOfGames
        self.decide_dominant_strategy()

    def decide_dominant_strategy(self):
        """"Method looks what option can get more points in average"""

        cooperate_avg = (self.matrix[0][1][0] + self.matrix[0][0][0]) / 2
        defect_avg = (self.matrix[1][0][0] + self.matrix[1][1][0]) / 2
        if cooperate_avg < defect_avg:
            self.dominantStrategy = True
        else:
            self.dominantStrategy = False

    def move(self):
        """"Play cooperate when it is worth"""
        if self.round == 0 and self.matrix[0][0][0] >= self.matrix[1][1][0]:
            self.round += 1
            return False
        elif self.matrix[0][0][0] >= self.matrix[1][1][0] and self.round != 0 and not self.opponentMoves[
            len(self.opponentMoves) - 1]:
            self.round += 1
            return False

        return self.dominantStrategy

    def record_last_moves(self, my_last_move, opponent_last_move):
        self.myMoves.append(my_last_move)
        self.opponentMoves.append(opponent_last_move)
