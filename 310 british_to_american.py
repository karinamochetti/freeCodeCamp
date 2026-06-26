def british_to_american(sentence):
    BRIT_AME = {
        "colour": "color",
        "flavour": "flavor",
        "honour": "honor",
        "neighbour": "neighbor",
        "labour": "labor",
        "humour": "humor",
        "centre": "center",
        "fibre": "fiber",
        "defence": "defense",
        "offence": "offense",
        "organise": "organize",
        "recognise": "recognize",
        "analyse": "analyze",
    }

    for word in BRIT_AME.keys():
        sentence = sentence.replace(word, BRIT_AME[word])
        sentence = sentence.replace(word.upper(), BRIT_AME[word].upper())
        sentence = sentence.replace(word.capitalize(), BRIT_AME[word].capitalize())

    return sentence

print(british_to_american("I love the colour blue."))
print(british_to_american("The fibre optic cable is new."))
print(british_to_american("It's an honour to meet someone with such humour."))
print(british_to_american("The unrecognised artist analysed his colour palette at the centre."))
print(british_to_american("The offence analysed, with organisation, the defence centre and recognised that the neighbouring labouror was humourous, flavourful, and colourful."))
