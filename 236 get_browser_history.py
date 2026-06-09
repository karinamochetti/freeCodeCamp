def get_browser_history(commands):
    sites = []
    index = -1
    print()
    for comm in commands:
        if comm == "Back":
            index = max(0, index-1)
        elif comm == "Forward":
            index = min(len(sites)-1, index+1)
        else:
            sites = sites[:index+1] + [comm]
            index = min(len(sites)-1, index+1)
        print(index, sites[index-1])


    return [sites, index]

print(get_browser_history(["freecodecamp.org", "freecodecamp.org/learn", "Back"]))
print(get_browser_history(["example.com", "example.com/about", "example.com/contact", "example.com/blog"]))
print(get_browser_history(["example.com", "example.com/about", "Back", "example.com/contact", "example.com/blog", "Back", "Back", "Forward"]))
print(get_browser_history(["example.com", "example.com/about", "example.com/contact", "example.com/blog", "Back", "Back", "Forward", "freecodecamp.org"]))
print(get_browser_history(["example.com", "example.com/about", "Back", "Back"]))
print(get_browser_history(["example.com", "example.com/about", "Forward"]))
