def is_valid_schema(obj):
    mandatory = {
        "username": "string", 
        "posts": 0, 
        "verified": True,
        "role": ["user", "creator", "moderator", "staff",  "admin"],
    }
    optional = {
        "supporter": True
    }

    if all(
            key in obj 
            and 
            (
                obj[key] in mandatory[key] 
                if isinstance(mandatory[key], list)
                else type(obj[key]) is type(mandatory[key])
            ) 
            for key in mandatory
        ) and all(
            type(obj[key]) is type(optional[key])
            for key in optional if key in obj 
        ):
        return True
    return False


print(is_valid_schema({"username": "vivian", "posts": 1, "verified": False, "role": "user", "supporter": True}))
print(is_valid_schema({"username": "rudolph", "posts": 15, "verified": True, "role": "creator"}))
print(is_valid_schema({"username": "hernandez", "posts": 35, "verified": True, "role": "moderator", "supporter": False, "followers": 55}))
print(is_valid_schema({"username": "julia", "posts": 50, "verified": True, "role": "admin", "supporter": "true"}))
print(is_valid_schema({"username": "bernard", "posts": 0, "verified": True, "role": "friend", "supporter": True}))
print(is_valid_schema({"username": "felix", "posts": 40, "verified": "yes", "role": "staff", "supporter": False}))
print(is_valid_schema({"username": "jimmy", "posts": True, "verified": False, "role": "creator", "supporter": True}))
print(is_valid_schema({"username": True, "posts": 30, "verified": True, "role": "moderator", "supporter": False}))
