#Just built a fun little Python program that simulates splitting a dinner bill at a fancy birthday dinner 💸🍽️
#The script uses conditional logic to suggest a tip based on the bill total, lets the user customize the tip percentage, and then calculates how much each person owes based on the group size.

print("""Think of this sernario: you're at a fancy restaurant for your birthday and you have all your friedns around you. y'all are loving the vibes and the food. Everything is great. Then BOOM the check comes in, the server couldn't divide the check so its all on one. You have to pay for it but you tell your friends to Zelle you back.""")
print()

myBill = float(input("How much was the bill?: $"))
print()


if myBill >= 1000:
  print("Wow, that's a lot of money!")
  print()
  print("You should probably tip 20%.")
  print()
  FixedTipRate = input("Would you like to tip 20%? (yes/no): ")
  print()
  if FixedTipRate == "yes":
    TipAmount = myBill * 0.20
    TotalBill = myBill + TipAmount
  else:
    AskTipAmount = int(input("How much would you like to tip? (whole number): "))
    ConvertToDecimal = AskTipAmount / 100
    TipAmount = myBill * ConvertToDecimal
    TotalBill = myBill + TipAmount


else:
  print("ohh that's a reasonable amount of money.")
  print()
  print("You should probably tip 15%.")
  print()
  FixedTipRate = input("Would you like to tip 15%? (yes/no): ")
  print()
  if FixedTipRate == "yes":
    TipAmount = myBill * 0.15
    TotalBill = myBill + TipAmount
  else:
    AskTipAmount = int(input("How much would you like to tip? (whole number): "))
    ConvertToDecimal = AskTipAmount / 100
    TipAmount = myBill * ConvertToDecimal
    TotalBill = myBill + TipAmount


print()
numberOfPeople = int(input("How many people are at your dinner?: "))
answer = TotalBill / numberOfPeople
print()
print("You all owe $" + str(int(answer)) + " EACH!")