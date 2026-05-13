def parse_blockquote(markdown):
    markdown = markdown.strip()
    parts = markdown.split(" ", 1)
    return f"<blockquote>{parts[1].strip()}</blockquote>"

print(parse_blockquote("> This is a quote"))
print(parse_blockquote(" > This is also a quote"))
print(parse_blockquote("  >    So  Is  This"))
