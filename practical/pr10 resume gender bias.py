"""
AI Practical-10.py
resume gender bias
"""

resume=input ("Paste resume text here: ").lower()

if "he " in resume or "she " in resume or "male " in resume or "female " in resume:
    print("Potential gender bias detected in Resume.")
else:
    print("no gender bias detected.")