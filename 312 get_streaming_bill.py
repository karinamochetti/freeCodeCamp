def get_streaming_bill(cart, subscription):
    COST = {
        "HD": {"rent": 3.99, "buy": 12.99,},
        "4K": {"rent": 5.99, "buy": 19.99,},
    }
    DISCOUNT = {
        "none": 1.0,
        "basic": 0.9,
        "premium": 0.75,
    }

    price = sum(COST[movie["format"]][movie["type"]]*DISCOUNT[subscription] for movie in cart)

    return f"${round(price, 2):.2f}"


print(get_streaming_bill([{ "format": "HD", "type": "rent" }], "none"))
print(get_streaming_bill([{ "format": "HD", "type": "rent" }, { "format": "HD", "type": "buy" }], "premium"))
print(get_streaming_bill([{ "format": "HD", "type": "rent" }, { "format": "HD", "type": "rent" }, { "format": "HD", "type": "buy" }], "basic"))
print(get_streaming_bill([{ "format": "4K", "type": "buy" }, { "format": "4K", "type": "buy" }], "premium"))
print(get_streaming_bill([{ "format": "HD", "type": "rent" }, { "format": "4K", "type": "rent" }, { "format": "HD", "type": "buy" }, { "format": "4K", "type": "buy" }], "none"))
print(get_streaming_bill([{ "format": "HD", "type": "rent" }, { "format": "4K", "type": "rent" }, { "format": "HD", "type": "buy" }, { "format": "4K", "type": "buy" }, { "format": "HD", "type": "buy" }], "basic"))
