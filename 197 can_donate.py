def can_donate(donor, recipient):
    compatibility = {
        "O": {"O", "A", "B", "AB"},
        "A": {"A", "AB"},
        "B": {"B", "AB"},
        "AB": {"AB"}
    }

    d_type, d_rh = donor[:-1], donor[-1]
    r_type, r_rh = recipient[:-1], recipient[-1]

    if d_rh == "+" and r_rh == "-":
        return False

    return r_type in list(compatibility[d_type])


print(can_donate("B+", "B+"))
print(can_donate("O-", "AB-"))
print(can_donate("O+", "A-"))
print(can_donate("A+", "AB+"))
print(can_donate("A-", "B-"))
print(can_donate("B-", "AB+"))
print(can_donate("B-", "A+"))
print(can_donate("O-", "O+"))
print(can_donate("O+", "O-"))
print(can_donate("AB+", "AB-"))
