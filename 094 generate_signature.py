def generate_signature(name, title, company):
    if "A" <= name[0].upper() <= "I":
        signature = ">>"
    if "J" <= name[0].upper() <= "R":
        signature = "--"
    if "S" <= name[0].upper() <= "Z":
        signature = "::"
    signature += name + ", " + title + " at " + company
    return signature

print(generate_signature("Quinn Waverly", "Founder and CEO", "TechCo"))
print(generate_signature("Alice Reed", "Engineer", "TechCo"))
print(generate_signature("Tina Vaughn", "Developer", "example.com"))
print(generate_signature("B. B.", "Product Tester", "AcmeCorp"))
print(generate_signature("windstorm", "Cloud Architect", "Atmospheronics"))
