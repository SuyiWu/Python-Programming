## Yuwen(Suyi)Wu Homework 3 (A16770560)

##Part A

Variable = "v"
numberV = input('How many waves would you like to ride?\n>>')
intNum = int(numberV)

i = 0
while i < intNum:
    print(Variable,end = '')
    i+=1
input()

##Part B

selectLetter = input('Please select a letter\n>>')
guess=['a','r','t','l','m','x','z']

for element in guess:
    if element != selectLetter:
        print('Computer guesses',element)
        print('The computer is wrong')
    else:
        print('Computer guesses',element)
        print('The computer is wins!')
        break

input()
       
##Part C

    
correctPassword = 'Beauvoir'
passwordEnter = input('Please enter the password:\n>>')
wrongPassword = []

while passwordEnter != correctPassword:
    wrongPassword.append(passwordEnter)
    if len(wrongPassword) == 3:
        
        print('Access denied')
        break
    elif len(wrongPassword) == 2:
        passwordEnter = input('That is incorrect, please try again(1 attempts left)\n>>')
    elif len(wrongPassword) == 1:
        passwordEnter = input('That is incorrect, please try again(2 attempts left)\n>>')
        
     
else:
    passwordEnter == correctPassword
    print ('Access granted')

input()

##Part D


price = 20
priceOffer = input('How much will you pay?\n>>')
floatPriceOffer = float(priceOffer)
i=0
while floatPriceOffer < price:
    price += 1
    i+=1
    print('Nope! Try offering more:\n>>')
    priceOffer = input('How much will you pay?\n>>')
    floatPriceOffer = float(priceOffer)
else:
    print('It\'s a deal! The price is',price,'\n>>')

    
originalPrice = price - i
print('You overpaid by',i,'I was originally willing to sell for',originalPrice,'\n>>')
    

   
    

    


