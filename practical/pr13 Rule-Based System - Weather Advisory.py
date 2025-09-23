"""
AI Practical-13.py
Rule-Based System:Weather Advisory
"""

def weather_advice(weather):
    if weather == "rainy":
        return "Carry an umbrella."
    elif weather == "sunny":
        return "Wear sunglasses."
    elif weather == "cloudy":
        return "You may need a light jacket."
    else :
        return "No specific advice."

print(weather_advice(input("Enter weather: ")))