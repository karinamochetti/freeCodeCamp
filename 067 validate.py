def validate(email):
    parts = email.split("@")
    if len(parts) != 2: return False

    if any(c for c in parts[0] if c not in "._-" and not c.isalnum()): return False
    if parts[0][0] == ".": return False
    if parts[0][-1] == ".": return False

    domains = parts[1].split(".")
    last_domain = [c for c in domains[-1] if c.isalpha()]
    if len(domains) == 1: return False
    if len(last_domain) < 2: return False
    if ".." in parts[0]: return False
    if ".." in parts[1]: return False
    return True

print(validate("a@b.cd"))
print(validate("hell.-w.rld@example.com"))
print(validate(".b@sh.rc"))
print(validate("example@test.c0"))
print(validate("freecodecamp.org"))
print(validate("develop.ment_user@c0D!NG.R.CKS"))
print(validate("hello.@wo.rld"))
print(validate("hello@world..com"))
print(validate("develop..ment_user@c0D!NG.R.CKS"))
print(validate("git@commit@push.io"))
