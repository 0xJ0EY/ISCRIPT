import re

def germaniseer(invoer):
    uitvoer = []
    for woord in re.split(" |\t|\n", invoer):
        uitvoer.append(woord.capitalize())

    return ' '.join(uitvoer)

def main():
    print(germaniseer("this is fine"))

if __name__ == "__main__":
    main()