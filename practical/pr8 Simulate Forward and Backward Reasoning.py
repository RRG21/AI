"""
AI Practical-8.py
Simulate Forward and Backward Reasoning.
"""

# Forward reasoning
def forward_reasoning(symptoms):
    if 'fever' in symptoms and 'cough' in symptoms:
        return "flu"
    elif "fever" in symptoms:
        return "viral infection"
    else:
        return "no disease"

# Backward reasoning
def backward_reasoning(disease):
    if disease == "flu":
        return ["fever", "cough"]
    elif disease == "viral infection":
        return ["fever"]
    else:
        return []
print("Forward Reasoning:", forward_reasoning(["fever"]))
print("Backward Reasoning for viral infection:", backward_reasoning("viral infection"))