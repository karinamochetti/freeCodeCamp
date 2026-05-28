def get_fastest_speed(times):
    segments = [320, 280, 350, 300, 250]
    speeds = [segment/time for segment, time in zip(segments, times)]
    i = speeds.index(max(speeds))
    return f"The luger's fastest speed was {speeds[i]:.2f} m/s on segment {i+1}."

print(get_fastest_speed([9.523, 8.234, 10.012, 9.001, 7.128]))
print(get_fastest_speed([9.381, 7.417, 9.912, 8.815, 7.284]))
print(get_fastest_speed([8.890, 7.601, 9.093, 8.392, 6.912]))
print(get_fastest_speed([8.490, 7.732, 10.103, 8.489, 6.840]))
print(get_fastest_speed([8.204, 7.230, 9.673, 7.645, 6.508]))
