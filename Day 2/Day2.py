# final project

print("\nWelcome to the tip Calculator\n")

total_bill = float(input("What was the total bill?\n- "))

tip = int(input("\nHow much tip would you like to give? 10, 12 or 15?\n- "))

people = int(input("\nHow many people to split the bill?\n- "))

total_inlucding_tip = total_bill + (total_bill * (tip / 100));

final_bill = total_inlucding_tip / people;

print(f"Each person should pay: {round(final_bill,2)}");









