def get_initials(name):
    names = name.split()
    return ".".join([n[0] for n in names]) + "."

print(get_initials("Tommy Millwood"))
print(get_initials("Savanna Puddlesplash"))
print(get_initials("Frances Cowell Conrad"))
print(get_initials("Dragon"))
print(get_initials("Dorothy Vera Clump Haverstock Norris"))
