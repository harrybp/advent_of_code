import numpy as np
from datetime import datetime
start_time = datetime.now()



class GameBoard():
    def __init__(self, value):
        self.current_marble = LinkedList(value)
        self.current_marble.next = self.current_marble
        self.current_marble.previous = self.current_marble
        self.length = 1
    def insert_marble(self, value):
        self.current_marble = self.current_marble.next
        self.current_marble = self.current_marble.next
        new_node = LinkedList(value)
        new_node.previous = self.current_marble
        new_node.next = self.current_marble.next
        self.current_marble.next.previous = new_node
        self.current_marble.next = new_node
        self.length += 1
    def mod_23(self):
        for i in range(6):
            self.current_marble = self.current_marble.previous
        score = self.current_marble.value
        next_marble = self.current_marble.next
        self.current_marble = self.current_marble.previous
        self.current_marble.next = next_marble
        next_marble.previous = self.current_marble
        self.length -= 1
        return score
    def print(self, reverse=False):
        x = 0
        node = self.current_marble
        nodes = []
        while x < self.length:
            nodes.append(node.value)
            if reverse:
                node = node.previous
            else:
                node = node.next
            x += 1
        print(nodes)

class LinkedList():
    def __init__(self, value):
        self.value = value
        self.next = None
        self.previous = None

last_marble = 72058 * 100
players = 426
player_scores = np.zeros(players)
current_player = 1
game_board = GameBoard(0)
for marble in range(1,last_marble+1):
    if marble % 23 == 0:
        score = game_board.mod_23()
        player_scores[current_player] += marble + score
    else:
        game_board.insert_marble(marble)
    current_player = (current_player + 1) % players
    

best_score = 0
for score in player_scores:
    if score > best_score:
        best_score = score

print(best_score)
time_elapsed = datetime.now() - start_time
print(time_elapsed)