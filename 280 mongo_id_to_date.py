import datetime

def mongo_id_to_date(s):
    dt = datetime.datetime.fromtimestamp(int(s[:8], 16), tz=datetime.UTC)
    print(int(s[:8], 16))
    return dt.replace(tzinfo=None).isoformat(timespec='milliseconds') + "Z"

print(mongo_id_to_date("6a094b50bcf86cd799439011"))
print(mongo_id_to_date("695344eb1f4a4c1123042128"))
print(mongo_id_to_date("386da62df34123ac54617e56"))
print(mongo_id_to_date("69f571c3d7711807afd3dd55"))
print(mongo_id_to_date("68adce01c0e1144d0a90295a"))
