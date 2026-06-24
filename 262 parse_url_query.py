def parse_url_query(url):
    key_values = url.split("?")[1]
    key_values = key_values.split("&")
    result = {}
    for key_value in key_values:
        key, value = key_value.split("=")
        result[str(key)] = str(value)
    return result

print(parse_url_query("https://example.com/search?name=Alice&age=30"))
print(parse_url_query("https://freecodecamp.org/learn?skill=programming&language=python"))
print(parse_url_query("https://freecodecamp.org/items?category=books&sort=asc&page=2"))
print(parse_url_query("https://example.com?redirect=freecodecamp.org/learn&when=now"))
