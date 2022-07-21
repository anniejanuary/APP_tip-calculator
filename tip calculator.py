print("Welcome to the tip calculator for all your tip calculating needs!")
bill=float(input("Enter the amount on the bill: "))
number_of_people=int(input("How many people to split between?: "))
percentage=float(input(f"Enter the tip amount - 10, 12 or 15 (%): "))
percentage_format=1 + percentage * 0.01

total_per_person=bill/number_of_people*percentage_format
total_per_person_format="{:.2f}".format (total_per_person)
print(f"The bill and the {percentage} % tip split {number_of_people} ways is: {total_per_person_format}")
