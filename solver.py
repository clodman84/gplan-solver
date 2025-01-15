from polyomino.jupyter import solution_to_png
from ingester import read_puzzle
from pathlib import Path
from polyomino.board import Rectangle 

polyominos, board = read_puzzle(Path('./puzzle.txt'))
cover_size = sum(len(poly) for poly in polyominos)
if cover_size < len(board):
    polyominos += [[(0, 0)]] * (len(board) - cover_size)

solutions = Rectangle(x=7, y=6).tile_with(polyominos).get_all_solutions()

for i, solution in enumerate(solutions):
    print(f"writing solution {i}")
    with open(f"solution_{i}.png", "wb") as file:
        file.write(solution_to_png(solution))
