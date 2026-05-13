def title_case(title):
    words = title.split()
    capitalized = [word.capitalize() for word in words]
    return " ".join(capitalized)

print(title_case("hello world"))
print(title_case("the quick brown fox"))
print(title_case("JAVASCRIPT AND PYTHON"))
print(title_case("AvOcAdO tOAst fOr brEAkfAst"))
