import io

def main():
    palindromen = palindroom(input("Lokaal bestand: "))

    for x in palindromen:
        print(x)

def palindroom(file_name):
    palindromen = []
    lines = read_lines_from_file(file_name)

    for line in lines:
        if line == line[::-1]:
            palindromen.append(line)

    return palindromen

def read_lines_from_file(file_name):
    lines = []

    with open(file_name, "r") as f: 
        [lines.append(line.rstrip('\n')) for line in f]

    return lines

if __name__ == "__main__":
    main()