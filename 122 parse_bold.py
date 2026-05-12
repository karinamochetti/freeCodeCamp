import string

def parse_bold(markdown):
    n = len(markdown)
    for bold_mark in ["**", "__"]:
        i = 0
        while i != -1:
            i = markdown.find(bold_mark, i)
            j = markdown.find(bold_mark, i+1)
            if i != -1 and i < n-2 and markdown[i+2] != " " and j != -1 and markdown[j-1] != " ":
                markdown = markdown.replace(bold_mark, "<b>", 1)
                markdown = markdown.replace(bold_mark, "</b>", 1)
            i = j

    return markdown

print(parse_bold("**This is bold**"))
print(parse_bold("__This is also bold__"))
print(parse_bold("**This is not bold **"))
print(parse_bold("__ This is also not bold__"))
print(parse_bold("The **quick** brown fox __jumps__ over the **lazy** dog."))
