def is_inside(row, col, size):
    return 0 <= row < size and 0 <= col < size


def move_next_position(row, col, direction):
    if direction == 'up':
        return row - 1, col
    elif direction == 'down':
        return row + 1, col
    elif direction == 'left':
        return row, col - 1
    elif direction == 'right':
        return row, col + 1


num_of_presents = int(input())
size_of_neighborhood = int(input())
santa_row = 0
santa_col = 0
nice_kids_number = 0
nice_kids_with_presents = 0
directions = ["up", "down", "left", "right"]
matrix_neighborhood = []
for _ in range(size_of_neighborhood):
    row = input().split()
    matrix_neighborhood.append(row)
for i in range(size_of_neighborhood):
    for j in range(size_of_neighborhood):
        if matrix_neighborhood[i][j] == 'S':
            santa_row = i
            santa_col = j
        elif matrix_neighborhood[i][j] == 'V':
            nice_kids_number += 1
presents_finished = False
command = input()
while command != 'Christmas morning' and num_of_presents > 0:
    next_row, next_col = move_next_position(santa_row, santa_col, command)
    if is_inside(next_row, next_col, size_of_neighborhood):
        if matrix_neighborhood[next_row][next_col] == 'X':
            matrix_neighborhood[santa_row][santa_col] = '-'
            matrix_neighborhood[next_row][next_col] = 'S'
        elif matrix_neighborhood[next_row][next_col] == 'V':
            nice_kids_with_presents += 1
            num_of_presents -= 1

            matrix_neighborhood[santa_row][santa_col] = '-'
            matrix_neighborhood[next_row][next_col] = 'S'
        elif matrix_neighborhood[next_row][next_col] == '-':
            matrix_neighborhood[santa_row][santa_col] = '-'
            matrix_neighborhood[next_row][next_col] = 'S'
        elif matrix_neighborhood[next_row][next_col] == 'C':
            matrix_neighborhood[santa_row][santa_col] = '-'
            matrix_neighborhood[next_row][next_col] = 'S'
            for direction in directions:
                n_row, n_col = move_next_position(next_row, next_col, direction)
                if is_inside(n_row, n_col, size_of_neighborhood):
                    if matrix_neighborhood[n_row][n_col] == 'V':
                        nice_kids_with_presents += 1
                        num_of_presents -= 1
                        matrix_neighborhood[n_row][n_col] = '-'
                    elif matrix_neighborhood[n_row][n_col] == 'X':
                        num_of_presents -= 1
                        matrix_neighborhood[n_row][n_col] = '-'
                # elif matrix_neighborhood[n_row][n_col] == '-':
                #     continue
                    if num_of_presents <= 0:
                        if nice_kids_number > 0:
                            print("Santa ran out of presents!")
                            presents_finished = True
                            break
        if presents_finished:
            break

        if num_of_presents <= 0:
            if nice_kids_number > 0:
                print("Santa ran out of presents!")
            break
    santa_row = next_row
    santa_col = next_col

    command = input()

for row in matrix_neighborhood:
    print(*row, sep=' ')
if nice_kids_number - nice_kids_with_presents <= 0:
    print(f"Good job, Santa! {nice_kids_with_presents} happy nice kid/s.")
else:
    print(f"No presents for {nice_kids_number - nice_kids_with_presents} nice kid/s.")


