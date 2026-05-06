def is_match(fingerprint_a, fingerprint_b):
    if len(fingerprint_a) != len(fingerprint_b): 
        return False
    diff = sum(a != b for a, b in zip(fingerprint_a, fingerprint_b))
    return diff <= 0.1*len(fingerprint_a)

print(is_match("helloworld", "helloworld"))
print(is_match("helloworld", "helloworlds"))
print(is_match("helloworld", "jelloworld"))
print(is_match("thequickbrownfoxjumpsoverthelazydog", "thequickbrownfoxjumpsoverthelazydog"))
print(is_match("theslickbrownfoxjumpsoverthelazydog", "thequickbrownfoxjumpsoverthehazydog"))
print(is_match("thequickbrownfoxjumpsoverthelazydog", "thequickbrownfoxjumpsoverthehazycat"))
