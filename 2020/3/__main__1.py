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

def __main__():
    input_file_list = read_input_file()
    current_x = 0
    count = 0
    for line in input_file_list:
        if(is_colision(line, current_x % len(line))):
            count +=1
        current_x += 3
    return count
print (__main__())
