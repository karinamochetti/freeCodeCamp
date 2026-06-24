def medication_reminder(medications, current_time):
    MED_SCH = {}

    current_hour = int(current_time[:2])
    current_min = int(current_time[3:])

    for name, hour in medications:
        if name == "Mergeflictamine": 
            med_hour = hour
    MED_SCH[str(int(med_hour[:2])+4)+med_hour[2:]] = "Mergeflictamine"

    if current_hour < 8:
        MED_SCH["08:00"] = "Deployxitrin"
    elif current_hour < 16:
        MED_SCH["16:00"] = "Deployxitrin"

    if current_hour < 7:
        MED_SCH["07:00"] = "Debuggamanizole"
    elif current_hour < 13:
        MED_SCH["13:00"] = "Debuggamanizole"
    else:
        MED_SCH["21:00"] = "Debuggamanizole"

    min_time = min(MED_SCH.keys())

    current = current_hour*60 + current_min
    med = int(min_time[:2])*60 + int(min_time[3:])
    H = (med-current)//60
    M = (med-current)%60

    return f"{MED_SCH[min_time]} in {H}h {M}m"

print(medication_reminder([["Deployxitrin", "08:00"], ["Debuggamanizole", "07:00"], ["Mergeflictamine", "10:00"]], "11:00"))
print(medication_reminder([["Deployxitrin", "08:00"], ["Debuggamanizole", "13:00"], ["Mergeflictamine", "14:00"]], "14:55"))
print(medication_reminder([["Deployxitrin", "08:00"], ["Debuggamanizole", "13:00"], ["Mergeflictamine", "14:00"]], "17:15"))
print(medication_reminder([["Deployxitrin", "08:00"], ["Debuggamanizole", "07:00"], ["Mergeflictamine", "09:00"]], "12:59"))
print(medication_reminder([["Deployxitrin", "08:00"], ["Debuggamanizole", "21:00"], ["Mergeflictamine", "03:00"]], "06:55"))
print(medication_reminder([["Deployxitrin", "08:00"], ["Debuggamanizole", "07:00"], ["Mergeflictamine", "07:30"]], "08:00"))
