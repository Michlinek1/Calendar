import datetime
import time



  


def Days():



    
    Christmas = datetime.datetime.strptime("12/24","%m/%d").strftime('%m/%d')
    BoxingDay = datetime.datetime.strptime("12/26", "%m/%d").strftime('%m/%d')
    Valentine = datetime.datetime.strptime("02/14", "%m/%d").strftime('%m/%d')
    EndOfTheSchoolYear = datetime.datetime.strptime("06/24", "%m/%d").strftime('%m/%d')
        
    print(f"Christmas Day - {Christmas}\nBoxing Day - {BoxingDay}\nValentine's day - {Valentine}\nEnd of the school (Polish time) - {EndOfTheSchoolYear}")


    

  




Days

