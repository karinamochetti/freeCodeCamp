import math

def get_itinerary_count(stops):
    n = len(stops)
    dinner0 = (math.factorial(n)*(n-1))
    dinner1 = n*(math.factorial(n-1)*(n-2))
    return dinner0+dinner1

print(get_itinerary_count(["library", "park"]))
print(get_itinerary_count(["library", "park", "arcade"]))
print(get_itinerary_count(["library", "park", "arcade", "store"]))
print(get_itinerary_count(["library", "park", "arcade", "store", "cafe"]))
print(get_itinerary_count(["library", "park", "arcade", "store", "cafe", "market", "museum"]))
