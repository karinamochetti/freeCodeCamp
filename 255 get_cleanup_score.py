def get_cleanup_score(items):
    SCORE = {
        "bottle": 10,
        "can": 6,
        "bag": 8,
        "tire": 35,
        "straw": 4,
        "cardboard": 3,
        "newspaper": 3,
        "shoe": 12,
        "electronics": 25,
        "battery": 18,
        "mattress": 38,
    }
    total_score = 0
    streak = 0
    prev_item = ""
    for i, item in enumerate(items):
        if isinstance(item, list):
            value = item[1]
            streak = 0
        else:
            value = SCORE[item]

        if prev_item == item:
            streak += 1
        else:
            streak = 0
            prev_item = item

        mult = 1
        if (i+1)%5 == 0: 
            mult += (i+1)//5

        total_score += (value+streak)*mult
    return total_score

print(get_cleanup_score(["bottle", "straw", "shoe", "battery"]))
print(get_cleanup_score(["electronics", "straw", "newspaper", "bottle", "bag"]))
print(get_cleanup_score(["shoe", "can", "can", "can", "bottle", "bottle", "straw", "straw", "straw"]))
print(get_cleanup_score(["mattress", ["rare", 80], "tire", "tire", "tire", ["rare", 95]]) )
print(get_cleanup_score(["bottle", "can", "can", "shoe", "shoe", ["rare", 56], "bottle", "bottle", "can", "can", "electronics", "bottle", ["rare", 48], "bottle", "can", "can", "can", "can", "can", "can", "can"]))
