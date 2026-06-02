from collections import defaultdict

def count_medals(winners):
    medals = defaultdict(lambda: {"G": 0, "S": 0, "B": 0})
    
    for gold, silver, bronze in winners:
        medals[gold]["G"] += 1
        medals[silver]["S"] += 1
        medals[bronze]["B"] += 1

    sorted_medals = sorted(
        medals.items(), 
        key=lambda x: (-x[1]["G"], x[0])
    )    

    csv_lines = ["Country,Gold,Silver,Bronze,Total"]
    
    for country, counts in sorted_medals:
        g, s, b = counts["G"], counts["S"], counts["B"]
        csv_lines.append(f"{country},{g},{s},{b},{g + s + b}")
        
    return "\n".join(csv_lines)

print(count_medals([["USA", "CAN", "NOR"], ["NOR", "USA", "CAN"], ["USA", "NOR", "SWE"]]))
print(count_medals([["NOR","SWE","FIN"]]))
print(count_medals([["ITA", "CHN", "CHN"], ["JPN", "ITA", "JPN"]]))
print(count_medals([["USA","CAN","NOR"], ["GER","FRA","ITA"], ["JPN","KOR","CHN"], ["SWE","FIN","NOR"], ["CAN","USA","SWE"], ["FRA","GER","ITA"]]))
print(count_medals([["ESP","ITA","FRA"], ["ITA","ESP","GER"], ["NOR","SWE","FIN"], ["FIN","NOR","SWE"], ["USA","CAN","MEX"], ["CAN","USA","MEX"], ["JPN","KOR","CHN"], ["CHN","JPN","KOR"]]))
print(count_medals([["USA","CAN","GER"], ["NOR","SWE","FIN"], ["USA","NOR","SWE"], ["GER","FRA","ITA"], ["JPN","KOR","CHN"], ["USA","GER","CAN"], ["SWE","NOR","FIN"], ["CAN","USA","NOR"], ["FRA","GER","ITA"], ["JPN","CHN","KOR"], ["SWE","FIN","NOR"], ["GER","ITA","FRA"]]))
