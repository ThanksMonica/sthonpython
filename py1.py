import re
import collections
import datetime

resultFile = open("D:\working\python study and practice\ipViews.txt", "w+")
# get ip(139.129.17.181)
pattern = re.compile(r'((2(5[0-5]|[0-4]\d))|[0-1]?\d{1,2})(\.((2(5[0-5]|[0-4]\d))|[0-1]?\d{1,2})){3}')
# get time(15/Jul/2019:00:38:11 +0800)
str_format = "%d/%b/%Y:%X %z"

startYear = int(input("start year"))
startMonth = int(input("start month"))
startDay = int(input("start day"))
startHour = int(input("start hour"))
startMinute = int(input("start minute"))
endYear = int(input("end year"))
endMonth = int(input("end month"))
endDay = int(input("end day"))
endHour = int(input("end hour"))
endMinute = int(input("end minute"))

# open file
with open("D:\working\python study and practice\PartofAccess.txt") as file:
    result = []
    for line in file:
        time = datetime.datetime.strptime(line.split("[")[1].split("]")[0], str_format)
        ip = pattern.search(line).group()
        startTime = datetime.datetime(startYear, startMonth, startDay, startHour, startMinute).timestamp()
        endTime = datetime.datetime(endYear, endMonth, endDay, endHour, endMinute).timestamp()
        # startTime = datetime.datetime(2018, 1, 1, 1, 1).timestamp()
        # endTime = datetime.datetime(2020, 1, 1, 1, 1).timestamp()
        if startTime < time.timestamp() < endTime:
            result.append(ip)
    count = collections.Counter(result).most_common()
    for c in count:
        print("ip：%s, 访问次数：%s" % c)
        # list to str
        # ip_str = "".join(ip)
        # int to str
        count_str = str(count)
        resultFile.write(count_str)
file.close()
