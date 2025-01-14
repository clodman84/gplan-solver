from pathlib import Path
import itertools

def read_puzzle(path: Path):
    polyominos = []
    board = []
    with open(path) as file:
        for k, plymino in itertools.groupby(file, lambda x: x!='\n'):
            if k:
                poly = []
                for j, row in enumerate(tuple(plymino)[::-1]):
                    for i, character in enumerate(row):
                        if character == '#':
                            poly.append((i, j))
                        elif character == "%":
                            board.append((i, j))
                if poly:
                    polyominos.append(poly)
    return polyominos, board

