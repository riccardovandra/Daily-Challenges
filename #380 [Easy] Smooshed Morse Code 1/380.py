from requests import get

Morse_code = {
    "a": ".-",
    "b": "-...",
    "c": "-.-.",
    "d": "-..",
    "e": ".",
    "f": "..-.",
    "g": "--.",
    "h": "....",
    "i": "..",
    "j": ".---",
    "k": "-.-",
    "l": ".-..",
    "m": "--",
    "n": "-.",
    "o": "---",
    "p": ".--.",
    "q": "--.-",
    "r": ".-.",
    "s": "...",
    "t": "-",
    "u": "..-",
    "v": "...-",
    "w": ".--",
    "x": "-..-",
    "y": "-.--",
    "z": "--.."
}


def smorse(word):
    smorsed_word = []
    for letter in word:
        # print(letter)
        decode = Morse_code.get(letter)
        # print(decode)
        smorsed_word.append(decode)
    final_word = "".join(smorsed_word)
    return final_word


smorse("sos")
smorse("daily")
smorse("programmer")
smorse("bits")
smorse("three")
