## 6.100A PSet 1: Part A
## Name:
## Time Spent:
## Collaborators:
    
## ------------------ Buying Dream House ----------------------- ##

 
##################################################################################
## Get user input for yearly_salary, portion_saved and cost_of_dream_home below ##
##################################################################################

## Take input yearly salary,portion saved,cost of dream home from <USER> ##

yearly_salary=float(input("What is your annual salary ? : "))
portion_saved=float(input("what percentage of your annual salary do you want to save ? : "))
cost_of_dream_home=float(input("How much does your deam house cost ? : "))

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

months=0
while amount_saved < portion_down_payment:
    amount_saved += amount_saved*(r/12) + (portion_saved*yearly_salary)/12
    months+=1
    
print("after",months,"months later you can buy your dream home !! :) ")