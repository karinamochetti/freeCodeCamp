def get_oldest(people):
    ages = [person["age"] for person in people]
    max_age = max(ages)
    names = [person["name"] for person in people if person["age"] == max_age]
    return names

print(get_oldest([{ "name": "Brenda", "age": 40 }]))
print(get_oldest([{ "name": "Alice", "age": 30 }, { "name": "Bob", "age": 25 }]))
print(get_oldest([{ "name": "Allison", "age": 25 }, { "name": "Bill", "age": 30 }, { "name": "Carol", "age": 30 }]))
print(get_oldest([{ "name": "George", "age": 50 }, { "name": "Shirley", "age": 42 }, { "name": "Beth", "age": 48 }, { "name": "Holly", "age": 50 }, { "name": "Kevin", "age": 44 }, { "name": "Frank", "age": 47 }, { "name": "Zach", "age": 50 }, { "name": "Jennifer", "age": 43 }]))
