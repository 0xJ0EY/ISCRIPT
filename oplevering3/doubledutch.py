import string

klinkers = ["a", "e", "i", "o", "u"]

def medeklinkers(file_location) -> dict:
    consonants = process_word_list(file_location)

    assert check_rule_1(consonants) and check_rule_2(consonants) and check_rule_3(consonants), "ongeldige vertaling"

    return consonants

# sommige medeklinkers van het alfabet meerdere keren voorkomen in het bestand            
def process_word_list(file_location) -> dict:
    consonants = {}

    with open(file_location) as f:
        for line in f:
            (key, value) = line.split("-")

            key = key.strip()
            value = value.strip()

            if key not in consonants: 
                consonants[key] = value
            else:
                raise AssertionError("ongeldige vertaling")

    return consonants

# een regel een letter bevat die geen medeklinker is
def check_rule_1(consonants):
    return len(set(consonants.keys()) & set(klinkers)) == 0

# een regel een lettergreep bevat die niet begint met de medeklinker op die regel
def check_rule_2(consonants):
    for key, item in consonants.items():
        if (not item.startswith(key)):
            return False

    return True

# niet alle medeklinkers van het alfabet voorkomen in het bestand
def check_rule_3(consonants):
    medeklinkers = set([v for v in list(string.ascii_lowercase) if not v in klinkers])
    keys = set(consonants.keys())

    return (len(medeklinkers & keys) == len(medeklinkers))


def vertaalWoord(word, consonants):

    output = []

    previous_is_vowel = False

    for i, char in enumerate(list(word)):
        is_upper = char.isupper()
        char = char.lower()
        in_vowel = char in klinkers

        item = ""

        if (in_vowel):
            if (previous_is_vowel):
                # Remove last item
                last_item = output.pop()
                item = 'squat' + char + 'h'
                
            else:
                item = char
        else:
            item = consonants[char]

        if (is_upper):
            item = item.capitalize()
    
        output.append(item)
        previous_is_vowel = in_vowel

    return ''.join(output)

def vertaal(sentence, consonants):

# Loop linear door de zin heen en split op niet alpha characters
    word = ""
    words = []

    for char in sentence:
        if char.isalpha():
            word += char
        else:
            if len(word) > 0:
                words.append(vertaalWoord(word, consonants))
                word = "" 

            words.append(char)

    # Voor als de zin op een alphabetisch karakter eindigt 
    if len(word) > 0:
        words.append(word)

    return ''.join(words)

def main():
    dutchLetter = medeklinkers("dutchLetters.txt")
    # print(dutchLetter['s'])
    # print(dutchLetter['q'])
    # print(dutchLetter['d'])
    # print(dutchLetter['e'])

    # print(vertaalWoord('took', dutchLetter))
    # print(vertaalWoord('BAMBOO', dutchLetter))
    # print(vertaalWoord('Yesterday', dutchLetter))

    # print(vertaal('I took a walk to the park yesterday.', dutchLetter))

if __name__ == "__main__":
    main()