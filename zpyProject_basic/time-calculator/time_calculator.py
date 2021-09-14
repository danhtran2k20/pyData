# https://stackoverflow.com/questions/10851906/python-3-unboundlocalerror-local-variable-referenced-before-assignment
# https://stackoverflow.com/questions/8023306/get-key-by-value-in-dictionary
# https://stackoverflow.com/questions/15858065/python-how-to-capitalize-nth-letter-of-a-string
lookupDay = {
    "monday": 0,
    "tuesday": 1,
    "wednesday": 2,
    "thursday": 3,
    "friday": 4,
    "saturday": 5,
    "sunday": 6,
}

lookupConst = {
    "hourHalfDay": 12,
    "hourPerDay": 24,
    "minPerHour": 60,
    "minPerDay": 24 * 60,
    "minPerWeek": 7 * 24 * 60,
}


def add_time(start, duration, startDay=False):
    minuteTotal = convert_Time(start, startDay) + convert_Time(duration)
    dayPass, minuteInDay = divmod(minuteTotal, lookupConst["minPerDay"])
    hourInDay, minuteFinal = divmod(minuteInDay, lookupConst["minPerHour"])
    timeFormater = "PM" if hourInDay > 11 else "AM"
    if hourInDay == 0:
        hourInDay = 12
    if hourInDay > 12:
        hourInDay -= 12
    # Check startDay value first to find correct dayPass
    if startDay:
        dayPass -= lookupDay[startDay.lower()]
        dayDisplayStr = ", " + find_newDay(minuteTotal)
    else:
        dayDisplayStr = ""
    dayPassDisplay = " (next day)" if dayPass == 1 else ""
    if dayPass > 1:
        dayPassDisplay = f" ({dayPass} days later)"
    strAddTime = (
        f"{hourInDay}:{minuteFinal:02d} {timeFormater}{dayDisplayStr}{dayPassDisplay}"
    )
    # print(
    #     "\n strAddTime:",
    #     strAddTime,
    # )
    return strAddTime


def convert_Time(timeInput, day=False):
    splitTimeFormat = timeInput.split()
    hour, minute = (int(x) for x in splitTimeFormat[0].split(":"))
    if len(splitTimeFormat) == 2 :
        if splitTimeFormat[1] == "PM":
            hour += lookupConst["hourHalfDay"]
        if splitTimeFormat[1] == "AM" and hour == 12:
            hour = 0
    if day:
        hour += lookupDay[day.lower()] * lookupConst["hourPerDay"]
    return hour * lookupConst["minPerHour"] + minute


def find_newDay(minuteTotal):
    minInWeek = minuteTotal % lookupConst["minPerWeek"]
    dayToLook = minInWeek // lookupConst["minPerDay"]
    return [k for k, v in lookupDay.items() if v == dayToLook][0].capitalize()


# print('add_time("11:55 AM", "3:12"):', add_time("11:55 AM", "3:12"))
# print('add_time("9:15 PM", "5:30"):', add_time("9:15 PM", "5:30"))
# print('add_time("11:40 AM", "0:25"):', add_time("11:40 AM", "0:25"))

# add_time("11:59 PM", "24:05")

# print('add_time("5:01 AM", "0:00"):', add_time("5:01 AM", "0:00"))

# print('add_time("8:16 PM", "466:02"):', add_time("8:16 PM", "466:02"))
# print(
#     'add_time("8:16 PM", "466:02", "tuesday"):',
#     add_time("8:16 PM", "466:02", "tuesday"),
# )

# print('add_time("11:59 PM", "24:05"):', add_time("11:59 PM", "24:05"))
# print(
#     'add_time("11:59 PM", "24:05", "Wednesday"):',
#     add_time("11:59 PM", "24:05", "Wednesday"),
# )

# print('add_time("2:59 AM", "24:00"):', add_time("2:59 AM", "24:00"))
# print(
#     'add_time("2:59 AM", "24:00", "saturDay"):',
#     add_time("2:59 AM", "24:00", "saturDay"),
# )

# print('add_time("3:30 PM", "2:12"):', add_time("3:30 PM", "2:12"))
# print('add_time("3:30 PM", "2:12", "Monday"):', add_time("3:30 PM", "2:12", "Monday"))
test = "12:05 AM", "00:55", "sUnDAy"

print(f"{test} add: \n{add_time(*test)}")

