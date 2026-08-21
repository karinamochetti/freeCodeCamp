def decode_morse(code):
    MORSE = {
        ".-": "A", "-.": "N",
        "-...": "B", "---": "O",
        "-.-.": "C", ".--.": "P",
        "-..": "D", "--.-": "Q",
        ".": "E", ".-.": "R",
        "..-.": "F", "...": "S",
        "--.": "G", "-": "T",
        "....": "H", "..-": "U",
        "..": "I", "...-": "V",
        ".---": "J", ".--": "W",
        "-.-": "K", "-..-": "X",
        ".-..": "L", "-.--": "Y",
        "--": "M", "--..": "Z",
    }
    str = ""
    words = code.split("   ")
    for word in words:
        letters = word.split(" ")
        for letter in letters:
            str += MORSE[letter]
        str += " "
    return str[:-1]

print(decode_morse("--.."))
print(decode_morse("... --- ..."))
print(decode_morse("..-. .-. . . -.-. --- -.. . -.-. .- -- .--."))
print(decode_morse(".... . .-.. .-.. ---   .-- --- .-. .-.. -.."))
print(decode_morse("- .... .   --.- ..- .. -.-. -.-   -... .-. --- .-- -.   ..-. --- -..-   .--- ..- -- .--. . -..   --- ...- . .-.   - .... .   .-.. .- --.. -.--   -.. --- --."))
