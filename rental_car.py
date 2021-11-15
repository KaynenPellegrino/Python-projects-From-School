import sys
'''
Section 1: Collect customer input
'''



dailyCharge = 60.00

#I am not entirely understanding what I am supposed to comment. I have read the syllabus
#several times over, not sure still. I also had a lot of trouble with this whole project.
#I did a lot of googling to find what I needed to get the floating numbers.
#But here's a shot at the commenting.
#
#my if and elif statements branched constantly, so if a D was shown as the active rentalCode
#there was an automatic switch without much need to go around and double check. I did comment
#each individual section so I can find whatever section is needed. 


#Customer Rental Data
rentalCode = input("(B)udget, (D)aily, or (W)eekly rental?")
print ('')

#the rental code is predetermined by customer input, should they be daily, weekly, or
#budget renters.

if rentalCode == 'D':
  rentalPeriod = input("Number of Days Rented:\n")
elif rentalCode == 'W':
  rentalPeriod = input ("Number of Weeks Rented:\n")
  
  
if rentalCode == 'B':
  baseCharge = "{:.2f}".format(int(rentalPeriod) * int(budgetCharge))
elif rentalCode == 'W':
  baseCharge = "{:.2f}".format(int(rentalPeriod) * int(weeklyCharge))
elif rentalCode == 'D':
  baseCharge = "{:.2f}".format(int(rentalPeriod) * int(dailyCharge))
  
#Customer Usage Data
odoStart = input("Starting Odometer Reading:")
print('')
odoEnd = input("Ending Odometer Reading:")
print('')

totalMiles = int(odoEnd) - int(odoStart)

#the odoStart command will display the miles on the odometer when the customer picked up the
#vehicle, and the odoend is the miles on the odometer at drop off. totalmiles, obviously
#is the amount of miles they put on, which they are charged for if deemed necessary based on
#type of rental and the distance they drove.

averageDayMiles = "{:.2f}".format(int(totalMiles)/ int(rentalPeriod))
averageWeekMiles = "{:.2f}".format(int(totalMiles)/ int(rentalPeriod))
extraMiles = float(averageDayMiles) - 100

#customer charges and costs

if rentalCode == 'B':
  mileCharge = "{:.2f}".format(int(totalMiles) * 0.25)
elif rentalCode == 'D':
  if float(averageDayMiles) > 100:
    mileCharge = float(extraMiles) * 0.25
  elif averageDayMiles <= 100:
    mileCharge = 0.00
elif rentalCode == 'W':
  if averageWeekMiles <= 900:
    mileCharge = 0.00
  elif averageWeekMiles > 900:
    mileCharge = "{:.2f}".format(100.00 * int(rentalPeriod))

#I had a bit of trouble with the amtDue, it kept coming out as 324.25 on the project,
#but I eventually got it to 324.4. Unfortunately, that also wasn't correct, it needed to be
#324.40. I finally found out how to do that through so extensive googling. But, that didn't 
#work at the end either. I had to find a dozen work arounds.    
    
amtDue = float(baseCharge) + (mileCharge)
formatted_amtDue = "{:.2f}".format(amtDue)

#customer Rental Summary

print('Rental Summary')
print('Rental Code:','', '', '', '', '', '', '', rentalCode)
print('Rental Period:','', '', '', '', '', '', '', rentalPeriod)
print('Starting Odometer:', '', odoStart)
print('Ending Odometer:', '', '', '', odoEnd)
print('Miles Driven:', '', '', '', '', '', '', totalMiles)
print('Amount Due:', '', '', '', '', '', '', '', '', '$' + str(formatted_amtDue))

#this was one of the most tedious parts. I had to find the right amount of spaces in order
#to make the code come out the way that Codio wanted, and jeeez that was bothersome.
#But, after about 5 minutes of just doing spaces, I figured it out. 