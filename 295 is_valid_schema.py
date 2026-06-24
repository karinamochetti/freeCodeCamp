def is_valid_schema(obj):
    if "username" in obj and isinstance(obj["username"],str):
        return True
    return False

print(is_valid_schema({"username": "bob"}))
print(is_valid_schema({"username": "jen", "posts": 30}))
print(is_valid_schema({"username": ""}))
print(is_valid_schema({"username": 7}))
print(is_valid_schema({"posts": 25}))
