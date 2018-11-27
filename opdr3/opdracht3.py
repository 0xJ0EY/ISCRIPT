def bereken_rondes(ciruit, km_per_ronde, min_per_ronde):

    aantal_rondes = 0
    gerede_km = 0
    gerede_tijd = 0

    aantal_km = 305 if ciruit.lower() != "monaco" else 260.52

    while (gerede_km <= aantal_km and gerede_tijd <= 120):
        gerede_km += km_per_ronde
        gerede_tijd += min_per_ronde
        aantal_rondes += 1

    return aantal_rondes

def bereken_totaal_km(rondes, km_per_ronde):
    return rondes * km_per_ronde

def main():
    plaats = input("Plaats: ")
    afstand = float(input("Afstand in kilometer van een enkele ronde: "))
    gemiddelde_tijd = float(input("Gemiddelde tijd in minuten: "))

    totaal_rondes = bereken_rondes(plaats, afstand, gemiddelde_tijd)
    totaal_km = bereken_totaal_km(totaal_rondes, afstand)

    print("De grote prijs van {} wordt verreden over {} ronden ({:.3f} km).".format(plaats.capitalize(), totaal_rondes, totaal_km))

    
if __name__ == "__main__":
    main()
