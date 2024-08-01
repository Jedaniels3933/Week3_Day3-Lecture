import re 
names = ["Abraham Lincoln", "Andrew P Garfield", "peter pan", "Connor Milliken", "Jordan Alexander Williams", "Madonna", "programming is cool"]

def JD():
    for name in names:
        if re.match(r"(^[A-J]{1})", name):
            print(f" {name} is Valid")
        else:
            print(f" {name} is Invalid")