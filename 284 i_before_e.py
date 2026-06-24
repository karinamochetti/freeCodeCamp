import re

def i_before_e(sentence):
    sentence = sentence.replace("cie", "cei")
    indices = [match.start() for match in re.finditer("ei", sentence)]
    for i in indices:
        if i > 0 and sentence[i-1] != "c":
            print(sentence[i-1:i+2])
            sentence = sentence[:i] + sentence[i:].replace("ei", "ie", 1)
    return sentence

print(i_before_e("beleive"))
print(i_before_e("recieve"))
print(i_before_e("we recieved a breif"))
print(i_before_e("she beleived the friendly niece could percieve the greif"))
print(i_before_e("we recieved relief after the theif gave us a breif piece of feirce deceit"))


#she believed the friendly niece could perceive the grief
#she believed the friendly niece could percieve the grief