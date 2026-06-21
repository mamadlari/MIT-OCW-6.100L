def part_a(yearly_salary, portion_saved, cost_of_dream_home):
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
	    
	print("after",months,"months later you can buy your dream home !! :) ")
	return months