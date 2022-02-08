import datetime
import csv



def data():
    date = datetime.datetime.today().replace(microsecond=0)
    print(f"Current date and time: {date}")
    CsvDate =(f'Edit: {date}').split(" , ")
    with open(r'Kalendarz.csv', "a") as f:
        writer = csv.writer(f)
        writer.writerow(CsvDate)