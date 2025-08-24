"""
description: Create a class Ghost
    Ghost objects are instantiated without any arguments.
    Ghost objects are given a random color attribute of "white" or "yellow" or "purple" or "red" when instantiated
site: Codewars
link: https://www.codewars.com/kata/53f1015fa9fe02cbda00111a
comments: Aug.23.2025 - This is a test for VSCode and GitHub integration. 
    We are solving a kata (practice problem) from Codewars and commting it to GitHub using VSCode.
"""

import random

class Ghost:
    def __init__(self):
        self.color = random.choice(["white","yellow","purple", "red"])

# Example usage:
g1 = Ghost()
g2 = Ghost()

print(g1.color)
print(g2.color)  