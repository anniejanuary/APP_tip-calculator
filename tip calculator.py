print("Welcome to the tip calculator for all your tip calculating needs!")
bill = float (input ("Enter the amount on the bill: ") )
number_of_people = int (input ("How many people to split between?: ") )
percentage = float (input (f"Enter the tip amount - 10, 12 or 15 (%): ") )
percentage_format = 1 + percentage * 0.01  #  or w/o this and instead: total_bill = percentage * bill + bill

total_per_person = bill / number_of_people * percentage_format
total_per_person_format = round(total_per_person,2)
#  OR:                  = "{:.2f}".format(total_per_person) -- if I really care about seeing '0' in the 2nd decimal point, eg. 33.60
print(f"The bill and the {percentage} % tip split {number_of_people} ways is: {total_per_person_format}")
