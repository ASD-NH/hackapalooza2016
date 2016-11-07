text = input()
data = text.split(",")

month = data[0]
if month == "september" or month == "april" or month == "june" or month == "november":
    month_days = 30
elif month == "february":
    month_days = 28
else:
    month_days = 31

day = data[2]
if day == "monday":
    day_num = 1
elif day == "tuesday":
    day_num = 2
elif day == "wednesday":
    day_num = 3
elif day == "thursday":
    day_num = 4
elif day == "friday":
    day_num = 5
elif day == "saturday":
    day_num = 6
else:
    day_num = 7

day = (month_days - int(data[1])) % 7 + day_num
if day == 1:
    name = "monday"
elif day == 2:
    name = "tuesday"
elif day == 3:
    name = "wednesday"
elif day == 4:
    name = "thursday"
elif day == 5:
    name = "friday"
elif day == 6:
    name = "saturday"
elif day == 7:
    name = "sunday"

print(name)