def convert_list_item(markdown):
    markdown = markdown.strip()
    parts = markdown.split(".")
    if len(parts) != 2 or not parts[0].isdigit():
        return "Invalid format"
    return f"<li>{parts[1].strip()}</li>"

print(convert_list_item("1. My item"))
print(convert_list_item(" 1.  Another item"))
print(convert_list_item("1 . invalid item"))
print(convert_list_item("2. list item text"))
print(convert_list_item(". invalid again"))
print(convert_list_item("A. last invalid"))
