def get_extension(filename):
    words = filename.split(".")
    if len(words) == 1 or words[-1] == "": 
        return "none"
    return words[-1]

print(get_extension("document.txt"))
print(get_extension("README"))
print(get_extension("image.PNG"))
print(get_extension(".gitignore"))
print(get_extension("archive.tar.gz"))
print(get_extension("final.draft."))
