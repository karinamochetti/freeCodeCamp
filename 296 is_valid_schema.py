def is_valid_schema(obj):
    types = {
        "username": "string", 
        "posts": 0, 
        "verified": True
    }
    if all(key in obj and type(obj[key]) is type(types[key]) for key in types):
        return True
    return False

print(is_valid_schema({"username": "alice", "posts": 10, "verified": False}))
print(is_valid_schema({"username": "carol", "posts": 15, "verified": True, "followers": 25}))
print(is_valid_schema({"username": "frank", "posts": "21", "verified": True}))
print(is_valid_schema({"username": "sam", "posts": 17, "verified": "false"}))
print(is_valid_schema({"username": "bill", "verified": True}))
print(is_valid_schema({"username": "fred", "verified": True}))
print(is_valid_schema({"username": 5, "posts": 10, "verified": True}))
