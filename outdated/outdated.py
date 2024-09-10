months = {
    "January": 1,
    "February": 2,
    "March":3,
    "April":4,
    "May":5,
    "June":6,
    "July":7,
    "August":8,
    "September":9,
    "October":10,
    "November":11,
    "December":12
}

def checkList(date):
    try:
        month = int(date[0])
        day = int(date[1])
    except ValueError:
        return False

    if month <1 or month >12:
        return False

    if day<1 or day>31:
        return False
    return True

def checkDate(date):
    for month in months:
        if date.count(month)!=1:
            continue
        if date.find(month)!=0:
            return False
        date = date.replace(month, "")
        date = date[1:]
        list = date.split(", ")
        monthNumber = months[month]
        list.insert(0,monthNumber)

        if checkList(list):
            return list
    return False




def getDate():
    while True:
        date = input("Date: ").strip()
        if date.count("/") == 2:
            list = date.split("/")
            if checkList(list):
                return list
        else:
            if checkDate(date):
                return checkDate(date)


def ConvertDate(date):
    day = date[1]
    month = date[0]
    year = date[2]

    if int(day)<10:
        day = f"0{day}"

    if int(month)<10:
        month = f"0{month}"

    result = f"{year}-{month}-{day}"
    return result



date = getDate()
date = ConvertDate(date)
print(date)




