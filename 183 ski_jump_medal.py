def ski_jump_medal(distance_points, style_points, wind_comp, k_point_bonus):
    total_score = distance_points + style_points + wind_comp + k_point_bonus
    if total_score > 180.0:
        return "Gold"
    elif total_score > 175.0:
        return "Silver"
    elif total_score > 172.0:
        return "Bronze"
    else:
        return "No Medal"

print(ski_jump_medal(125.0, 58.0, 0.0, 6.0))
print(ski_jump_medal(119.0, 50.0, 1.0, 4.0))
print(ski_jump_medal(122.0, 52.0, -1.0, 4.0))
print(ski_jump_medal(118.0, 50.5, -1.5, 4.0))
print(ski_jump_medal(124.0, 50.5, 2.0, 5.0))
print(ski_jump_medal(119.0, 49.5, 0.0, 3.0))
