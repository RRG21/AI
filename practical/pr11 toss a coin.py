"""
AI Practical-11.py
toss a coin
"""

import random
def toss_coin():
    return "Heads" if (random.choice([0,1]) == 0) else "Tails"

print("Toss Result: ",toss_coin())  