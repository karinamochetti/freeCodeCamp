import math

def calculate_start_delays(jump_scores):
    best_score = max(jump_scores)
    return [math.ceil((best_score-score)*1.5) for score in jump_scores]

print(calculate_start_delays([120, 110, 125]))
print(calculate_start_delays([118, 125, 122, 120]))
print(calculate_start_delays([100, 105, 95, 110, 120, 115, 108]))
print(calculate_start_delays([130, 125, 128, 120, 118, 122, 127, 115, 132, 124]))
