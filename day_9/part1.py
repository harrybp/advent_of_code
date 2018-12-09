import numpy as np

last_marble = 72058
players = 426

player_scores = np.zeros(players)
game_board = []
current_marble = 0
current_player = 0


for marble in range(last_marble+1):
    if len(game_board) > 0:
        current_marble = (current_marble + 2) % len(game_board)
    if marble % 23 == 0 and len(game_board) > 0:
        current_marble = (current_marble - 9) % len(game_board)
        player_scores[current_player] += marble + game_board[current_marble+1]
        game_board = game_board[:current_marble+1] + game_board[current_marble+2:]
    else:
        game_board = game_board[0:current_marble+1] + [marble] + game_board[current_marble+1:]
    current_player = (current_player + 1) % players

best_score = 0
for score in player_scores:
    if score > best_score:
        best_score = score

print(best_score)