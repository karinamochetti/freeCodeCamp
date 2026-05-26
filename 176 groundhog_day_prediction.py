def groundhog_day_prediction(appearance):
    if not isinstance(appearance, bool):
        return "No prediction this year."
    if appearance:
        return "Looks like we'll have six more weeks of winter."
    if not appearance:
        return "It's going to be an early spring."

print(groundhog_day_prediction(True))
print(groundhog_day_prediction(False))
print(groundhog_day_prediction(None))
print(groundhog_day_prediction(" "))
print(groundhog_day_prediction("True"))
