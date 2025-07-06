"""
Create a program that asks the user for a number and then prints out a list of all the divisors of that number. 
divisor = 26 / 13 = 2 (no remainder = divisors)
"""

num = int(input("Enter a number: "))
new_list = []

for i in range(1, num+1):
    if num % i == 0:
        new_list.append(i)
print(new_list)
