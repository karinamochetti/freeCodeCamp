def space_jam(string):
    string = string.replace(" ", "").upper()
    new_string = "" 
    for s in string:
        new_string += s + "  "
    return new_string[:-2]

print(space_jam("freeCodeCamp"))
print(space_jam("   free   Code   Camp   "))
print(space_jam("Hello World?!"))
print(space_jam("C@t$ & D0g$"))
print(space_jam("allyourbase"))