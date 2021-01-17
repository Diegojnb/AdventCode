import os

limit = 2020

class PasswordPolicy:
    def __init__(self, min_range,max_range,letter,password):
        self.min_range = int(min_range)
        self.max_range = int(max_range)
        self.letter = letter
        self.password = password

    def is_valid(self):
        count = 0
        for letter in self.password:
            if(self.letter == letter):
                count +=1
        return count >= self.min_range and count <= self.max_range

def read_input_file():
    current_path = os.getcwd()
    file = open(current_path + "\\2020\\2\\input.txt", "r")
    input_file_list = []
    for line in file:
        input_file_list.append(line.replace("\n",""))
    return input_file_list

def get_password_policy(line):
    line_splited = line.split(":")
    password = line_splited[1].strip()
    policy = line_splited[0]
    policy_splited = policy.split(" ")
    range = policy_splited[0]
    letter = policy_splited[1].strip()
    range_splited = range.split("-")
    min_range = range_splited[0]
    max_range = range_splited[1].strip()
    return PasswordPolicy(min_range,max_range,letter,password)

def __main__():
    input_file_list = read_input_file()
    count = 0
    for line in input_file_list:
        password_policy = get_password_policy(line)
        if(password_policy.is_valid()):
            count += 1
    return count
    
print (__main__())
