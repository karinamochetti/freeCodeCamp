def check_eligibility(athlete_weights, sled_weight):
    BOBSLED_RULES = {
        1: (162, 247),
        2: (170, 390),
        4: (210, 630)
    }
    
    num_atl = len(athlete_weights)
    
    min_sled, max_combined = BOBSLED_RULES[num_atl]
    total_weight = sum(athlete_weights) + sled_weight
    
    if sled_weight < min_sled or total_weight > max_combined:
        return "Not Eligible"        
    return "Eligible"

print(check_eligibility([78], 165))
print(check_eligibility([80], 160))
print(check_eligibility([80], 170))
print(check_eligibility([85, 90], 170))
print(check_eligibility([85, 95], 168))
print(check_eligibility([112, 97], 185))
print(check_eligibility([110, 102, 90, 106], 222))
print(check_eligibility([106, 99, 90, 88], 205))
print(check_eligibility([106, 99, 103, 96], 227))
