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

##################################################################################################
## Determine the lowest rate of return needed to get the down payment for your dream home below ##
##################################################################################################

def is_less(amount_saved_after_36_months):
    if amount_saved_after_36_months<(portion_down_payment-100):
        return True
    else: return False


def Enough(amount_saved_after_36_months):
    if (portion_down_payment-100) <= amount_saved_after_36_months <= (portion_down_payment+100):
        return True
    else: return False


def Answer(r,amount_saved):
     for month in range(1,37):
         amount_saved+=initial_deposit*(1+r/12)**month
     amount_saved_after_36_months=amount_saved
     if Enough(amount_saved_after_36_months):
         return "Acceptable"
     elif is_less(amount_saved_after_36_months):
         return "Less_than"
     
def Acceptable_r(high,low):
     global steps
     steps+=1
     r=(low+high)/2.0
     if Answer(r,amount_saved)== "Acceptable":
         return r
     elif Answer(r, amount_saved)=="Less_than":
         low=r
         return Acceptable_r(high, low)
     else:
         high=r
         return Acceptable_r(high, low)