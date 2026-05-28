def compute_score(judge_scores, *penalties):
    total_score = sum(judge_scores) - max(judge_scores) - min(judge_scores) - sum(penalties)

    return total_score

print(compute_score([10, 8, 9, 6, 9, 8, 8, 9, 7, 7], 1))
print(compute_score([10, 8, 9, 6, 9, 8, 8, 9, 7, 7], 1))
print(compute_score([10, 8, 9, 10, 9, 8, 8, 9, 10, 7], 1, 2, 1))
print(compute_score([8.0, 8.5, 9.0, 8.5, 9.0, 8.0, 9.0, 8.5, 9.0, 8.5], 0.5, 1.0))
print(compute_score([6.0, 8.5, 7.0, 9.0, 7.5, 8.0, 6.5, 9.5, 7.0, 8.0], 1.5, 0.5, 0.5))
