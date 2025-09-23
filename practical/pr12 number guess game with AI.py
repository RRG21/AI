"""
AI Practical-12.py
number guess game with AI
"""

import random

low = 1
high = 100
feedback = ""
print("Think of a number between 1 and 100. I will guess it!")

while feedback != "correct":
    guess = random.randint(low, high)
    print(f"My guess is : {guess}")
    feedback = input("Too high (h), too low (l), or correct (c)? ")

    if feedback == "h":
        high = guess - 1
    elif feedback == "l":
        low = guess + 1
print("AI guessed the number correctly!") 