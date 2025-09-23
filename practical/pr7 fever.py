"""
AI Practical-07.py
Write a mini knowledge base using if-else rules (e.g., Disease Diagnosis based on symptoms).
"""
fever=input("Do you have fever? (yes/no): ").lower()
cough=input("Do you have cough? (yes/no): ").lower()

if fever=="yes" and cough=="yes":
    print("You have a fever and cough. You may have a flu.")
elif fever=="yes" and cough=="no":
    print("You have a fever. You may have a flu.")
elif fever=="no" and cough=="yes":
    print("You have a cough. You may have a cold.")
else:
    print("You have no fever, cough. You may not have a flu.")