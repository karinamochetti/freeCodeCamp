def migrate_record(schema, record):
    for key in schema:
        if key not in list(record):
            record[key] = schema[key]
    return record

print(migrate_record({ "username": "", "posts": 0 }, { "verified": True }))
print(migrate_record({ "username": "", "posts": 0 }, { "username": "camper", "posts": 5 }))
print(migrate_record({ "username": "", "posts": 0, "verified": False }, { "username": "camper" }))
print(migrate_record({ "username": "", "posts": 0 }, { "username": "camper", "role": "admin" }))
print(migrate_record({ "username": "", "email": "", "posts": 0, "verified": False, "role": "user", "banned": False }, { "username": "camper", "email": "camper@freecodecamp.org", "role": "admin" }))
