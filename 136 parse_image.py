def parse_image(markdown):
    start_src = markdown.find("(")
    end_src = markdown.find(")")
    start_alt = markdown.find("[")
    end_alt = markdown.find("]")
    src = markdown[start_src+1:end_src]
    alt = markdown[start_alt+1:end_alt]
    return f'<img src="{src}" alt="{alt}">'

print(parse_image("![Cute cat](cat.png)"))
print(parse_image("![Rocket Ship](https://freecodecamp.org/cdn/rocket-ship.jpg)"))
print(parse_image("![Cute cats!](https://freecodecamp.org/cats.jpeg)"))
