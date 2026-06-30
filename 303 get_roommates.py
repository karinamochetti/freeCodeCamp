def get_roommates(people):
    people = sorted(people, key=lambda x: x["group"])
    pairs = []
    i = 0
    while i < len(people):
        p1 = people[i]
        p2 = people[i+1] if i+1 < len(people) else {}
        if p2 == {}:
            pairs.append(p1["name"])
            i += 1
        elif p1["group"] != p2["group"]:
            pairs.append(p1["name"])
            i += 1
        else:
            pairs.append(p1["name"]+" and "+p2["name"])
            i += 2
    return pairs


print(get_roommates([{ "name": "Alice", "group": "A" }, { "name": "Bob", "group": "B" }, { "name": "Carol", "group": "A" }]))
print(get_roommates([{ "name": "John", "group": "C" }, { "name": "Julia", "group": "C" }, { "name": "Jim", "group": "C" }]))
print(get_roommates([{ "name": "Adam", "group": "D" }, { "name": "Abraham", "group": "E" }, { "name": "Austin", "group": "E" }, { "name": "Augustus", "group": "D" }, { "name": "Angelica", "group": "D" }, { "name": "Aaron", "group": "E" }]))
print(get_roommates([{ "name": "Frank", "group": "A" }, { "name": "Emitt", "group": "B" }, { "name": "Daria", "group": "F" }, { "name": "Charles", "group": "D" }, { "name": "Bailey", "group": "A" }, { "name": "Albert", "group": "F" }]))
print(get_roommates([{ "name": "Kevin", "group": "A" }, { "name": "Yuri", "group": "A" }, { "name": "Hugo", "group": "B" }, { "name": "Violet", "group": "A" }, { "name": "Brett", "group": "A" }, { "name": "Wayne", "group": "B" }]))
