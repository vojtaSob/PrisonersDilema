# This script creates two (identical) players, 
# lets them play for some number of iterations and 
# then displays their scores. 
#
# For running this script, you need to put the 'game.py'
# as well as your 'player.py' to the python path, e.g. 
# to the the working directory. 
#
# A very simple testing script, feel free to modify it
# according to your needs
#
# example code for students of B4B33RPH course
# Author: Tomas Svoboda, and the RPH team

from game import Game

# assuming your player is in player.py as required
# https://cw.fel.cvut.cz/wiki/courses/b4b33rph/cviceni/veznovo_dilema/specifikace
import player

# define the payoff matrix; see game.py for detailed explanation of this matrix
payoff_matrix = (((4, 4), (1, 6)), ((6, 1), (2, 2)))

# define the number of iterations
number_of_iterations = 20

# create the players
playerA = player.MyPlayer(payoff_matrix)
# at the moment, me and the opponent are of the same type
playerB = player.MyPlayer(payoff_matrix)

# create the game instance
my_game = Game(playerA, playerB, payoff_matrix, number_of_iterations)
# run game
my_game.run()

# get scores 
scores = my_game.get_players_payoffs()

# display scores
print('playerA got:', scores[0], '\nplayerB got:', scores[1])
