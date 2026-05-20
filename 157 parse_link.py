def parse_link(markdown):
    start = markdown.find("(")+1
    end = -1
    link_url = markdown[start:end]
    start = 1
    end = markdown.find("]")
    link_text = markdown[start:end]
    return f'<a href="{link_url}">{link_text}</a>'

print(parse_link("[freeCodeCamp](https://freecodecamp.org/)"))
print(parse_link("[Donate to our charity.](https://www.freecodecamp.org/donate/)") )
print(parse_link("[Contribute to our repository at https://github.com/freeCodeCamp/freeCodeCamp.](https://github.com/freeCodeCamp/freeCodeCamp/)"))
