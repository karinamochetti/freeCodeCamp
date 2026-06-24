def is_valid_schema(obj):

    def validade_user(obj):
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

    if "users" not in obj or not isinstance(obj["users"], list):
        return False
    if all(validade_user(user) for user in obj["users"]):
        return True
    return False


print(is_valid_schema({"users": [{"username": "ron", "posts": 14, "verified": True, "role": "creator", "badges": ["early-adopter"]}, {"username": "cher", "posts": 25, "verified": True, "role": "moderator", "supporter": True, "followers": 20, "badges": ["helper"]}]}))
print(is_valid_schema({"users": []}))
print(is_valid_schema({"users": {"username": "anne", "posts": 0, "verified": False, "role": "user", "supporter": False, "badges": []}}))
print(is_valid_schema({"users": [{"username": "tony", "posts": 10, "verified": True, "role": "creator", "supporter": True, "badges": ["liked", 6]}]}))
print(is_valid_schema({"users": [{"username": "ursula", "posts": 3, "verified": False, "role": "user", "supporter": "false", "badges": ["comeback"]}]}))
print(is_valid_schema({"users": [{"username": "benny", "posts": 55, "verified": True, "role": "superstar", "supporter": True, "badges": ["veteran"]}]}))
print(is_valid_schema({"users": [{"username": "chase", "posts": 1, "verified": "yes", "role": "staff", "supporter": False, "badges": ["superstar"]}]}))
print(is_valid_schema({"users": [{"username": "carla", "posts": "10", "verified": False, "role": "user", "supporter": False, "badges": ["newbie"]}]}))
print(is_valid_schema({"users": [{"posts": 4, "verified": False, "role": "admin", "supporter": False, "badges": ["superuser", "veteran"]}]}))
print(is_valid_schema({"users": [{"username": "harold", "posts": 80, "verified": True, "role": "creator", "supporter": True, "badges": ["liked", "hero"]}, {"username": "kim", "posts": 11, "verified": False, "role": "admin", "supporter": True, "badges": ["first"]}, {}]}))
