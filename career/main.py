from input_output_data import *

max_experience = 0
length, positions = unpack()
i = length - 1
stack = []

for j in range(0, len(positions[i])):
    stack.insert(0, [i, j, positions[i][j]])
    while stack:
        current_coord = stack.pop(0)
        current_i = current_coord[0]
        current_j = current_coord[1]
        current_experience = current_coord[2]
        if current_i != 0:
            if current_j == 0:
                stack.insert(0, [current_i - 1, 0, current_experience + positions[current_i - 1][current_j]])
            elif current_j == len(positions[current_i]) - 1:
                stack.insert(0, [current_i - 1, current_j - 1,
                                 current_experience + positions[current_i - 1][current_j - 1]])
            else:
                stack.insert(0, [current_i - 1, current_j, current_experience + positions[current_i - 1][current_j]])
                stack.insert(0, [current_i - 1, current_j - 1,
                                 current_experience + positions[current_i - 1][current_j - 1]])
        else:
            if current_experience > max_experience:
                max_experience = current_experience
                current_experience = 0

output(max_experience)
