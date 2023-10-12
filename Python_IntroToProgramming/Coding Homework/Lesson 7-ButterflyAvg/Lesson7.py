# This program represents butterflies collected in a day
# Inputs: Butterflies/Days
# Outputs: Total butterflies/ avg 
# Written by: Jose Gonzalez
# Modified Date: Feb 13, 2020

#start
print ("Welcome to the Butterfly Collecting Program\n Enter the amount collected on each day\n Enter -1 when finished\n")
#Beginning variables
days = 0
total= 0
average= 0
butterflies= 0

#Loop
while (butterflies >=0 ):
    butterflies = int(input("Enter the number of Butterflies for day {} (or -1 to end):".format(days +1)))
    total= total + butterflies 
    days= days +1 
    if(butterflies ==-1):
        days= days-1
        total= total+1
        break


print("\n Here are the resulults of your butterfly collecting!")
 
# Calculation and Final output
if days>0:
    average= total/days
    print ("Total bugs collected:", total)
    print("Average bugs collected per day:",average)
else: 
    print("You have entered no butterfly data")