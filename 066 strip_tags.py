def strip_tags(html):
    text = ""
    is_att = False
    for char in html:
        if char == '<':
            is_att = True
        elif char == '>':
            is_att = False
        elif not is_att:
            text += char
    return text

print(strip_tags('<a href="#">Click here</a>'))
print(strip_tags('<p class="center">Hello <b>World</b>!</p>'))
print(strip_tags('<img src="cat.jpg" alt="Cat">'))
print(strip_tags('<main id="main"><section class="section">section</section><section class="section">section</section></main>'))
