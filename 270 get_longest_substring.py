def get_longest_substring(s):
    max_s = ""
    n = len(s)
    for i in range(n):
        for j in range(i,n):
            if sum(1 if s[k:k+j-i] == s[i:j] else 0 for k in range(n+j-i)) > 1 and len(s[i:j]) > len(max_s):
                max_s = s[i:j]
    return max_s

print(get_longest_substring("abracadabra"))
print(get_longest_substring("hello world hello"))
print(get_longest_substring("mississippi"))
print(get_longest_substring("ha ha ha ha ha ha ha"))
print(get_longest_substring("the quick brown fox jumped over the lazy dog that the quick brown fox jumped over"))
