def parse_inline_code(markdown):
    while markdown.find("`") != -1:
        markdown = markdown.replace("`", "<code>", 1)
        markdown = markdown.replace("`", "</code>", 1)

    return markdown

print(parse_inline_code("Use `let` to declare the variable."))
print(parse_inline_code("Use `let` or `const` to declare a variable."))
print(parse_inline_code("Run `npm install` then `npm start`."))
