def levensverwachting(geslacht, roker=, sport=2, alcohol=10, fastfood=True):
    leeftijd = 70

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