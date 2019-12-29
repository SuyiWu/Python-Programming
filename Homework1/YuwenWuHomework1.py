# Yuwen(Suyi) Wu Homework 1 (A16770560)

distance = input('How far will you run?\n>>')
speed = input('How fast will you run per mile (please enter decimal, like 7.5 for 7:30 pace)\n>>')

distancefloat = float(distance)
speedfloat = float(speed)

time = distancefloat * speedfloat
timeString = str(time)
decimal = timeString.index('.')

timeSubString = timeString[:decimal+4]

print('It will take you',timeSubString,'minutes to run',distance,'\n')


principle = input('Please enter principle:\n>>')
interestRate = input('Please enter annual interest rate(example 5.2 for 5.2%)\n>>')
term = input('Please enter the term in years:\n>>')
compound = input('Please enter number of times the interest will compound per year:\n>>')

floatPrinciple = float(principle)
floatInterestRate = float(interestRate)
floatTerm = float(term)
floatCompound = float(compound)

futureValue = floatPrinciple*((1+floatInterestRate/100/floatCompound)**(floatCompound*floatTerm))
futureValueString = str(futureValue)
decimal = futureValueString.index('.')
futureValueStringSubString = futureValueString[:decimal+3]
paidInterest = futureValue - floatPrinciple
paidInterestString = str(paidInterest)
decimalInterest = paidInterestString.index('.')
paidInterestSubString = paidInterestString[:decimal+3]

print('In',floatTerm,'years, at the interest rate of',interestRate+'%','compounded',compound,'times per year, the initial amount of','$'+str(floatPrinciple),'will be worth','$'+futureValueStringSubString+'.','$'+paidInterestSubString,'will be paid in interest.')
      
