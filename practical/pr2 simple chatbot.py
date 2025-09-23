""" Dessin a simple rule-based
chatbot using if-else
Conditions (min 5 responses). """

"""
AI Practical 02.py
ChatBot
"""
try:
    User = ""
    while User != "exit":
        User = input("User: ").lower()
        if "exit" in User:
            print("Exiting ChatBot")
            break
        elif "hi" in User or "hello" in User:
            print("Bot: Hello User")
        elif "how are you" in User:
            print("Bot: I am fine")
        elif "your name" in User:
            print("Bot: My name is AI ChatBot")
        elif "your age" in User:
            print("Bot: I am 2 years old")
        elif "your purpose" in User:
            print("Bot: I am a chatbot, here to answer your questions.")
        elif "your creator" in User:
            print("Bot: My creator is RRG")
        elif "ai stands for" in User:
            print("Bot: AI stands for Artificial Intelligence")
        else:
            print("Bot: I do not understand.")
except:
    print("Invalid Input")
