# Ask user for the type of year
year_type = input("Are you asking for a Normal year or a Leap year? (Normal/Leap): ").lower()

# Calculate seconds based on year type
if year_type == "normal":
    days = 365
    seconds = days * 24 * 60 * 60
    print(f"There are {seconds:,} seconds in a Normal year.")
elif year_type == "leap":
    days = 366
    seconds = days * 24 * 60 * 60
    print(f"There are {seconds:,} seconds in a Leap year.")
else:
    print("Invalid input. Please enter either 'Normal' or 'Leap'.")