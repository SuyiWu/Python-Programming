## YuwenWu Homework 4 (A16770560)

##Part A

name = input("What's your name?\n>>")

def happyBirthday(name):
   
    print("Happy Birthday to you,\nHappy Birthday to you,\nHappy Birthday, dear",name,"\nHappy Birthday to you!")

happyBirthday(name)


##Part B

def futureValue(p,r,t,n = 365):
    pFloat = float(p.replace('$','').replace(',',''))
    rFloat = float(r.replace('%',''))*0.01
    a = pFloat*(1+rFloat/n)**(n*t)
    return a


futureValue1 = futureValue('$5,000','%7.9',5)
print(futureValue1)
futureValue2 = futureValue('$12,000','%3.2',10)
print(futureValue2)
futureValue3 = futureValue('$1700,000','%4.8',30,4)
print(futureValue3)
  

