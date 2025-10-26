from random import choice
from os import makedirs
noun1:str = input("Enter a noun: ")
verb:str = input("Enter a verb: ")
noun2:str = input("Enter a noun: ")
stories = [
    f"One day, a {noun1} decided to {verb} the {noun2}. Everyone in town still talks about that day!",
    f"Two {noun1}s entered a coffee shop with a {noun2} and {verb}ed",
    f"Fortnite {noun1}, I'm {noun2}, I love {verb}ing"       
           ]
makedirs("madlibs", exist_ok=True)
storyFile="madlibs/stories.txt"
option = choice(stories)
with open(storyFile, "a") as file:
    file.write(option + "\n")
    

print(option)