#DESCRIPTION:

# I had a sample of code I needed to debug.
# Heres the Before and After

#Before

# print("100 Days of Code QUIZ")
# print()
# print("How many can you answer correctly?)
# ans1 = ("What language are we writing in?")
# if ans1 == "python":
#   print("Correct")
# else:
#   print("Nope🙈
# ans2 = input("Which lesson number is this?")
# if(ans2>12):
# print("We're not quite that far yet")
# else:
#  print("We've gone well past that!")
# elif(ans2==12):
#   print("That's right!")


#After

print()
print("How many can you answer correctly?")
print()
ans1 = input("What language are we writing in? ").lower()
if ans1 == "python":
    print("Correct")
else:
    print("Nope🙈")
print()
while True: 
    ans2 = int(input("Which lesson number is this? "))
    if(ans2==12):
        print("That's right!")
        break
    elif(ans2>12):
        print()
        print("You think your so advanced huh?")
        print("Try again")
        print()
    else:
        print()
        print("We've gone well past that!")
        print("We're not quite that far yet")
        print()