
def isScrikkeljaar(jaar):
    # Kijk of het een schikkeljaar is
    return (jaar % 4 == 0 and jaar % 100 != 0) or jaar % 400 == 0

def main():
    print(isScrikkeljaar(2004))
    print(isScrikkeljaar(2000))
    print(isScrikkeljaar(1704))
    print(isScrikkeljaar(1700))


if __name__ == '__main__':
    main()