# ==============================================
# Project Name:      OOP Retro Game – [Game Title]
# File Name:         obstacle.py
# Author:            [Full Name]
# Description:       Base class for obstacles (e.g. cars, logs)
# ==============================================

class Obstacle:
    def __init__(self, obstacle_type="Car", speed=1, position=(0, 0)):
        self.obstacle_type = obstacle_type
        self.speed = speed
        self.position = position

    def move(self):
        # Basic movement logic
        print(f"{self.obstacle_type} moves at speed {self.speed}")
