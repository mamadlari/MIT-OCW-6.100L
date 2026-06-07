## 6.100A PSet 1: Part B
## Name:
## Time Spent:
## Collaborators:

##########################################################################################
## Get user input for yearly_salary, portion_saved, cost_of_dream_home, semi_annual_raise below ##
##########################################################################################

## Take input yearly salary,portion saved,cost of dream home,semi annual raise from <USER> ##

yearly_salary=float(input("What is your annual salary ? : "))
portion_saved=float(input("what percentage of your annual salary do you want to save ? : "))
cost_of_dream_home=float(input("How much does your deam house cost ? : "))
semi_annual_raise=float(input("What percentage of your annual salary will be paid to you after 6 months ? : "))

#########################################################################
## Initialize other variables you need (if any) for your program below ##
#########################################################################

## Initialize  house down payment , interest and monthly saving ##

portion_down_payment=0.25*cost_of_dream_home
amount_saved=0.0
r=0.05

###############################################################################################
## Determine how many months it would take to get the down payment for your dream home below ## 
###############################################################################################

## Calculating monthly savings ##

months=0
while amount_saved < portion_down_payment:
    amount_saved += amount_saved*(r/12) + (portion_saved*yearly_salary)/12
    months+=1
    
## Salary incease every 6 months ##
    
    if months%6 == 0 :
        yearly_salary+=(semi_annual_raise*yearly_salary)
    
print("after",months,"months later you can buy your dream home !! :) ")