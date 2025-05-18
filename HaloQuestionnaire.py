#Description
# This code is a Python script that implements a questionnaire for a Halo game.
#Askes you a series of questions to see if your a true halo fan. Point was to practice Nesting IF statements into my code to make it one level deeper of questions.

print("Let's find out if you're a HALO fan?")
print()

which_halo = input("Which Halo game is your favorite?: ").lower()

if which_halo == "halo 1":
    print("You are an OG of the game")
    print()
    print("No further questions for you")
elif which_halo == "halo 2":
    print("Had the best soundtrack and you could play as an Elite")
    print()
    name_of_elite = input("What was the name of the Elite you played as?: ").lower()
    if name_of_elite == "arbiter":
        print("Correct, you're a true fan.")
    else:
        print("Wrong answer, you're not a true fan")
elif which_halo == "halo 3":
    print("Had the best campaign of the series")
    print()
    print("My personal favorite out the whole series")
elif which_halo == "halo 4":
    print("Had the best multiplayer of the series")
elif which_halo == "halo 5":
    print("I liked the new movement system")
    print()
    which_team = input("Which team did you like the best? Blue Team or Fireteam Osiris: ").lower()
    if which_team == "blue team":
        print("You're a true fan, Master Chief is the GOAT!")
    elif which_team == "fireteam osiris":
        print("You're a true fan, more like an opp!")
    else:
        print("You're not a true fan")
else:
    print("You're not a true fan")