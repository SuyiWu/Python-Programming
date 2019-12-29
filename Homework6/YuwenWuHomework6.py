## Yuwen Wu Homework 6

originalFileName = 'C:/Users/michael.deamer/Desktop/Python IO/tickerInfo.csv'
modifiedFileName = 'C:/Users/michael.deamer/Desktop/Python IO/tickerInfoWithDelta.csv'

def calculateDelta(closingPrice, openingPrice):
    closingPriceFloat = float(closingPrice.replace('$', '').replace(',', ''))
    openingPriceFloat = float(openingPrice.replace('%', '').replace(',', ''))
    a = closingPriceFloat - openingPriceFloat
    a = round(a,2)
    return a
 

with open(originalFileName,'r',encoding = 'utf-8') as originalFile, open(modifiedFileName, 'w',encoding = 'utf-8') as destinationFile:
    destinationFile.write('Date,Close,Open,Delta,Direction,UpDays\n') 
    line = originalFile.readline()
    line = originalFile.readline()
    i = 0
    a = 0
    while line != '':
        lineList = line.split(',')
        date = lineList[0]
        closingPrice = lineList[1]
        highPrice = lineList[2]
        lowPrice = lineList[3]
        openingPrice = lineList[4]
        volume = lineList[5]
        delta = calculateDelta(closingPrice,openingPrice)
        if delta > 0 :
            direction = 1
            i += 1
        else :
            direction = 0
            i = 0
        if i >= 4:
            d = 1
        else:
            d = 0
        destinationFile.write(date+','+closingPrice+','+openingPrice+','+str(delta)+','+str(direction)+','+str(d)+'\n')       
        line = originalFile.readline().replace('\n','')
        