#Asks the user to enter their annual salary.
print(">>>\nEnter your annual salary: ")
annual_salary = input()
annual_salary = float(annual_salary) 

#Asks the user to enter their annual salary.
print("Enter the percent of your salary to save, as a decimal: ")
portion_saved = input()
portion_saved = float(portion_saved)

print("Enter the cost of your dream home: ")
total_cost = input()
total_cost = float(total_cost)

portion_down_payment = 0.25

current_savings = 0

r = 0.04

monthly_salary = annual_salary/12

down_payment = portion_down_payment * total_cost

counter = 0;

while current_savings < down_payment:
  current_savings += (current_savings*r/12) + (portion_saved*monthly_salary)
  counter += 1

print("Number of months: "+ str(counter) + "\n>>>")