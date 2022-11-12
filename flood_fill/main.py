from input_output_data import *
import queue

width, height, start_row, start_column, color_to_repaint, field = unpack()
color_to_be_repainted = field[start_row][start_column]

my_q = queue.Queue()

my_q.put([start_row, start_column])

while not my_q.empty():
    row, column = my_q.get()
    if field[row][column] != color_to_be_repainted:
        continue
    field[row][column] = color_to_repaint
    if row > 0:
        my_q.put([row - 1, column])
    if row < len(field) - 1:
        my_q.put([row + 1, column])
    if column > 0:
        my_q.put([row, column - 1])
    if column < len(field[0]) - 1:
        my_q.put([row, column + 1])

output(field)
