def get_average_grade(scores):
    average = int(sum(scores)/len(scores))
    grade_scale = [
        (97, "A+"), (93, "A"), (90, "A-"),
        (87, "B+"), (83, "B"), (80, "B-"),
        (77, "C+"), (73, "C"), (70, "C-"),
        (67, "D+"), (63, "D"), (60, "D-")
    ]
    
    for threshold, grade in grade_scale:
        if average >= threshold:
            return grade
            
    return "F"

print(get_average_grade([92, 91, 90, 94, 89, 93]) )
print(get_average_grade([84, 89, 85, 100, 91, 88, 79]))
print(get_average_grade([63, 69, 65, 66, 71, 64, 65]))
print(get_average_grade([97, 98, 99, 100, 96, 97, 98, 99, 100]))
print(get_average_grade([75, 100, 88, 79, 80, 78, 64, 60]))
print(get_average_grade([45, 48, 50, 52, 100, 54, 56, 58, 59]))
