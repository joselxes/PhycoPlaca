import os
import datetime
from random import  randrange
import random
import sys
plateToDay={ "1":0,
        "2":0,
        "3":1,
        "4":1,
        "5":2,
        "6":2,
        "7":3,
        "8":3,
        "9":4,
        "0":4,
}

def randomInput():
    #for i in range(0,1):
    fout=open("create_query.txt", 'wt')

    plate1=random.randint(0, 9)
    plate2=random.randint(0, 9)
    plate3=random.randint(0, 9)
    plate4=random.randint(0, 9)    

    testDate,dayBool=randomDay(plate4)
    testHour,timeBool=randomHour()

    fout.write('%s%s%s%s %s %s\n' % (plate1, plate2, plate3, plate4,
     str(testDate), 
     str(testHour)[:-3] ))
    fout.write('\n')
    fout.close
    print('%s%s%s%s %s %s\n' % (plate1, plate2, plate3, plate4,
     str(testDate), 
     str(testHour)[:-3] ))
    return  timeBool and dayBool
def randomDay(plateDigit):
    testYear=random.randint(2012, 2023)    
    testMonth=random.randint(1, 12)

    if testMonth in [1,3,5,7,8,10,12]:
        lastDay=31
    elif testMonth in [4,6,9,11]:
        lastDay= 30
    else:
        lastDay=28
    testDay=random.randint(1, lastDay)
    testDate=datetime.date(testYear,testMonth,testDay)

    if random.randint(0,1):
        drive=True    
    else:
        drive=False

    if drive:
        while testDate.weekday() != plateToDay[str(plateDigit)]:
            testDay=random.randint(1, lastDay)
            testDate=datetime.date(testYear,testMonth,testDay)

    else:
        while testDate.weekday() == plateToDay[str(plateDigit)]:
            testDay=random.randint(1, lastDay)
            testDate=datetime.date(testYear,testMonth,testDay)


    return testDate, drive

def randomHour():
    if random.randint(0,1):
        drive=True    
    else:
        drive=False
    restrictedHours=[7, 8, 9, 16, 17, 18, 19]
    allowedHours=[6, 9, 10, 11, 12, 13, 14,15,19,20]
    
    if drive:
        randomHour=restrictedHours[random.randint(0,len(restrictedHours)-1)]
        if randomHour in [9,19]:
            randomMinutes=random.randint(0,30)
        else:
            randomMinutes=random.randint(0,59)


    else:
        randomHour=allowedHours[random.randint(0,len(allowedHours)-1)]
        if randomHour in [9,19]:
            randomMinutes=random.randint(31,59)
        else:
            randomMinutes=random.randint(0,59)
    
    # print('--%s--   %s:%s'%(drive,randomHour,randomMinutes))
    

    return datetime.time(randomHour,randomMinutes), drive   

    # print('%s%s%s%s %s%s-%s-%s %s:%s%s\n' % (plate1, plate2, plate3, plate4, 
    # 20, testYear, testMonth, testday,
    #  testHour, testMinute1, testMinute2))




def main():
    varControl=randomInput()
    batcmd=('python3 predictor.py < create_query.txt ')
    result  = os.popen(batcmd).readlines()
    print(result[0][:-1]== str(varControl))
    varCount=0
    while result[0][:-1]== str(varControl):
        varControl=randomInput()
        result  = os.popen(batcmd).readlines()
        print(result[0][:-1]== str(varControl), varCount)
        varCount+=1



if __name__ == "__main__":
    main()
