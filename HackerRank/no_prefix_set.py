# [해커랭크] No Prefix Set
def noPrefix(words):
    # Write your code here
    wordDict = {}
    for word in words:
        temp = wordDict
        for letter in word:
            flag=False
            if letter in temp:
                flag = True
                temp = temp[letter]
                if len(temp.keys()) == 0:
                    break
                continue
            temp[letter] = {}
            temp = temp[letter]
        if flag:
            print("BAD SET")
            print(word)
            return
    print("GOOD SET")