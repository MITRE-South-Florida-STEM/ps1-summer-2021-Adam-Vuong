print(">>>\nEnter your annual salary: ")
annual_salary = input()
annual_salary = int(annual_salary)

portion_saved = 0.04

total_cost = 1000000

semi_annual_rate = 0.07

portion_down_payment = 0.25

current_savings = 0.0

r = 0.04

months_salary = annual_salary/12

down_payment = portion_down_payment * total_cost

investment_return = r

tolerance = 100
steps = 0
high = 10000.0
low = 0.0
guess = (high+low)/2.0
total_salaries = 0.0
tolerance = down_payment/100
def calculateSavings(current_savings,months_salary,guess,month):
    for months in range(0,37):
        if  months%6==1 and months >1:
            months_salary=months_salary*(1+semi_annual_rate)
        current_savings = current_savings + months_salary * guess
    current_savings = current_savings * (1+0.04)
    return(current_savings)

while abs(current_savings-down_payment)>=100:
    current_savings = calculateSavings(current_savings,months_salary,guess,1)
    if  current_savings < down_payment:
        low = guess
        current_savings = 0.
    elif current_savings > down_payment + tolerance:
        high = guess
        current_savings = 0.
    if (steps > 36):
        print("It is not possible to pay the down payment in three years.")
        break
    guess = (low+high)/2
    steps += 1
  
if(guess > 1.0):
  print("It is not possible to pay the down payment in three years.\n>>>")
else:
  print("Best savings rate: " + str(guess) + "\nSteps in bisection search: " + str(steps) + "\n>>>") 
# Steps and rates may be off, I have to test the search algorithm a bit more.
