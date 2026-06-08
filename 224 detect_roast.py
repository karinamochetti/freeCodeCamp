def detect_roast(beans):
    beans = beans.replace("'","1").replace("-","2").replace(".","3")
    points = [int(bean) for bean in beans]
    average = sum(points)/len(points)
    if average < 1.75: return "Light"
    if 1.75 <= average <= 2.5: return "Medium"
    if average > 2.5: return "Dark"

print(detect_roast("''-''''''-'-''--''''"))
print(detect_roast(".'-''-''..'''.-.-''-"))
print(detect_roast("--.''--'-''.--..-.--"))
print(detect_roast("-...'-......-..-...-"))
print(detect_roast(".--.-..-......----.'"))
print(detect_roast("..-..-..-..-....-.-."))
print(detect_roast("-'-''''''..-'.''-'.'"))
