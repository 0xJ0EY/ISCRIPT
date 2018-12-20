import math

def samen(prijzen):
    prijzen = list(prijzen)
    item_to_remove = math.floor(len(prijzen) / 4)

    if (item_to_remove != 0):
        prijzen.sort(reverse=True)
        prijzen = prijzen[0:-item_to_remove]

    return round(sum(prijzen), 2)

def groeperen(prijzen):
    prijzen.sort(reverse=True)
    groeperingen = []

    for x in range(math.ceil(len(prijzen) / 4)):
        start = x * 4
        end = start + 4

        groeperingen.append(tuple(prijzen[start:end]))

    return groeperingen

def gegroepeerd(prijzen):
    groeperingen = groeperen(prijzen)
    som = 0

    for x in groeperingen:
        som += samen(x)

    return som

def winst(prijzen):
    return round(samen(prijzen) - gegroepeerd(prijzen), 2)

if __name__ == "__main__":
    prijzen = [3.23, 5.32, 8.23, 2.23, 9.98, 7.43, 6.43, 8.23, 4.23]

    print(samen(prijzen))

    print(groeperen(prijzen))

    print(gegroepeerd(prijzen))

    print(winst(prijzen))


