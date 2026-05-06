def convert(heading):
    heading = heading.strip()
    num = 0
    while heading[num] == '#':
        num += 1
    if num == 0 or heading[num] != " " or num > 6:
        return "Invalid format"
    return f"<h{num}>{heading[num:].strip()}</h{num}>"

print(convert("# My level 1 heading"))
print(convert("My heading"))
print(convert("##### My level 5 heading"))
print(convert("#My heading"))
print(convert("  ###  My level 3 heading"))
print(convert("####### My level 7 heading"))
print(convert("## My #2 heading"))
