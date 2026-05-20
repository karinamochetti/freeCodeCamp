def get_number_of_plants(field_size, unit, crop):
    to_sm = {
        "acres": 4046.86,
        "hectares": 10000,
    }
    space = {
        "corn": 1,
        "wheat": 0.1,
        "soybeans": 0.5,
        "tomatoes": 0.25,
        "lettuce": 0.2,
    }


    return int(field_size*to_sm[unit]/space[crop])

print(get_number_of_plants(1, "acres", "corn"))
print(get_number_of_plants(2, "hectares", "lettuce"))
print(get_number_of_plants(20, "acres", "soybeans"))
print(get_number_of_plants(3.75, "hectares", "tomatoes"))
print(get_number_of_plants(16.75, "acres", "tomatoes"))
