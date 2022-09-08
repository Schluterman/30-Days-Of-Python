from datetime import datetime
from datetime import date
now = datetime.now()
print(now)
day = now.day
month = now.month               
year = now.year
hour = now.hour
min = now.minute
second = now.second

timestamp = now.timestamp()

print(day,month,year,hour,min)
formated_date = now.strftime("%m/%D/%Y, %H:%M:%S")
print(formated_date)

date_string = "5 December, 2019"
print("date_string =", date_string)
date_object = datetime.strptime(date_string, "%d %B, %Y")
print("date_object =", date_object)

today = date(year=2022, month=9,day=8)
new_year = date(year=2023, month=1, day=1)
diff = new_year - today
print(f'time left :{diff}')
print(now.timestamp())

