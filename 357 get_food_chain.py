def get_food_chain(pairs):
    predators = [p[1] for p in pairs]
    for pair in pairs:
        if not pair[0] in predators:
            main_predator = pair[0]
            break
    chain = [main_predator]
    is_predator = True
    while is_predator:
        is_predator = False
        for pair in pairs:
            if chain[-1] == pair[0]:
                is_predator = True
                chain.append(pair[1])
    return chain


print(get_food_chain([["cat", "mouse"]]))
print(get_food_chain([["wolf", "deer"], ["deer", "grass"]]))
print(get_food_chain([["hawk", "snake"], ["snake", "frog"], ["frog", "fly"]]))
print(get_food_chain([["rabbit", "grass"], ["fox", "rabbit"], ["eagle", "fox"]]))
print(get_food_chain([["seal", "salmon"], ["herring", "shrimp"], ["orca", "seal"], ["shrimp", "plankton"], ["salmon", "herring"]]) )
