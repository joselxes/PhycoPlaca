import datetime
import sys

plateToDay={ "1":"lunes",
        "2":"lunes",
        "3":"martes",
        "4":"martes",
        "5":"miercoles",
        "6":"miercoles",
        "7":"jueves",
        "8":"jueves",
        "9":"viernes",
        "0":"viernes",
}
starTime1=datetime.time(7,0)
endTime1=datetime.time(9,30)
starTime2=datetime.time(16,0)
endTime2=datetime.time(19,30)

plateList=["lunes","martes","miercoles","jueves","viernes","sabado","domingo",]

class autoQuery:
    def __init__(self,queryData):
        self.number=int(queryData[0])


        year,month,day=map(int,queryData[1].split("-"))
        self.currentDate=datetime.date(year,month,day)


        hour,minutes=map(int,queryData[2].split(":"))
        self.hour=datetime.time(hour,minutes)


    def __str__(self):

        return f'\tPlate {self.number}, in the Day {self.currentDate}, at the time {self.hour}'


    def drivingTime(self):

        dontDrive=plateToDay[str(self.number%10)]
        todayIs=plateList[self.currentDate.weekday()]
        sameDay=dontDrive==todayIs
        inTime=(starTime1<= self.hour <= endTime1) or (starTime2<= self.hour <= endTime2)
        
        return sameDay and inTime

    def writeSolution(self,boolean):

        if boolean:
            return f'The car with the plate {self.number}, the date {self.currentDate} at the time {str(self.hour)[:-3]}  has a mobility restriction.'
        return f'The car with the plate {self.number}, the date {self.currentDate} at the time {str(self.hour)[:-3]}  does not have a mobility restriction.'

