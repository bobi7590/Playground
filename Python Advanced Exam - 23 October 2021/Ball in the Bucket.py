def read_matrix(matrix:list):
    for i in range(6):
        line = input().split()
        matrix.append(line)

def hit_B(matrix:list, point_y: int):
    temp_sum = 0
    for i in range(6):
        if matrix[i][point_y] != 'B':
            temp_sum += int(matrix[i][point_y])
    return temp_sum

def end_result(points):
    if points < 100:
        print(f"Sorry! You need {100 - int(points)} points more to win a prize.")
    elif points < 200:
        print(f"Good job! You scored {points} points, and you've won Football.")
    elif points < 300:
        print(f"Good job! You scored {points} points, and you've won Teddy Bear.")
    else:
        print(f"Good job! You scored {points} points, and you've won Lego Construction Set.")

def point_in_matrix(point_x:int, point_y:int):
    return 0<= point_x<=5 and 0<= point_y <=5

matrix = []
points = 0
read_matrix(matrix)
for i in range(3):
    input_str = input()
    (point_x , point_y) = input_str[1:len(input_str)-1].split(', ')
    if point_in_matrix(int(point_x),int(point_y)):
        if matrix[int(point_x)][int(point_y)] == "B":
            points += hit_B(matrix,int(point_y))
end_result(points)


