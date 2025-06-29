# toy interpreter 26/06/25
# for reference I didn't base this on any architecture I just made it up as I went along creatively for fun
# to rediscover concepts and more of a challenge
# example syntax: 
# print("hello world")
# int count = 3
# str name = "Bob"
# str name = input()
# flt currency = 3.2
# if currency > 3.1 { 
# print("yes")
# }
# function add(int1,int2){
# return(int1+int2)
# }



# expression evaluation using reverse polish notation

def evaluate_expression(expression):


import os


print("Enter the name of the file with the code to run.")
print("Note it must be in the same directory")
file_name=input("Enter file name: ")

script_dir = os.path.dirname(__file__)  # Folder of the script
file_path = os.path.join(script_dir, file_name)
code = open(file_path)
lines=code.readlines()

# Token generation
instructions=[]
values=[]
for i in range(len(lines)):
    current_line=lines[i]
    if current_line[0:5]=="print": # eg print("hello world")
        instructions.append("p")
        if current_line[-1]=="\n":
            values.append(current_line[6:-2])
        else:
            values.append(current_line[6:-1])
    elif current_line[0:3]=="int": # int count = 3
        instructions.append("vi")
        variable_name=""
        j=4
        while current_line[j]!="=":
            if current_line[j]!=" ":
                variable_name+=current_line[j]
            j+=1
        value=""
        j+=1
        for k in range(j,len(current_line)):
            if current_line[k]!=" ":
                value+=current_line[k]
        if value[-1]=="\n":
            value=value[:-1]
        values.append(f"{variable_name},{value}")
    elif current_line[0:3]=="str": # str name = "Bob"
        instructions.append("vs")
        variable_name=""
        j=4
        while current_line[j]!="=":
            if current_line[j]!=" ":
                variable_name+=current_line[j]
            j+=1
        value=""
        j+=1
        flag=False # flag inside a string? if so it is not whitespace so don't strip
        for k in range(j,len(current_line)):
            if current_line[k]!=" " and flag==False:
                value+=current_line[k]
            elif flag==True:
                value+=current_line[k]
            if current_line[k]=='"':
                flag=True
        if value[-1]=="\n":
            value=value[:-1]
        values.append(f"{variable_name},{value}")
    elif current_line[0:3]=="flt": # flt currency = 3.2
        instructions.append("vf")
        variable_name=""
        j=4
        while current_line[j]!=" ":
            variable_name+=current_line[j]
            j+=1
        value=""
        j+=2
        for k in range(j,len(current_line)):
            if current_line[k]!=" ":
                value+=current_line[k]
        if value[-1]=="\n":
            value=value[:-1]
        values.append(f"{variable_name},{value}")
    elif current_line[0:2]=="if":
        j=2
        value=""
        flag = False # flag inside a string? if so it is not whitespace so don't strip
        while current_line[j]!="=" and current_line[j]!=">" and current_line[j]!="<": # get first value so if >>name<< = "John" {
            if current_line[j]!=" " and flag==False:
                value+=current_line[j]
            elif flag==True:
                value+=current_line[j]
            if current_line[j]=='"':
                flag=True
            j+=1
        instructions.append("if" + current_line[j])
        j+=1
        value+=","
        while current_line[j]!="{": # get second value so if name = >>"John"<< {
            if current_line[j]!=" " and flag==False:
                value+=current_line[j]
            elif flag==True:
                value+=current_line[j]
            if current_line[j]=='"':
                flag=True
            if current_line[j]=='"' and flag==True:
                flag=False
            j+=1
        k=i

        # find end of if statement
        end=False # flag to show whether the end has been reached
        ifs_left = 0 # shows how deep in a nested if we are from the initial if
        while not end:
            k+=1
            if ifs_left == 0 and lines[k][0]=="}": # need to make sure } does not correspond to a nested if
                end=True
            if ifs_left>0 and lines[k][0]=="}":
                ifs_left-=1
            if lines[k][0:2]=="if":
                ifs_left+=1
        k+=1
        value+=","+str(k)
        values.append(value)
    elif lines[i][0]=="}":
        instructions.append("}")
        values.append("")
    else:
        instructions.append("")
        values.append("")


# Execution
data = {}
if_stack = []
i=0
while i<len(instructions):
    if instructions[i]=="p":
        if values[i][0]=='"':
            print(values[i][1:-1])
        elif values[i][0].isdecimal():
            print(values[i])
        else: # otherwise it is a variable
            print( data[values[i]] )
    
    elif instructions[i]=="vs":
        variable_name=""
        j=0
        while values[i][j]!=",":
            variable_name+=values[i][j]
            j+=1
        j+=1
        value=values[i][j:]
        if value[0]=='"': # eg str name = "Bob"
            value=value[1:-1]
            data[variable_name]=value
        elif len(value)>=7 and value[0:7]=="input()":
            data[variable_name]=input("enter string: ")
        else: # eg str name = name_entered
              data[variable_name]=data[value]
        
    elif instructions[i]=="vi":
        variable_name=""
        j=0
        while values[i][j]!=",":
            variable_name+=values[i][j]
            j+=1
        j+=1
        value=values[i][j:]
        if value[0].isdecimal(): # eg int num = 3
            data[variable_name]=int(value)
        elif len(value)>=7 and value[0:7]=="input()":
            data[variable_name]=int(input("enter int: "))
        else: # eg int num = fib
              data[variable_name]=int(data[value])
    elif instructions[i]=="vf":
        variable_name=""
        j=0
        while values[i][j]!=",":
            variable_name+=values[i][j]
            j+=1
        j+=1
        value=values[i][j:]
        if value[0].isdecimal(): # eg flt currency = 3.2
            data[variable_name]=float(value)
        elif len(value)>=7 and value[0:7]=="input()":
            data[variable_name]=float(input("enter float: "))
        else: # eg int currency = num
              data[variable_name]=float(data[value])
    elif instructions[i]=="}":
        if len(if_stack)>0:
            i=if_stack.pop()
    elif instructions[i][0:2]=="if":
        value1=""
        j=0
        while values[i][j]!=",":
            value1+=values[i][j]
            j+=1
        j+=1
        value2=""
        while values[i][j]!=",":
            value2+=values[i][j]
            j+=1
        endif=values[i][j+1:]
        if endif[-1]=="\n":
            endif=endif[:-1]
        endif=int(endif)
        if value1[0].isalpha(): # means it must be an identifier
            value1=data[value1]
        elif value1[0].isdecimal() and "." not in value1: # must be an int
            value1=int(value1)
        elif value1[0].isdecimal(): # must be a float
            value1=float(value1)
        else: # otherwise it is a string
            value1=value1[1:-1]
        if value2[0].isalpha():
            value2=data[value2]
        elif value2[0].isdecimal() and "." not in value2:
            value2=int(value2)
        elif value2[0].isdecimal():
            value2=float(value2)
        else:
            value2=value2[1:-1]

        # check if it is an if else statement
        elseFlag=False
        if endif<len(instructions)-1 and lines[endif+1][0:4]=="else":
            endif+=1
            elseFlag=True

        if instructions[i][2]=="=" and value1!=value2: # if condition is not true skip over the block, otherwise continue as usual
            i = endif
        elif instructions[i][2]==">" and value1<=value2: 
            i = endif
        elif instructions[i][2]=="<" and value1>=value2: 
            i = endif
        else: # therefore statement is true but if it is an else statement skip over the else block
            if elseFlag==True:
                j=endif
                while instructions[j]!="}":
                    j+=1
                if_stack.append(j) # when reach next } and update i to go to last location in if_stack
        
    i+=1
        
        
