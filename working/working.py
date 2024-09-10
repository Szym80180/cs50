import re
import sys

pattern1 = r"^(\d{1,2}) (\w{2})$" # bez :
pattern2 = r"^(\d{1,2}):(\d{2}) (\w{2})$"

def main():
    print(convert(input("Hours: ")))

def convert(s):
    if " to " in s:
        split = s.split(" to ")
    else:
        raise ValueError

    ### Time 1
    time1 = split[0]

    matchtime1 = re.match(pattern1, time1)
    if matchtime1: #time 1 matched with pattern 1
        hour = int(matchtime1.group(1))
        if hour>12:
            raise ValueError("Wrong hour")

        if matchtime1.group(2)=="AM":
            if hour == 12:
                hour = 0

        if (matchtime1.group(2)=="PM"):
            if hour == 12:
                hour = 12
            else:
                hour+=12

        if hour==24:
                hour=0
        if len(str(hour))==1:
            hour=f"0{hour}"
        time1=f"{hour}:00"
    else:
        matchtime1 = re.match(pattern2, time1) #time 1 matched with pattern 2
        if matchtime1:
            hour = int(matchtime1.group(1))
            if hour>12:
                raise ValueError("Wrong hour")
            minutes = int(matchtime1.group(2))

            if matchtime1.group(3)=="AM":
                if hour == 12:
                    hour = 0

            if (matchtime1.group(3)=="PM"):
                if hour == 12:
                    hour = 12
                else:
                    hour+=12

            if hour==24:
                hour=0

            if minutes >59 or minutes <0:
                raise ValueError("Wrong minutes")
            if len(str(hour))==1:
                hour=f"0{hour}"
            if len(str(minutes))==1:
                minutes=f"0{minutes}"

            time1=f"{hour}:{minutes}"
        else:
            raise ValueError("Time 1 not matched")
    ### Time 2
    time2 = split[1]
    matchtime2 = re.match(pattern1, time2)
    if matchtime2: #time 2 matched with pattern 1
        hour = int(matchtime2.group(1))

        if hour>12:
            raise ValueError("Wrong hour")

        if matchtime2.group(2)=="AM":
            if hour == 12:
                hour = 0

        if (matchtime2.group(2)=="PM"):
            if hour == 12:
                hour = 12
            else:
                hour+=12

        if hour==24:
            hour=0

        if len(str(hour))==1:
            hour=f"0{hour}"
        time2=f"{hour}:00"
    else:
        matchtime2 = re.match(pattern2, time2) #time 2 matched with pattern 2
        if matchtime2:
            hour = int(matchtime2.group(1))
            if hour>12:
                raise ValueError("Wrong hour")
            minutes = int(matchtime2.group(2))

            if matchtime2.group(3)=="AM":
                if hour == 12:
                    hour = 0

            if (matchtime2.group(3)=="PM"):
                if hour == 12:
                    hour = 12
                else:
                    hour+=12

            if minutes >59 or minutes <0:
                raise ValueError("Wrong minutes")

            if len(str(hour))==1:
                hour=f"0{hour}"

            if len(str(minutes))==1:
                minutes=f"0{minutes}"

            time2=f"{hour}:{minutes}"
        else:
            raise ValueError("Time 2 not matched")
    return f"{time1} to {time2}"












...


if __name__ == "__main__":
    main()
