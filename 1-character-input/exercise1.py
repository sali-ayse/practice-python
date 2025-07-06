"""
Create a program that asks the user to enter their name and their age. 
Print out a message addressed to them that tells them the year that they will turn 100 years old
"""

print("Let's calculate what year you'll be turning 100 years old")

age = int(input("What's your age?"))

current_year = 2025

birth_res = current_year - age
res = birth_res + 100

print("You will be turning 100 in year: ", res)
