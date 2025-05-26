# ==============================================
# Project Name:      OOP Retro Game – [Game Title]
# File Name:         player.py
# Author:            [Full Name]
# Description:       Defines the Player class and player actions
# ==============================================

class Player:
    def __init__(self, name="Player1", position=(0, 0)):
        self.name = name
        self.position = position
        self.lives = 3
        self.score = 0

    def move(self, direction):
        # Example: update player position based on direction
        print(f"{self.name} moves {direction}")

    def reset_position(self):
        self.position = (0, 0)
