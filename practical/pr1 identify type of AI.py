# Write A Program to identify types of AI (narrow,general,super) based on user input description : 

#input from user
desc=input("Enter the description of AI: ")

#condition
if "specific task" in desc or "one task" in desc:
    print("Narrow AI (ANI:artifical narrow intelligence)")
elif "multi-task" in desc or "human-like" in desc :
    print("General AI (AGI:artifical general intelligence)")
elif "superior to human" in desc:
    print("Super AI (ASI: artifical super intelligence)")
else :
    print("Type of AI could not be determined")