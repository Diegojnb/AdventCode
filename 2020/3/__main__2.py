import os

tree = "#"

def read_input_file():
    current_path = os.getcwd()
    file = open(current_path + "\\2020\\3\\input.txt", "r")
    input_file_list = []
    for line in file:
        input_file_list.append(line.replace("\n",""))
    return input_file_list

def is_colision(line,x):
    return line[x] == tree

def custom_slope(input_file_list,x_slope,y_slope):
    count = 0
    current_x = 0
    for i in range(0,len(input_file_list),y_slope):
        line = input_file_list[i]
        if(is_colision(line, current_x % len(line))):
            count +=1
        current_x += x_slope
    return count

def __main__():
    input_file_list = read_input_file()
    result = 1
    result = result * custom_slope(input_file_list,1,1)
    result = result * custom_slope(input_file_list,3,1)
    result = result * custom_slope(input_file_list,5,1)
    result = result * custom_slope(input_file_list,7,1)
    result = result * custom_slope(input_file_list,1,2)
    return result
print (__main__())
