def scoresToevoegen(totaal: dict, toevoegen: dict) -> None:
    for k, v in toevoegen.items():
        if k in totaal:
            totaal[k] += v
        else:
            totaal[k] = v


def scoresTonen(scoreLijst: dict, aantal: int = -1) -> list:
    if (aantal < 0): aantal = len(scoreLijst)

    items = list(scoreLijst.items())

    items.sort(key = lambda x: x[0])
    items.sort(key = lambda x: x[1], reverse = True)

    return items[:aantal]


def main():
    scorebord = {}
    scores_UK = {'Lithuania': 7, 'Russia': 3, 'Estonia': 4, 'Azerbaijan': 2, 'Sweden': 12, 'Turkey': 1, 'Spain': 8, 'Germany': 6, 'Malta': 5, 'Ireland': 10}
    scores_HU = {'Albania': 8, 'Russia': 7, 'Iceland': 6, 'Italy': 5, 'Sweden': 12, 'Turkey': 3, 'Spain': 1, 'Germany': 10, 'Serbia': 4, 'Moldova': 2}

    print(scoresToevoegen(scorebord, scores_UK))

    print(scoresTonen(scorebord))

    print(scoresToevoegen(scorebord, scores_HU))

    print(scoresTonen(scorebord, 3))

if __name__ == "__main__":
    main()