def palindrome_locator(s):
    m = len(s)//2

    if s[::] == s[::-1]:
        return s[m] if len(s)%2==1 else s[m-1:m+1]
    return "none"

print(palindrome_locator("racecar"))
print(palindrome_locator("level"))
print(palindrome_locator("freecodecamp"))
print(palindrome_locator("noon"))
print(palindrome_locator("11100111"))
