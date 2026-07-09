def triage_issue(ms, message):
    SEVEN_DAYS_MS = 7*24*60*60*1000
    if ms < SEVEN_DAYS_MS: return "leave it"
    elif "bump" in message.lower(): return "close it"
    return "bump it"

print(triage_issue(86400000, "Lets fix it"))
print(triage_issue(1209600000, "still waiting"))
print(triage_issue(864000000, "bump"))
print(triage_issue(604800000, "Do we still want this?"))
print(triage_issue(604800000, "Bumping this"))
print(triage_issue(345600000, "I'll make a PR"))
