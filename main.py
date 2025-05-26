# ==============================================
# Project Name:      OOP Retro Game – [Game Title]
# File Name:         main.py
# Author:            [Full Name]
# Class:             Year 11 Software Engineering
# Date Commenced:    DD/MM/YYYY
# Date Submitted:    DD/MM/YYYY
# GitHub Repo Link:  [URL if required]
# Description:       Entry point for game logic and main loop
# ==============================================

# Import custom classes
from player import Player
from obstacle import Obstacle
from game_manager import GameManager

def main():
    # Setup game environment and objects
    game = GameManager()
    game.run()

if __name__ == "__main__":
    main()
