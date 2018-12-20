def vertaal(woord: str, vertalingen: dict) -> str:
    # Geen vertaling gevonden, geef het woord terug
    if woord.lower() not in vertalingen:
        return woord

    vertaling = vertalingen[woord.lower()]

    # Return full caps words
    if woord == woord.upper():
        return vertaling.upper()

    # Only return capitalized words
    elif woord == woord.capitalize():
        return vertaling.capitalize()

    # None of the above, just return the lowercase word
    else:
        return vertaling.lower()

def geslachtsverandering(zin: str, vertalingen: dict) -> str:
    zin_lower = zin.lower()

    # Loop linear door de zin heen en split op niet alpha characters
    woord = ""
    woorden = []

    for karakter in zin:
        if karakter.isalpha():
            woord += karakter
        else:
            if len(woord) > 0:
                woorden.append(woord)
                woord = "" 

            woorden.append(karakter)

    # Voor als de zin op een alphabetisch karakter eindigt 
    if len(woord) > 0:
        woorden.append(woord)
        
    # Vertaal de zin
    for i, val in enumerate(woorden):
        if val.lower() in vertalingen.keys():
            woorden[i] = vertaal(val, vertalingen)

    return ''.join(woorden)

def geslachtsherstel(zin: str, vertalingen: str) -> str:
    inv_vertalingen = {}

    for k, v in vertalingen.items():
        inv_vertalingen[v] = k

    return geslachtsverandering(zin, inv_vertalingen)

def main() -> None:
    vertalingen = {'hij':'zij', 'broer':'zus'}

    print(vertaal('hij', vertalingen))
    print(vertaal('HIJ', vertalingen))
    print(vertaal('Hij', vertalingen))
    print(vertaal('broer', vertalingen))
    print(vertaal('mijn', vertalingen))

    print(geslachtsverandering('Hij is mijn broer.', vertalingen))
    print(geslachtsherstel('Zij is mijn zus.', vertalingen))

if __name__ == "__main__":
    main()