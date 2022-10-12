# [해커랭크] Palindrom Index
'''
aaab
baa
aaa
'''
def isPalindrome(s):
    return s == s[::-1]

def palindromeIndex(s):
    for i in range(len(s)//2):
        start = i
        end = len(s)-1-i
        if s[start] != s[end]:
            if isPalindrome(s[start+1:end+1]):
                return start
            elif isPalindrome(s[start:end]):
                return end
            else:
                return -1
    return -1

print(palindromeIndex('aaab'))
print(palindromeIndex('baaa'))
print(palindromeIndex('aaa'))