#Code to determine if the Year is a leap year or not.
Year=2020
#Year is the variable.  The value is 2020. 
if Year%4==0:
#This determines if the Year value is divisible by 4.  If it is, it goes to the next line's prompt.  If it is not, it goes down to the "else" inline with it below that will print it isn't a leap year.
	if Year%100==0:
	#This determines if the year is divisible by 100 after it has been cleared by the above command that is it divisable by 4.  If it is, it goes to the next line's prompt.  If it is not, it goes down the the else inline with it below that will print it is a leap year.
		if Year%400==0:
		#If the value has cleared the above 2 prompts, it will go to this line to see if it is divisible by 400.  It if is, it will print that it is a leap year. If it is not, it goes down to the "else" inline with it below that will print it isn't a leap year.
			print('Year is a leap year')
		else:
			print('Year is not a leap year')
	else:
		print('Year is a leap year')
else:
	print('Year is not a leap year')