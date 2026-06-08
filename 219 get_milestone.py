def get_milestone(years):
    milestones = {
        70: "Platinum",
        60: "Diamond",
        50: "Gold",
        40: "Ruby",
        25: "Silver",
        10: "Tin",
        5: "Wood",
        1: "Paper",
    }
    for year in milestones:
        if years >= year:
            return milestones[year]
    return "Newlyweds"

print(get_milestone(0))
print(get_milestone(1))
print(get_milestone(8))
print(get_milestone(10))
print(get_milestone(26))
print(get_milestone(45))
print(get_milestone(50))
print(get_milestone(64))
print(get_milestone(71))

