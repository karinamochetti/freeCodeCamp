def email_chain_count(subject):
    subject = subject.lower()
    return subject.count("fwd:") + subject.count("fw:") + subject.count("re:")

print(email_chain_count("Re: Meeting Notes"))
print(email_chain_count("Meeting Notes"))
print(email_chain_count("Re: re: RE: rE: Meeting Notes"))
print(email_chain_count("Re: Fwd: Re: Fw: Re: Meeting Notes"))
print(email_chain_count("re:Ref:fw:re:review:FW:Re:fw:report:Re:FW:followup:re:summary:Fwd:Re:fw:NextStep:RE:FW:re:Project:Fwd:Re:fw:Notes:RE:re:Update:FWD:Re:fw:Summary"))
