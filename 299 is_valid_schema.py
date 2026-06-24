def is_valid_schema(obj):
    mandatory = {
        "username": "string", 
        "posts": 0, 
        "verified": True,
        "role": {"user", "creator", "moderator", "staff",  "admin"},
        "badges": ["string"]
    }
    optional = {
        "supporter": True
    }

    def validate_key(key, obj, types):
        if isinstance(types[key], set):
            return obj[key] in types[key] 
        elif isinstance(types[key], list):
            return all(type(k) is type(types[key][0]) for k in obj[key])
        else:
            return type(obj[key]) is type(types[key])

    if all(
            key in obj 
            and 
            validate_key(key, obj, mandatory) 
            for key in mandatory
        ) and all(
            validate_key(key, obj, optional) 
            for key in optional if key in obj
        ):
        return True
    return False


print(is_valid_schema({"username": "gill", "posts": 12, "verified": False, "role": "creator", "supporter": False, "badges": ["early-adopter", "popular"]}))
print(is_valid_schema({"username": "tonya", "posts": 299, "verified": True, "role": "moderator", "supporter": True, "badges": ["streak-master", "veteran"], "followers": 1233}))
print(is_valid_schema({"username": "zara", "posts": 0, "verified": False, "role": "user", "supporter": False, "badges": []}))
print(is_valid_schema({"username": "nicole", "posts": 65, "verified": True, "role": "admin", "supporter": False, "badges": ["first-post", 18]}))
print(is_valid_schema({"username": "tim", "posts": 25, "verified": True, "role": "staff", "supporter": False}))
print(is_valid_schema({"username": "charlie", "posts": 0, "verified": False, "role": "user", "supporter": "no", "badges": ["first-post", "anniversary"]}))
print(is_valid_schema({"username": "wanda", "posts": 15, "verified": True, "role": "friend", "supporter": True, "badges": ["popular"]}))
print(is_valid_schema({"username": "guy", "posts": 5, "verified": "false", "role": "staff", "supporter": True, "badges": ["helper"]}))
print(is_valid_schema({"username": "carrie", "verified": True, "role": "moderator", "supporter": True, "badges": ["helper", "sharer"]}))
print(is_valid_schema({"username": True, "posts": 75, "verified": True, "role": "creator", "supporter": True, "badges": ["veteran"]}))
