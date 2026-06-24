def get_open_issues(issues, prs):
    prs_sorted = [sorted(f"{pr:04d}") for pr in prs]
    closed = [issue for issue in issues if sorted(f"{issue:04d}") not in prs_sorted or issue in prs]
    return closed

print(get_open_issues([123, 234], [231]))
print(get_open_issues([123, 345, 16], [345, 231]))
print(get_open_issues([456, 332, 12, 15], [201, 945, 180]))
print(get_open_issues([12, 115, 296, 170, 24], [17, 18, 19, 20, 21]))
print(get_open_issues([19, 95, 422, 395, 754, 102, 296, 709, 237, 4400, 1802], [395, 440, 9001, 95, 242, 21, 287, 169, 14]) )
