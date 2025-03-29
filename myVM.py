#Initial variables needed for conducting operations
pc = 0
MAX_MEMORY_SIZE = 500
memory = [] * MAX_MEMORY_SIZE
split_ops = []
#Empty dictionary for the input function
dict = {}

#Input file being stored in the list "memory"
with open("myVM_Prog.txt", "r") as file:
    memory = file.readlines()
#Output file to write results to
output_file = open("myVM_Output.txt", "w")


#Functions for the different operators
def add(dest, num1, num2):
    num1 = int(num1)
    num2 = int(num2)
    dest = (num1 + num2)
    output_file.write(str(dest))
    output_file.write("\n")
    print(dest)

def sub(dest, num1, num2):
    num1 = int(num1)
    num2 = int(num2)
    dest = (num1 - num2)
    output_file.write(str(dest))
    output_file.write("\n")
    print(dest)

def mul(dest, num1, num2):
    num1 = int(num1)
    num2 = int(num2)
    dest = (num1 * num2)
    output_file.write(str(dest))
    output_file.write("\n")
    print(dest)

def div(dest, num1, num2):
    num1 = int(num1)
    num2 = int(num2)
    dest = (num1 / num2)
    output_file.write(str(dest))
    output_file.write("\n")
    print(dest)

def sto(dest, x):
    dest = x
    output_file.write(str(dest))
    output_file.write("\n")
    print(dest)

def input(dest):
    dest = input("Input a variable to store: ")

def out(output):
    str = " ".join(output)
    output_file.write(str)
    output_file.write("\n")
    print(str)

def brn(x):
    if x<0:
        output_file.write("The value is negative")
    else:
        output_file.write("The value is not negative")

def brz(x):
    if x==0:
        output_file.write("The value is zero")
    else:
        output_file.write("The value is not zero")

def brp(x):
    if x>0:
        output_file.write("The value is positive")
    else:
        output_file.write("The value is not positive")

def brzp(x):
    if x>=0:
        output_file.write("The value is greater than or equal to zero")
    else:
        output_file.write("The value is less than zero")

def brzn(x):
    if x<=0:
        output_file.write("The value is less than or equal to zero")
    else:
        output_file.write("The value is greater than zero")


output_file.write("Davis Hagle CSCI 4200, Spring 2025")
output_file.write("\n")
output_file.write("**********************************************")
output_file.write("\n")

    
#Iterates through each lines of th ememory list then uses the other list, split ops, to split each line to find which operation is needed
for line in memory:
    split_ops = line.split()
    if(split_ops[0].upper() == "HALT"):
        break
    elif(split_ops[0]==";"):
        continue
    elif(split_ops[0].upper() == "ADD"):
        add(split_ops[1], split_ops[2], split_ops[3])
    elif(split_ops[0].upper() == "SUB"):
        sub(split_ops[1], split_ops[2], split_ops[3])
    elif(split_ops[0].upper() == "MUL"):
        mul(split_ops[1], split_ops[2], split_ops[3])
    elif(split_ops[0].upper() == "DIV"):
        div(split_ops[1], split_ops[2], split_ops[3])
    elif(split_ops[0].upper() == "STO"):
        sto(split_ops[1], split_ops[2])
    elif(split_ops[0].upper() == "IN"):
        input(split_ops[1])
    elif(split_ops[0].upper() == "OUT"):
        out(split_ops[1:])
    elif(split_ops[0].upper() == "BRn"):
        brn(split_ops[1])
    elif(split_ops[0].upper() == "BRz"):
        brz(split_ops[1])
    elif(split_ops[0].upper() == "BRp"):
        brp(split_ops[1])
    elif(split_ops[0].upper() == "BRzp"):
        brzp(split_ops[1])
    elif(split_ops[0].upper() == "BRzn"):
        brzn(split_ops[1])