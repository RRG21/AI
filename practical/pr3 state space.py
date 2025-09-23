"""
Write a program to take a user
problem (e.g. travel route)
and display state-space
representation.
"""

states = {
    "Home" : ["Bus stop"],
    "Bus stop" : ["Station", "college","Home"],
    "Station" : ["Bus stop"],
    "College" : []
}

print("staate-Space Representation of a problem")

for state in states:
    print(f"{state} -> {states[state]}")