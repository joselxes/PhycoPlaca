import datetime

plateToDay={ "1":"lunes",
        "2":"lunes",
        "3":"martes",
        "4":"martes",
        "5":"miércoles",
        "6":"miércoles",
        "7":"jueves",
        "8":"jueves",
        "9":"viernes",
        "0":"viernes",
}

class autoQuery:
    def __init__(self,plateNumber,plateDate,plateTime):
        self.number=plateNumber
        self.date=plateDate
        self.time=plateTime
    def __str__(self):
        # format.{the car {self.number}, inthe Day {self.date}, at the time {self.time}  }
        # 'The car with the plate {number}, inthe Day {date}, at the time {time}'.format(number=self.number, date=self.date, time=self.time)
        return f'\tThe car with the plate {self.number}, in the Day {self.date}, at the time {self.time}'
    def drivingTime(self):
        print("\t",self.number%10)    
        
        # __ini__():
# python3 
#

