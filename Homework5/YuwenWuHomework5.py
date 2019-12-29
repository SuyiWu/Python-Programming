## YuwenWu Homework 5

## Part A

customer = {1:{'name': 'Orwell', 'address':'4 Church St', 'age':'46'}
            , 2:{'name': 'Cicero', 'address':'11 Carmine St', 'age':'63'}}

a = customer[1]['address']
print(a)

customer[1]['birthday'] = '25 June'
customer[1]['name'] = 'Orwell, George'

print(customer)



## Part B

phonebook = { 'Euclid': {'number':'212.479.2851'}
              , 'Pythagoras': {'number':'212.479.4953'}
              , 'Avicenna': {'number':'212.892.1234'}
              , 'Descartes': {'number':'917.372.1650'}
              }


work = phonebook.get('Newton',"Name not found")
print(work)

if work == "Name not found":
    phonebook['Newton'] = {'number':'917.364.1727'}

phonebook['Avicenna'] ={'number': '212.472.1037'}
phonebook.pop('Descartes')


for i,j in phonebook.items():
    print(i,j['number'])

for i in phonebook:
    if i == "Newton":
        phonebook['Newton'] ={'number':'212.479.2851','areaCode': '917'}
    elif i == 'Euclid':
        phonebook['Euclid']= {'number':'212.479.2851', 'areaCode': '212'}
    elif i == 'Pythagoras':
        phonebook['Pythagoras']={'number':'212.479.4953','areaCode': '212'}
    else:
        phonebook['Avicenna']= {'number': '212.472.1037', 'areaCode': '212'}
        
print(phonebook)

for i,j in phonebook.items():
    if j['number']=='212.479.4953':
        print("The name associated with 212.479.4953 is:", i)


