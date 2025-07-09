def print_number_grid_with_borders():
    num = 1
    rows, cols = 4, 4

    horizontal_border = "+---" * cols + "+"
    
    for i in range(rows):
        print(horizontal_border)
        row = ""
        for j in range(cols):
            row += f"| {num:2}"  # 2-digit padding
            num += 1
        print(row + " |")
    print(horizontal_border)

print_number_grid_with_borders()