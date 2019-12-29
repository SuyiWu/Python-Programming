## Yuwen(Suyi)Wu Homework2


## Part A
maximumAmount = 500
priceDemanded = input('How much are you asking?\n>>')
floatPriceDemanded = float(priceDemanded)
if floatPriceDemanded  > 500:
    print('Sorry, that price is too high for me.')
else:
    print('Ok, I would like to purchase it.')
    
input()

## Part B

print('Welcome to the currency calculator')
amount = input('Enter the amount:\n>>')
fromCurrency = input('Enter the from currency:\n>>')
floatAmount = float(amount)
convertedAmount = input('Enter the to currency:\n>>')
usDollar = ['Dollar','dollar','DOLLAR','$']
japaneseYen = ['Yen','yen','YEN','¥']
europeanEUR = ['EURO','Euro','euro','€']
ukPound = ['pound','POUND','Pound','£']

if fromCurrency in usDollar and convertedAmount in japaneseYen:
    print(floatAmount,'dollar(s) is worth',floatAmount*112.04,'Yen(s)')
elif fromCurrency in usDollar and convertedAmount in europeanEUR:
    print(floatAmount,'dollar(s) is worth',floatAmount*0.86,'Euro(s)')
elif fromCurrency in usDollar and convertedAmount in ukPound:
    print(floatAmount,'dollar(s) is worth',floatAmount*0.76,'Pound(s)')    
elif fromCurrency in japaneseYen and convertedAmount in usDollar:
    print(floatAmount,'Yen(s) is worth',floatAmount*0.0089,'Dollar(s)')   
elif fromCurrency in japaneseYen and convertedAmount in europeanEUR:
    print(floatAmount,'Yen(s) is worth',floatAmount*0.007680,'EUR(s)')
elif fromCurrency in japaneseYen and convertedAmount in ukPound:
    print(floatAmount,'Yen(s) is worth',floatAmount*0.006830,'Pound(s)')
elif fromCurrency in europeanEUR and convertedAmount in usDollar:
    print(floatAmount,'EUR(s) is worth',floatAmount*1.16,'Dollar(s)')
elif fromCurrency in europeanEUR and convertedAmount in japaneseYen:
    print(floatAmount,'EUR(s) is worth',floatAmount*130.21,'Yen(s)')
elif fromCurrency in europeanEUR and convertedAmount in ukPound:
    print(floatAmount,'EUR(s) is worth',floatAmount*0.89,'Pound(s)')
elif fromCurrency in ukPound and convertedAmount in usDollar:
    print(floatAmount,'Pound(s) is worth',floatAmount*1.31,'Dollar(s)')
elif fromCurrency in ukPound and convertedAmount in japaneseYen:
    print(floatAmount,'Pound(s) is worth',floatAmount*146.52,'Yen(s)')
else:
    print(floatAmount,'Pound(s) is worth',floatAmount*1.12,'EUR(s)')

input()

                      
