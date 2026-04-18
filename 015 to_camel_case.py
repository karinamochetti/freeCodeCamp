def to_camel_case(string):
    string = string.replace("-", " ").replace("_", " ")
    words = string.split(" ")
    cleaned_words = [w.capitalize() for w in words if w]
    result_str = "".join(cleaned_words)

    return result_str[0].lower() + result_str[1:]


print(to_camel_case("hello world"))
print(to_camel_case("HELLO WORLD"))
print(to_camel_case("secret agent-X"))
print(to_camel_case("FREE cODE cAMP"))
print(to_camel_case("ye old-_-sea  faring_buccaneer_-_with a - peg__leg----and a_parrot_ _named- _squawk"))
