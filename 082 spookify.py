def spookify(boo):
    i = 1
    new_boo = ""
    for c in boo.lower():
        if c == "_" or c == "-":
            new_boo += "~"
        else:
            i += 1
            if i%2==1: 
                new_boo += c
            else: 
                new_boo += c.upper()
    return new_boo

print(spookify("hello_world"))
print(spookify("Spooky_Case"))
print(spookify("TRICK-or-TREAT"))
print(spookify("c_a-n_d-y_-b-o_w_l"))
print(spookify("thE_hAUntEd-hOUsE-Is-fUll_Of_ghOsts"))
