#1 DATA TYPES
len("1")

print(type(False))

#2 TYPE ERROR, CHECKING AND CONVERSION
# print(type("Holas vienen, holas van"))
# print(type(len("12345")))
# print(type(1.2))
# print(type(1<2))

# print(int("123") + int("456"))

username = input("Enter your name\n")
length_of_name = len(username)

print("Number of letters in your name: " + str(length_of_name))

#3 MATHEMATICAL OPERATIONS
print("My age: " + str(12))
print(123 + 456)
print(7 - 3)
print(3 * 2)
print(6 / 3)
print(5 / 3)
print(5 // 3)
print(2**2)
print(2**3)

print(3*(3+3)/3-3)

#4 NUMBER MANIPULATION
# bmi = 84 / 1.65 ** 2
# print(bmi)
# print(int(bmi))
# print(round(bmi))
# print(round(bmi, 1))

# score = 0
#
# score += 1
# print(score)
# score -= 2
# print(score)

#f-string
score = 0
height = 1.8
is_winning = True
print(f"Your score is = {score}, your height is {height}. You're winning is {is_winning}")

#5 TIP CALCULATOR PROJECT
print("Welcome to the tip calculator!")
bill = float(input("What was the total bill?\n$"))
tip = int(input("What percentage tip would you like to give? \nFor example: 10%, 12%, 15%... "))
people = int(input("How many people to split the bill? \n"))
# tip_per_person = (bill / people) * round(tip/100 + 1, 2)
# print(f"Each person should pay: ${tip_per_person}")
tip_as_percent = tip/100
total_tip_amount = bill * tip_as_percent
total_bill = bill + total_tip_amount
bill_per_person = total_bill / people
final_amount = round(bill_per_person, 2)
print(f"Each person should pay: ${final_amount}")