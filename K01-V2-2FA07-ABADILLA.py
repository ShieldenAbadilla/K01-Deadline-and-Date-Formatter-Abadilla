import datetime

event_title = str(input("Enter event title: "))
year = int(input("Enter event year: "))
month = int(input("Enter event month: "))
day = int(input("Enter event day: "))

event_day = datetime.date(year, month, day)

formatted_title = event_title.upper()
readable_date = event_day.strftime("%B %d, %Y")
month_name = event_day.strftime("%B")
weekday_name = event_day.strftime("%A")

print("Event:", event_title.upper())
print(f"Date: {readable_date}")
print(f"Year: {year}")
print(f"Month: {month_name}")
print(f"Day: {day}")
print(f"Weekday: {weekday_name}")