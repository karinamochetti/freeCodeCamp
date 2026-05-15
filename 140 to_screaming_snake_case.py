def to_screaming_snake_case(variable_name):
    variable_name = variable_name.replace("-", "_")
    snakecase = variable_name[0].upper()
    for c1, c2 in zip(variable_name[:-1], variable_name[1:]):
        if c1.islower() and c2.isupper():
            snakecase += "_"
        snakecase += c2.upper()
    return snakecase

print(to_screaming_snake_case("userEmail"))
print(to_screaming_snake_case("UserPassword"))
print(to_screaming_snake_case("user_id"))
print(to_screaming_snake_case("user-address"))
print(to_screaming_snake_case("username"))
print(to_screaming_snake_case("my_variable_name"))
