# [해커랭크] lonely Integer
def lonelyinteger(a):
    # Write your code here
    find_num = set(a)
    for num in find_num:
        if a.count(num) == 1:
            return num