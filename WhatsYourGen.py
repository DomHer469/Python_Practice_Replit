#DESCRIPTION:
#Wrote a simple Python program that identifies which generation you belong to based on your birth year 👶📅👴
#The script takes user input, compares the year against known generational ranges, and responds with a personalized message. Great way to practice using if/elif/else statements and user interaction!

print("What generation are you a part of?")

name = input("Enter your name: ")
year = int(input("Enter your birth year: "))
print()

if year >= 1925 and year <= 1946:
    print("You are a Traditionalist,", name) 
elif year >= 1947 and year <= 1964:
    print("You are a Baby Boomer,", name)
elif year >= 1965 and year <= 1981:
    print("You are a Generation X,", name)
elif year >= 1982 and year <= 1995:
    print("You are a Millennial,", name)
elif year >= 1996 and year <= 2015:
    print("You are a Generation Z,", name)
else: 
    print("Are you sure your not a time traveler,", name)
    print("You are not a part of any generation,", name)
    print("You are a part of the future,", name)