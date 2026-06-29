from collections import Counter

def triage_blood(bank, patients):

    supply = Counter(bank)
    demand = Counter(patients)

    matchs = 0

    o_served = min(demand["O"], supply["O"])
    matchs += o_served
    supply["O"] -= o_served


    a_served = min(demand["A"], supply["A"])
    matchs += a_served
    supply["A"] -= a_served
    
    a_patients = demand["A"] - a_served
    a_served = min(a_patients, supply["O"])
    matchs += a_served
    supply["O"] -= a_served

 
    b_served = min(demand["B"], supply["B"])
    matchs += b_served
    supply["B"] -= b_served
    
    b_patients = demand["B"] - b_served
    b_served = min(b_patients, supply["O"])
    matchs += b_served
    supply["O"] -= b_served


    ab_served = min(demand["AB"], supply["A"]+supply["B"]+supply["AB"]+supply["O"])
    matchs += ab_served

    return f"{matchs} of {len(patients)} patients served"

print(triage_blood(["O", "A", "B", "AB"], ["O", "A", "B", "AB"]))
print(triage_blood(["A", "A", "B", "B", "AB"], ["O", "A", "B", "B", "B"]))
print(triage_blood(["O", "A", "B", "AB"], ["AB", "AB", "AB", "AB", "AB"]))
print(triage_blood(["O", "O", "O", "O", "O"], ["O", "A", "B", "AB"]))
print(triage_blood(["A", "O", "B", "AB", "B", "AB", "O", "A", "A"], ["O", "A", "B", "AB", "A", "B", "A", "A", "B", "A", "B"]))
print(triage_blood(["O", "B", "AB", "AB", "O", "A", "A", "AB", "O", "B", "B", "AB", "A", "B", "AB"], ["O", "A", "B", "B", "A", "B", "AB", "A", "B", "A", "O", "AB", "AB", "O"]))
