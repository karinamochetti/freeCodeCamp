def generate_snowflake(crystals):
    lines = crystals.split("\n")
    mirror = [line + line[::-1] for line in lines]
    return "\n".join(mirror)

print(generate_snowflake("* \n *\n* "))
print(generate_snowflake("X=~"))
print(generate_snowflake(" X  \n  v \nX--=\n  ^ \n X  "))
print(generate_snowflake("*   *\n * * \n* * *\n * * \n*   *"))
print(generate_snowflake("*  -\n * -\n*  -"))
