def get_semifinal_matchups(teams):
    points = []
    for team in teams:
        name, record = team.split(":")
        record_values = record[1:].split("-")
        total = int(record_values[0])*3 + int(record_values[1])*2 + int(record_values[2])
        points.append((total, name))
    points = sorted(points)
    return f"The semi-final games will be {points[-1][1]} vs {points[-4][1]} and {points[-2][1]} vs {points[-3][1]}."


print(get_semifinal_matchups(["CAN: 2-2-0-1", "FIN: 2-2-1-0", "GER: 1-0-1-3", "SUI: 0-1-3-1", "SWE: 1-1-2-1", "USA: 2-1-0-2"]))
print(get_semifinal_matchups(["CAN: 2-1-1-1", "CZE: 1-1-1-2", "FIN: 1-2-1-1", "NOR: 0-1-1-3", "SLO: 1-0-1-3", "USA: 5-0-0-0"]))
print(get_semifinal_matchups(["CAN: 3-2-0-0", "CZE: 2-1-2-0", "LAT: 0-0-1-4", "ITA: 1-1-1-2", "DEN: 1-0-0-4", "USA: 3-1-1-0"]))
print(get_semifinal_matchups(["AUT: 2-2-1-0", "DEN: 1-0-0-4", "ITA: 1-1-1-2", "JPN: 3-2-0-0", "KOR: 2-1-2-0", "LAT: 0-0-1-4"]))
