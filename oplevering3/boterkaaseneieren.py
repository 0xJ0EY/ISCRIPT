def leesBord(file_location) -> list:
    rows = []

    with open(file_location) as f:
        for line in f:
            rows.append(line.rstrip('\n'))

    return rows

def toonBord(board) -> str:
    lines = []

    for row in board:
        chars = list(row)
        line = ""

        for char in chars:
            if char == " ":
                char = "."

            line += char + " "

        lines.append(line.strip())

    return '\n'.join(lines)

def winnaar(board) -> str:
    winner = find_winner(board)

    if (winner != None):
        return winner + " wint"
    else:
        return "gelijkspel"


def find_winner(board) -> str:
    matrix = []

    for row in board:
        matrix.append(list(row))

    max_x = len(matrix)
    max_y = max_x

    # horizontal
    for x in range(max_x):

        equal = True
        first = None

        for y in range(max_y):
            if (first == None and matrix[x][y] != " "):
                first = matrix[x][y]
                continue

            if (first != matrix[x][y]):
                equal = False
                break

        if equal == True:
            return first

    # vertical
    for y in range(max_y):
        equal = True
        first = None

        for x in range(max_x):
            if (first == None and matrix[x][y] != " "):
                first = matrix[x][y]
                continue

            if (first != matrix[x][y]):
                equal = False
                break

        if equal == True:
            return first

    # cross
    # left top -> right bottom
    if (matrix[0][0] != " "):
        first = matrix[0][0]

        if (matrix[1][1] == first and matrix[2][2] == first):
            return first

    # right top - left bottom
    if (matrix[0][2] != " "):
        first = matrix[0][2]

        if (matrix[1][1] == first and matrix[2][0] == first):
            return first

    return None

            
            






def main():
    # print(leesBord('tictactoe1.txt'))
    # print(leesBord('tictactoe2.txt'))
    # print(leesBord('tictactoe3.txt'))

    # print(toonBord(['OX ', 'OX ', ' X ']))
    # print(toonBord(['OX ', 'OX ', ' X ']))
    # print(toonBord(['XXO', 'OOX', 'XOX']))

    print(winnaar(['OX ', 'OX ', ' X ']))
    print(winnaar(['OOO', ' XX', 'X  ']))
    print(winnaar(['XXO', 'OOX', 'XOX']))

if __name__ == "__main__":
    main()