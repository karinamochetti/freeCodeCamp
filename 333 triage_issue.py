def triage_issue(title, labels):
    if labels == []:
        if "bug" in title or "error" in title:
            labels.append("bug")
            labels.append("needs triage")
        if "feature" in title or "add" in title:
            labels.append("enhancement")
            labels.append("discussing")
    else:
        if "needs triage" in labels:
            if ("simple" in title or "easy" in title):
                labels.remove("needs triage")
                labels.append("good first issue")
            else:
                labels.remove("needs triage")
                labels.append("help wanted")
        if "discussing" in labels:
            if ("planned" in title or "next" in title):
                labels.remove("discussing")
                labels.append("on the roadmap")
            else:
                labels.remove("discussing")
                labels.append("help wanted")
    if "security" in title:
        labels.append("critical")

    return labels

print(triage_issue("app crashes with error", []))
print(triage_issue("app crashes with error", ["bug", "needs triage"]))
print(triage_issue("add dark mode", []))
print(triage_issue("add dark mode", ["enhancement", "discussing"]))
print(triage_issue("xss security bug", []))
print(triage_issue("security vulnerability in auth", []))
print(triage_issue("easy a11y fix", ["bug", "needs triage"]))
print(triage_issue("planned api migration", ["enhancement", "discussing"]))
print(triage_issue("improve security", ["enhancement", "discussing"]))
