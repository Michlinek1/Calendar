import calendar
import csv


def Kalendarz():
    while True:
        try:
            yy = int(input("Enter year:"))
            mm = int(input("Enter month(1 = January, 2 = February etc...):"))
            print(calendar.month(yy, mm))
            break
        except (ValueError , TypeError, IndexError, calendar.IllegalMonthError):
            print("Try again!")
        

    if (yy % 4 == 0): #Sprawdzam, czy reszta z yy jest rowna 0 
        print(f'Funfact, {yy} is a leap day')
    else:
        print(f'Funfact, {yy} is not a leap day')

    if mm == 1:
        print(f'Important days in January:', end="")
        print("Jan 15 - Army Day,Jan 27 - International Holocaust Day")
    elif mm == 2:
        print(f'Important days in February:', end= "")
        print("Feb 14 - St. Valentine's Day,Feb 28	- National Science Day")
    elif mm == 3:
        print(f'Important days in March:', end= "")
        print("Mar 8 - International Women's Day,Mar 15 - World Consumer Day")
    elif mm == 4:
        print(f'Important days in April:', end= "")
        print("Apr 7 - World Health Day,Apr 12 - International Day of Human Space Flight")
    elif mm == 5:
        print(f'Important days in May:', end= "")
        print("May 1 - International Worker's Day,May 21 - Anti-terrorism Day")
    elif mm == 6:
        print(f'Important days in June:', end= "")
        print("Jun 5 - World Environment Day")
    elif mm == 7:
        print(f'Important days in July:', end= "")
        print("Jul 11 - World Population Day")
    elif mm == 8:
        print(f'Important days in August:', end= "")
        print("Aug 19- World Humanitarian Day,Sep 5 - Teacher's Day")
    elif mm == 9:
        print(f'Important days in September:', end= "")
        print("Sep 15 - Engineers' Day,Sep 27 - World Tourism Day")
    elif mm == 10:
        print(f'Important days in October:', end= "")
        print("Oct 16  -World Food Day, Oct 24 - United Nations Day")
    elif mm == 11:
        print(f'Important days in November:', end= "")
        print("Nov 11 - National Education Day, Nov 14 - Children's Day")
    elif mm == 12:
        print(f'Important days in December:', end= "")
        print("Dec 24 - Christmas,Dec 25 - Good Governance Day")
    

    

            
    CsvYearAndMonth = (f'Editing {yy} and {mm} month').split(",")
    with open(r'Kalendarz.csv', "a") as f:
        writer = csv.writer(f)
        writer.writerow(CsvYearAndMonth)

   
    

Kalendarz()