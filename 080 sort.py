def sort(emails):
    return sorted(emails, key=lambda x: (x.split('@')[1].lower(), x.split('@')[0].lower()))


print(sort(["jill@mail.com", "john@example.com", "jane@example.com"]))
print(sort(["bob@mail.com", "alice@zoo.com", "carol@mail.com"]))
print(sort(["user@z.com", "user@y.com", "user@x.com"]))
print(sort(["sam@MAIL.com", "amy@mail.COM", "bob@Mail.com"]))
print(sort(["simon@beta.com", "sammy@alpha.com", "Sarah@Alpha.com", "SAM@ALPHA.com", "Simone@Beta.com", "sara@alpha.com"]))
