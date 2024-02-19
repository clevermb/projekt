import random

def create_board():
    board = [[0] * 4 for _ in range(4)]
    nums = list(range(1, 16))
    random.shuffle(nums)
    nums_iter = iter(nums)
    for i in range(4):
        for j in range(4):
            try:
                board[i][j] = next(nums_iter)
            except StopIteration:
                # Jeśli iterator został wyczerpany, przerwij pętlę
                break
    return board

def print_board(board):
    for row in board:
        print(" | ".join("{:2}".format(num) if num != 0 else "  " for num in row))
        print("-" * 29)

def get_blank_position(board):
    # Znajdowanie pozycji pustego pola
    for i in range(4):
        for j in range(4):
            if board[i][j] == 0:
                return i, j

def is_valid_move(board, move):
    i, j = get_blank_position(board)
    if move == "W":
        return i != 0
    elif move == "S":
        return i != 3
    elif move == "A":
        return j != 0
    elif move == "D":
        return j != 3

def make_move(board, move):
    i, j = get_blank_position(board)
    if move == "W":
        board[i][j], board[i - 1][j] = board[i - 1][j], board[i][j]
    elif move == "S":
        board[i][j], board[i + 1][j] = board[i + 1][j], board[i][j]
    elif move == "A":
        board[i][j], board[i][j - 1] = board[i][j - 1], board[i][j]
    elif move == "D":
        board[i][j], board[i][j + 1] = board[i][j + 1], board[i][j]

def is_solved(board):
    return all(board[i][j] == i * 4 + j + 1 for i in range(4) for j in range(4)) and board[3][3] == 0

def main():
    board = create_board()
    print("Witaj w grze Piętnastka!")
    while True:
        print_board(board)
        move = input("Wpisz ruch (W - góra, S - dół, A - lewo, D - prawo, Q - wyjście): ").upper()
        if move == "Q":
            print("Dziękujemy za grę!")
            break
        if move in ("W", "S", "A", "D"):
            if is_valid_move(board, move):
                make_move(board, move)
                if is_solved(board):
                    print_board(board)
                    print("Gratulacje! Ułożyłeś planszę!!!")
                    break
            else:
                print("Nieprawidłowy ruch. Spróbuj ponownie.")
        else:
            print("Nieprawidłowy ruch. Spróbuj ponownie.")

if __name__ == "__main__":
    main()