def levensverwachting(geslacht: str, roker: bool, sport: int, alcohol: int, fastfood: bool) -> float:
    leeftijd = 70.0

    # Geslacht
    if (geslacht == 'vrouw'):
        leeftijd += 4 
    
    # Roken
    leeftijd += -5 if roker == True else 5

    # Sporten
    leeftijd += -3 if sport <= 0 else 1 * sport

    # Alcohol
    leeftijd -= 0.5 * (alcohol - 7) if alcohol > 7 else -2 if alcohol == 0 else 0 

    # Fastfood
    if (not fastfood):
        leeftijd += 3

    return leeftijd

def main():
    print(levensverwachting(geslacht='man', roker=True, sport=2, alcohol=10, fastfood=True))
    print(levensverwachting(geslacht='man', roker=True, sport=5, alcohol=5, fastfood=True))
    print(levensverwachting(geslacht='vrouw', roker=False, sport=5, alcohol=0, fastfood=False))
    print(levensverwachting(geslacht='vrouw', roker=False, sport=3, alcohol=14, fastfood=True))
    print(levensverwachting(geslacht='man', roker=False, sport=4, alcohol=4, fastfood=False))

if __name__ == "__main__":
    main()