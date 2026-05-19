import string

def parse_italics(markdown): 
    n = len(markdown) 
    for italics_mark in ["*", "_"]: 
        i = 0 
        while i != -1: 
            i = markdown.find(italics_mark, i) 
            j = markdown.find(italics_mark, i+1) 
            if i != -1 and i < n-2 and markdown[i+1] != " " and j != -1 and markdown[j-1] != " ": 
                markdown = markdown.replace(italics_mark, "<i>", 1) 
                markdown = markdown.replace(italics_mark, "</i>", 1) 
            i = j 
    return markdown

print(parse_italics("*This is italic*"))
print(parse_italics("_This is also italic_"))
print(parse_italics("*This is not italic *"))
print(parse_italics("_ This is also not italic_"))
print(parse_italics("The *quick* brown fox _jumps_ over the *lazy* dog."))
