def read_matrix(matrix:list,rows,cols):
    for i in range(rows):
        matrix.append([])

    for i in range(rows):
        line = input()
        for j in range(cols):
            matrix[i].append(line[j])

def print_matrix(matrix,rows):
    for i in range(rows):
        print(''.join(matrix[i]))

def find_mouse(matrix:list,rows,cols):
    for i in range(rows):
        for j in range(cols):
            if matrix[i][j] == "M":
                return i,j

def mouse_movement(current_x,current_y,direction):
    if direction == "up":
        current_x -= 1
    elif direction == 'down':
        current_x += 1
    elif direction == 'left':
        current_y -= 1
    elif direction == 'right':
        current_y += 1
    return current_x,current_y

def is_in_matrix(rows,cols, next_x, next_y):
    return 0 <= next_x < rows and 0 <= next_y < cols

def total_cheese_func(matrix:list,rows,cols):
    count = 0
    for i in range(rows):
        for j in range(cols):
            if matrix[i][j] == 'C':
                count += 1
    return count

rows, cols = [int(x) for x in input().split(',')]
matrix = []
read_matrix(matrix,rows,cols)
# print_matrix(matrix,rows,cols)
direction = input()
starting_x , starting_y = find_mouse(matrix,rows,cols)
current_x , current_y = starting_x,starting_y
total_cheese = total_cheese_func(matrix,rows,cols)
current_cheese = 0

while True:
    if direction == 'danger':
        matrix[current_x][current_y] ='M'
    new_x, new_y = mouse_movement(current_x,current_y,direction)
    if not is_in_matrix(rows,cols,new_x,new_y):
        print("No more cheese for tonight!")
        matrix[current_x][current_y] = 'M'
        break
    if matrix[new_x][new_y] == '@':
        direction = input()
        continue
    if matrix[new_x][new_y] == 'C':
        current_cheese += 1
        matrix[new_x][new_y] = '*'
        if total_cheese == current_cheese:
            print("Happy mouse! All the cheese is eaten, good night!")
            matrix[new_x][new_y] = 'M'
            break
    if matrix[new_x][new_y] == 'T':
        matrix[new_x][new_y] = 'M'
        print("Mouse is trapped!")
        break

    matrix[current_x][current_y] = '*'
    current_x,current_y = new_x,new_y
    direction = input()
print_matrix(matrix,rows)
