import io

def main():
    palindroom(input("Lokaal bestand: "))

def palindroom(file_name):
    # Haal de palindromen uit het bestand 
    with open(file_name, "r") as f:
        pd = [l for l in [l.rstrip() for l in f] if l == l[::-1]]

    # Schrijf de palindromen weg
    with open(file_name, "w") as f:
        [print(p, file=f) for p in pd]

if __name__ == "__main__":
    main()