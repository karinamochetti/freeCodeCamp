def navigate(commands):
    history = ["Home"]
    page = 0
    for command in commands:
        if command == "Back":
            if page > 0: page -= 1
        elif command == "Forward":
            if page < len(history)-1: page += 1
        else:
            history.append(command[6:])
            page += 1
    return history[page]

print(navigate(["Visit About Us", "Back", "Forward"]))
print(navigate(["Forward"]))
print(navigate(["Back"]))
print(navigate(["Visit About Us", "Visit Gallery"]))
print(navigate(["Visit About Us", "Visit Gallery", "Back", "Back"]))
print(navigate(["Visit About Us", "Visit Visit Us", "Forward", "Visit Contact Us", "Back"]))
