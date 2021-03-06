# import os
import datetime
from random import  randrange
import random
# import sys
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

class randQuery():
    #for i in range(0,1):
    def __init__(self):
        plate1=random.randint(0, 9)*1000
        plate2=random.randint(0, 9)*100
        plate3=random.randint(0, 9)*10
        plate4=random.randint(0, 9)
        self.plate=plate1+plate2+plate3+plate4
        
        testDate,dayBool=randomDay(plate4)
        self.date=testDate

        testHour,timeBool=randomHour()
        self.hour=str(testHour)[:-3]

        self.solution=str(timeBool and dayBool)

    def __str__(self):
        return f'Car with the plate {self.plate}, date {self.date}, time {self.hour}'


    def saveQuery(self):
        """ Saves the created input in a txt file"""

        # print('%s %s %s %s\n' % (self.plate,
        # self.date, 
        # self.hour,
        # self.solution))
        fout=open("test_query.txt", 'wt')
        fout.write('%s %s %s\n' % (self.plate,
        self.date, 
        self.hour) )
        fout.write('\n')
        fout.close


def randomDay(plateDigit):
    """ Receives the plate number, and outputs a random date and a boolean 
    True if the date is in the same day of the week of the given plate, otherwise False"""
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
    """ Outputs a random time and a boolean 
    True if the time is between Pico y Placa time restriction, otherwise False"""

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


