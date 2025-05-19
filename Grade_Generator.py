#DESCRIPTION:

#Get test information from user and store in variables.
#This section prompts the user to input:
#1. The name of their test (stored as string)
#2. The total number of questions on the test (stored as float)
#3. The number of questions answered correctly (stored as float)
#These inputs are used later to calculate the percentage score and determine the letter grade.

# Get test information from user
test_name = input("Enter the name of your test: ")
max_score = float(input("Enter how many questions there was: "))
user_score = float(input("Enter how many you got right: "))

# Calculate percentage
percentage = (user_score / max_score) * 100
percentage = round(percentage, 2)

# Determine letter grade
if percentage >= 90:
    letter_grade = "A+"
elif percentage >= 80:
    letter_grade = "A"
elif percentage >= 70:
    letter_grade = "B"
elif percentage >= 60:
    letter_grade = "C"
elif percentage >= 50:
    letter_grade = "D"
else:
    letter_grade = "F (Did you study, or did you just Netflix and chill?)"

# Display results
print(f"\nTest: {test_name}")
print(f"Your percentage: {percentage}%")
print(f"Your grade: {letter_grade}")