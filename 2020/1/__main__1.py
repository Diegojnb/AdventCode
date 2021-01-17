import os

limit = 2020

def read_input_file():
    current_path = os.getcwd()
    file = open(current_path + "\\2020\\1\\input.txt", "r")
    input_file_list = []
    for line in file:
        input_file_list.append(line.replace("\n",""))
    return input_file_list

def __main__():
    input_file_list = read_input_file()
    for item_m in input_file_list:
        int_item_m = int (item_m)
        for item_n in input_file_list:
            int_item_n = int (item_n)
            if(int_item_n + int_item_m == limit):
                return int_item_n*int_item_m

print (__main__())
