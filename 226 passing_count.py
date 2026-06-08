def passing_count(scores, passing_score):
    return sum(1 if score >= passing_score else 0 for score in scores)

print(passing_count([90, 85, 75, 60, 50], 70))
print(passing_count([100, 80, 75, 88, 72, 74, 79, 71, 60, 92], 75))
print(passing_count([79, 60, 88, 72, 74, 59, 75, 71, 80, 92], 60))
print(passing_count([76, 79, 80, 70, 71, 65, 79, 78, 59, 72], 85))
print(passing_count([84, 65, 98, 53, 58, 71, 91, 80, 92, 70, 73, 83, 86, 69, 84, 77, 72, 58, 69, 75, 66, 68, 72, 96, 90, 63, 88, 63, 80, 67], 60))
