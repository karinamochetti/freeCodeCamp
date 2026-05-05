def can_post(message):
    if len(message) <= 40: return "short post"
    elif len(message) > 80: return "invalid post"
    else: return "long post"
    
print(can_post("Hello world"))
print(can_post("This is a longer message but still under eighty characters."))
print(can_post("This message is too long to fit into either of the character limits for a social media post."))
