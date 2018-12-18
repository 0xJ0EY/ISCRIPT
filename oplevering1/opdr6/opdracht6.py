def rot(step, string):
    characters = []

    for char in list(string):
        if (not char.isalpha()):
            characters.append(char)
            continue

        if (char.isupper()):
            characters.append(rot_upper_case(step, char))
        else:
            characters.append(rot_lower_case(step, char))

    return "".join(characters)


def rot_upper_case(step, char):
    return rot_decrypt(step, char, ord("A"), ord("Z"))


def rot_lower_case(step, char):
    return rot_decrypt(step, char, ord("a"), ord("z"))

'''
Function to decrypt a rot encoded string 
'''
def rot_decrypt(step, char, begin, end):
    possible_steps = 1 + end - begin
    step = possible_steps - step

    current_steps = (ord(char) - begin + step) % possible_steps
    return chr(begin + current_steps)

'''
Function to encrypt a rot string, not used in this program
'''
def rot_encrypt(step, char, begin, end):
    possible_steps = 1 + end - begin
    current_steps = (ord(char) - begin + step) % possible_steps
    return chr(begin + current_steps)


def main():
    n = int(input("Aantal rotaties: "))
    string = input("Geëncodeerde string: ")

    print(rot(n, string))


if __name__ == "__main__":
    main()
