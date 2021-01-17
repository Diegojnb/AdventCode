import os

class Passport:
    def __init__(self, byr,iyr,eyr,hgt,hcl,ecl,pid,cid):
        self.byr = byr
        self.iyr = iyr
        self.eyr = eyr
        self.hgt = hgt
        self.hcl = hcl
        self.ecl = ecl
        self.pid = pid
        self.cid = cid

    def validate_byr(self):
        return self.byr != None
    def validate_iyr(self):
        return self.iyr != None
    def validate_eyr(self):
        return self.eyr != None
    def validate_hgt(self):
        return self.hgt != None
    def validate_hcl(self):
        return self.hcl != None
    def validate_ecl(self):
        return self.ecl != None
    def validate_pid(self):
        return self.pid != None
    def validate_cid(self):
        return True
    def is_valid(self):
        return self.validate_byr() and self.validate_iyr() and self.validate_eyr() and self.validate_hgt() and self.validate_hcl() and self.validate_ecl() and self.validate_pid() and self.validate_cid()

def read_input_file():
    current_path = os.getcwd()
    file = open(current_path + "\\2020\\4\\input.txt", "r")
    input_file_list = []
    for line in file:
        input_file_list.append(line.replace("\n",""))
    return input_file_list

def add_info(passport,line):
    line_splited = line.split(" ")
    for field in line_splited:
        field_splited = field.split(":")
        setattr(passport,field_splited[0],field_splited[1])
    return passport

def __main__():
    input_file_list = read_input_file()
    count = 0
    passport = Passport(None,None,None,None,None,None,None,None)
    passport = Passport(None,None,None,None,None,None,None,None)
    for line in input_file_list:
        if(len(line)==0):
            if(passport.is_valid()):
                count +=1
            passport = Passport(None,None,None,None,None,None,None,None)
        else:
            passport = add_info(passport,line)
    if(passport.is_valid()):
        count +=1
    return count

print (__main__())
