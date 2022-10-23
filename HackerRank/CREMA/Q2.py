def findRange(num):
    num = str(num)
    max_num = ''
    min_num = ''
    max_change = ''
    min_change = ''
    for i, n in enumerate(num):
        if i == 0:
            if int(n) < 9:
                max_change = n
            max_num += '9'
            if int(n) > 1:
                min_change = n
            min_num += '1'
        else:
            if max_change == '' and int(n) < 9:
                max_change = n
                max_num += '9'
            elif n == max_change:
                max_num += '9'
            else:
                max_num += n
            if min_change == '' and int(n) > 0 and n != num[0]:
                min_change = n
                min_num += '0'
            elif n == min_change:
                if n == num[0]:
                    min_num += '1'
                else:
                    min_num += '0'
            else:
                min_num += n

    return int(max_num) - int(min_num)