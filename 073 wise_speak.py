def wise_speak(sentence):
    VERBS = ["have", "must", "are", "will", "can"]
    for verb in VERBS:
        if verb in sentence:
            verb_index = sentence.find(verb)
            verb_len = len(verb)
            break
    prefix = sentence[verb_index+verb_len+1:-1].capitalize()
    suffix = sentence[0:verb_index+verb_len].lower()
    pontuation = sentence[-1]
    result = prefix + ", " + suffix + pontuation
    return result

print(wise_speak("You must speak wisely."))
print(wise_speak("You can do it!"))
print(wise_speak("Do you think you will complete this?"))
print(wise_speak("All your base are belong to us."))
print(wise_speak("You have much to learn."))
