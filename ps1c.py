## 6.100A PSet 1: Part C
## Name:
## Time Spent:
## Collaborators:

##############################################
## Get user input for initial_deposit below ##
##############################################

initial_deposit=float(input("whats is your initial amount in your savings account ? : "))

#########################################################################
## Initialize other variables you need (if any) for your program below ##
#########################################################################

cost_of_dream_home= 800000.0
portion_down_payment=0.25*cost_of_dream_home
amount_saved=0.0
steps=0
months=36
##################################################################################################
## Determine the lowest rate of return needed to get the down payment for your dream home below ##
##################################################################################################

def Enough(amount_saved_after_36_months):
    
    if (portion_down_payment-100) <= amount_saved_after_36_months <= (portion_down_payment+100):
        return "Acceptable"
    elif amount_saved_after_36_months < (portion_down_payment-100):
        return "less_than"
    else: return "more_than"

def Answer(r,amount_saved):
    
     amount_saved_after_36_months=initial_deposit*(1+(r/12))**months
     return Enough(amount_saved_after_36_months) 
     
def Acceptable_r(high,low):
    
     if initial_deposit>=portion_down_payment:
        return 0.0
     global steps
     steps+=1
     r=(low+high)/2.0
     ans=Answer(r, amount_saved)
     if steps==30:
         exit()
     match ans:
         case "Acceptable":
             return r
         case "less_than":
             low=r
             return Acceptable_r(high, low)
         case "more_than":
             high=r
             return Acceptable_r(high, low)
         case _:
             return None

r=Acceptable_r(1.0, 0.0)
print("r = ",r,"and steps in bisections search is : ",steps)