# wp1.py

# Eugene Ashkinadze
# eashkina@uci.edu
# 36928353

import sys

"""On the first argument inputed, function opens file, and reads it, reversing the information and then
 appending all lines to a list called encrypt_list, calling the update_file function"""
def encrypt(first_file, second_file):
   f = open(first_file, "r")
   info = f.readlines()
   encrypt_list = []
   for i in info:
       i_str = str(i)
       rev_i = i_str[::-1]
       encrypt_list.append(rev_i)
   f.close
   update_file(encrypt_list, second_file) 


"""In the update_file, writes all information in the list to the file. Writing in lines per item in the encrypt_list"""
def update_file(encrypt_list, second_file):
    rewrite = open(second_file, "w")
    rewrite.writelines(encrypt_list)

    

"""When called, collects system commands and sends them to the encrypt function"""
def commands():
    first_file = sys.argv[1]
    second_file = sys.argv[2]
    encrypt(first_file, second_file)

"""Checks to make sure all proper commands are inputted into the program. If test is passed, calls the commands function"""
def main():
    if len(sys.argv) == 3:
        commands()
        #print("Good")
    else:
        print("This file needs 2 inputs")

"""When program is run, call the main function"""
if __name__ == "__main__":
    main()


#print(sys.argv[0])