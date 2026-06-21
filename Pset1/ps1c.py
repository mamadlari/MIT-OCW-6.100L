## 6.100A PSet 1: Part C
## Name:Mohammad Tolooei
## Time Spent:3
## Collaborators:No One

##############################################
## Get user input for initial_deposit below ##
##############################################

initial_deposit=float(input("whats is your initial amount in your savings account ? : "))

#########################################################################
## Initialize other variables you need (if any) for your program below ##
#########################################################################

cost_of_dream_home= 800000.0
portion_down_payment=0.25*cost_of_dream_home
steps=0
months=36

##################################################################################################
## Determine the lowest rate of return needed to get the down payment for your dream home below ##
##################################################################################################


def Enough(amount_saved_after_36_months):
    """ 
     Checks amount_saved_after_36_months is Acceptable or not
     
     Parameters:
         
         amount_saved_after_36_months (float):The user's savings
         with compound interest after 36 months.
         
     Globals:
         
         portion_down_payment (float): Down payment for buing a house.
         
     Returns (string):
         
         Acceptable :if amount_saved_after_36_months fall
         with in down payment range.
         
         less_than :if amount_saved_after_36_months less than
         with in down payment range.
         
         more_than :if amount_saved_after_36_months more than
         with in down payment range.
    """    
    if (portion_down_payment-100) <= amount_saved_after_36_months <= (portion_down_payment+100):
        return "Acceptable"
    elif amount_saved_after_36_months < (portion_down_payment-100):
        return "less_than"
    else: return "more_than"

def Answer(r):
     """
     Checks amount_saved_after_36_months with compound interest formula is enough or not
    
     Parameters:
        
        r (float):Annual interest rate
        
     Globals:
         
         amount_saved_after_36_months(float):The user's savings
         with compound interest after 36 months.
         
     Returns (string):
         
         Returns the return value of a function.
         Enough(amount_saved_after_36_months)
         
     """
     amount_saved_after_36_months=initial_deposit*(1+(r/12))**months
     return Enough(amount_saved_after_36_months) 
     
def Acceptable_r(high,low,steps):

     """
     Find the acceptable annual interest rate (r) recursively by bisections search
     
     Parameters:
         
         high (float):The highest range in bisection search
         
         low (float):The lowest range in bisection search
         
         steps (int):Number of function executions
         
     Globals:
         
         initial_deposit (float):Initial account balance
         
         portion_down_payment (float):Down payment for buing a house.
         
         r (float): Annual interest rate (guess)
         
         ans (string): The return value of a Answer(r) funcction
         
     Returns (a tuple):
         
         (r,steps):("The acceptable anuual interest rate" , "number of function executions")
     """
     steps+=1
     r=(low+high)/2.0
     ans=Answer(r)
     match ans:
         case "Acceptable":
             return (r,steps)
         case "less_than":
             low=r
             return Acceptable_r(high, low,steps)
         case "more_than":
             high=r
             return Acceptable_r(high, low,steps)
         case _:
             return (None,steps)
         
  
if initial_deposit>=portion_down_payment:
   (r,steps)=(0.0,steps)
   print("r = ",r,"and steps in bisections search is : ",steps)
elif Answer(1)=="less_than":
    (r,steps)=(None,steps)
    print("r = ",r,"and steps in bisections search is : ",steps)
else:
    (r,steps)=Acceptable_r(1.0, 0.0,steps)
    print("r = ",r,"and steps in bisections search is : ",steps)
