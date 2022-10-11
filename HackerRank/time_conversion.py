# [해커랭크] Time Conversion
def timeConversion(s):
    ampm = s[-2:]
    time = s[:-2]
    hh = int(s[:2])
    if ampm == 'PM' and hh < 12:
        time = str(hh + 12).zfill(2) + time[2:]
    elif ampm == 'AM' and hh >= 12:
        time = str(hh - 12).zfill(2) + time[2:]
    return time

if __name__ == '__main__':

    s = '12:05:39AM'

    result = timeConversion(s)

    print(result)
