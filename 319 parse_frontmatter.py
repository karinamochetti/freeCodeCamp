def parse_frontmatter(s):
    obj = {}

    for line in s.splitlines():
        if ":" not in line:
            continue
            
        key, raw_value = line.split(":", 1) 
        raw_value = raw_value.strip()  

        if raw_value.lower() == "true":
            value = True
        elif raw_value.lower() == "false":
            value = False
        elif raw_value.isdigit():
            value = int(raw_value)
        else:
            try:
                value = float(raw_value)
            except ValueError:
                value = raw_value  
                
        obj[key] = value

    return obj

print(parse_frontmatter("---\ntitle: My Post\ndraft: false\nviews: 100\n---"))
print(parse_frontmatter("---\nid: 6a174db57256a112f932195c\ntitle: My Book\nlocale: en\nwordCount: 10000\npublished: false\n---"))
print(parse_frontmatter("---\nversion: 1.0.0\nurl: https://example.com\nprivate: true\n---"))
print(parse_frontmatter("---\nrating: 4.5\nprice: 9.99\n---"))
