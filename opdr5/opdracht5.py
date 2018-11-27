def dubbels(values):

    # Use a dict to keep check if duplicated values
    values_dict = {}

    for value in values:
        # Check if value exists in the map
        if (value in values_dict):
            values_dict[value] += 1
        else:
            values_dict[value] = 1

    values_list = []

    # If the value has a occurence of 2 or higher,
    # add them to the values_list
    for key, value in values_dict.items():
        if (value > 1):
            values_list.append(key)

    # Sort the list and return the value
    values_list.sort()
    return values_list

def main():
    print(dubbels([3, 9, 4, 3, 8, 7, 3, 4, 2]))
    print(dubbels([1, 2, 3, 4, 5, 6, 7, 8, 9]))
    print(dubbels([8, 6, 9, 5, 7, 4, 8, 3]))
    print(dubbels(['0476-987394', '0498-837493', '0476-987394']))

if __name__ == '__main__':
    main()