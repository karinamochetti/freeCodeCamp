def get_headings(csv):
    headings = csv.split(",")
    headings = [heading.strip() for heading in headings]
    return headings

print(get_headings("name,age,city"))
print(get_headings("first name,last name,phone"))
print(get_headings("username , email , signup date "))
