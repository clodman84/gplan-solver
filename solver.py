from polyomino.jupyter import solution_to_png
from ingester import read_puzzle
from pathlib import Path
from polyomino.board import Rectangle 

polyominos, board = read_puzzle(Path('./puzzle.txt'))
cover_size = sum(len(poly) for poly in polyominos)
print(cover_size)

solution = Rectangle(x=7, y=6).tile_with(polyominos).solve()
with open("solution.png", "wb") as file:
    file.write(solution_to_png(solution))
