# Toy interpreter 26/06/25 to 30/06/25
# For reference I didn't base this on any architecture I just made it up as I went along creatively for fun
# To rediscover concepts and more of a challenge

import os

# Expression evaluation using reverse polish notation
def evaluate_expression(expression):
    """
    Evaluates mathematical expressions by converting infix notation to RPN using Shunting Yard Algorithm
    Then evaluates the RPN expression and returns the result
    """
    
    # First preprocess the expression - remove whitespace and newlines
    expression = expression.replace(" ", "")
    expression = expression.replace("\n", "")

    # Tokenize the expression into numbers/variables and operators
    tokens = []
    current = ""

    for char in expression:
        if char in "+-*/":
            if current:
                tokens.append(current)
                current = ""
            tokens.append(char)
        else:
            current += char

    if current:
        tokens.append(current)

    # Apply the Shunting Yard Algorithm to convert from infix notation to RPN 
    operator_stack = []
    operator_queue = []

    # Define operator precedence (higher number = higher precedence)
    precedence = {
        "*": 1,
        "/": 1,
        "+": 0,
        "-": 0
    }
    
    for token in tokens:
        if token[0].isalpha():  # Token is a variable
            operator_queue.append(data[token])  # Queue the variable's value
        elif token[0].isdecimal():  # Token is a number
            if "." in token:
                operator_queue.append(float(token))
            else:
                operator_queue.append(int(token))
        elif token == "*" or token == "+" or token == "-" or token == "/":  # Token is an operator
            if operator_stack == []:
                operator_stack.append(token)
            elif precedence[token] >= precedence[operator_stack[-1]]:  # If greater than or equal precedence then push
                operator_stack.append(token)
            else:  # Otherwise pop and queue
                value = operator_stack.pop()
                operator_queue.append(value)
                operator_stack.append(token)

    # Pop remaining operators from stack to queue
    for i in range(len(operator_stack)):
        operator_queue.append(operator_stack.pop())
    
    # Evaluate the RPN expression
    RPN_stack = []

    for i in range(len(operator_queue)):
        if type(operator_queue[i]) == int or type(operator_queue[i]) == float:  # If it's a number, push to stack
            RPN_stack.append(operator_queue[i])
        else:  # If it's an operator, pop two operands and apply operation
            operation = operator_queue[i]
            operand2 = RPN_stack.pop()
            operand1 = RPN_stack.pop()
            output = 0
            
            if operation == "*":
                output = operand1 * operand2
            elif operation == "+":
                output = operand1 + operand2
            elif operation == "-":
                output = operand1 - operand2
            elif operation == "/":
                output = operand1 / operand2
                
            RPN_stack.append(output)
    
    return RPN_stack[0]


# Main interpreter starts here

# Get file input from user
print("Enter the name of the file with the code to run.")
print("Note it must be in the same directory")
file_name = input("Enter file name: ")

# Read the source code file
script_dir = os.path.dirname(__file__)  # Folder of the script
file_path = os.path.join(script_dir, file_name)
code = open(file_path)

# remove leading whitespace and replace blank lines with # so their 0 index can be checked while keeping them
# to respect goto statements

lines = [line.lstrip() if line.strip() else '#' for line in code.readlines()]

# Token generation - parse source code into instructions and values
instructions = []  # Stores instruction types (p, vi, vs, vf, if, etc.)
values = []        # Stores the values/parameters for each instruction

for i in range(len(lines)):
    current_line = lines[i]

    # Parse print statements - eg print("hello world")
    if current_line[0:5] == "print":
        instructions.append("p")

        if current_line[-1] == "\n":
            values.append(current_line[6:-2])
        else:
            values.append(current_line[6:-1])
            
    # Parse integer variable declarations - eg int count = 3
    elif current_line[0:3] == "int":
        instructions.append("vi")
        variable_name = ""
        j = 4
        while current_line[j] != "=":
            if current_line[j] != " ":
                variable_name += current_line[j]
            j += 1
        value = ""
        j += 1
        for k in range(j, len(current_line)):
            if current_line[k] != " ":
                value += current_line[k]
        if value[-1] == "\n":
            value = value[:-1]
        values.append(f"{variable_name},{value}")
        
    # Parse string variable declarations - eg str name = "Bob"
    elif current_line[0:3] == "str":
        instructions.append("vs")
        variable_name = ""
        j = 4
        while current_line[j] != "=":
            if current_line[j] != " ":
                variable_name += current_line[j]
            j += 1
        value = ""
        j += 1
        flag = False  # Flag to track if we're inside a string (don't strip whitespace inside strings)
        for k in range(j, len(current_line)):
            if current_line[k] != " " and flag == False:
                value += current_line[k]
            elif flag == True:
                value += current_line[k]
            if current_line[k] == '"':
                flag = True
        if value[-1] == "\n":
            value = value[:-1]
        values.append(f"{variable_name},{value}")
        
    # Parse float variable declarations - eg flt currency = 3.2
    elif current_line[0:3] == "flt":
        instructions.append("vf")
        variable_name = ""
        j = 4
        while current_line[j] != " ":
            variable_name += current_line[j]
            j += 1
        value = ""
        j += 2
        for k in range(j, len(current_line)):
            if current_line[k] != " ":
                value += current_line[k]
        if value[-1] == "\n":
            value = value[:-1]
        values.append(f"{variable_name},{value}")
        
    # Parse if statements - eg if name = "John" {
    elif current_line[0:2] == "if":
        j = 2
        value = ""
        flag = False  # Flag to track if we're inside a string
        
        # Get first value (left side of comparison)
        while current_line[j] != "=" and current_line[j] != ">" and current_line[j] != "<":
            if current_line[j] != " " and flag == False:
                value += current_line[j]
            elif flag == True:
                value += current_line[j]
            if current_line[j] == '"':
                flag = True
            j += 1
            
        # Store the comparison operator (=, >, <)
        instructions.append("if" + current_line[j])
        j += 1
        value += ","
        
        # Get second value (right side of comparison)
        while current_line[j] != "{":
            if current_line[j] != " " and flag == False:
                value += current_line[j]
            elif flag == True:
                value += current_line[j]
            if current_line[j] == '"':
                flag = True
            if current_line[j] == '"' and flag == True:
                flag = False
            j += 1
            
        k = i

        # Find end of if statement (handling nested ifs)
        end = False
        ifs_left = 0  # Track nesting depth
        while not end:
            k += 1
            if ifs_left == 0 and lines[k][0] == "}":  # Make sure } doesn't correspond to a nested if
                end = True
            if ifs_left > 0 and lines[k][0] == "}":
                ifs_left -= 1
            if lines[k][0:2] == "if" or lines[k][0:4] == "else":
                ifs_left += 1
        value += "," + str(k)
        values.append(value)
        
    # Parse closing braces
    elif current_line[0] == "}":
        instructions.append("}")
        values.append("")
        
    # Parse goto statements - eg goto 3 or goto num
    elif current_line[0:4] == "goto":
        current_line = current_line[4:]
        current_line = current_line.replace(" ", "")
        current_line = current_line.replace("\n", "")
        instructions.append("goto")
        values.append(current_line)

    elif current_line[0:4] == "else":
        instructions.append("else")
        values.append("")

    else:
        # Empty instruction for unrecognized lines
        instructions.append("")
        values.append("")


# Execution phase
data = {}          # Dictionary to store variable values
if_stack = []      # Stack to handle nested if statements and control flow
i = 0              # Instruction pointer

while i < len(instructions):
    # Execute print instruction
    if instructions[i] == "p":
        value = values[i]
        if value[0] == '"':  # Print string literal
            print(values[i][1:-1])
        elif value[0].isdecimal():  # Print number or expression
            if "+" in value or "-" in value or "/" in value or "*" in value:
                value = evaluate_expression(value)
                print(value)
            else:
                print(value)
        else:  # Print variable value or evaluate expression with variables
            if "+" in value or "-" in value or "/" in value or "*" in value:
                value = evaluate_expression(value)
            else:
                print(data[value])
    
    # Execute string variable assignment
    elif instructions[i] == "vs":
        variable_name = ""
        j = 0
        while values[i][j] != ",":
            variable_name += values[i][j]
            j += 1
        j += 1
        value = values[i][j:]
        
        if value[0] == '"':  # String literal assignment - eg str name = "Bob"
            value = value[1:-1]
            data[variable_name] = value
        elif len(value) >= 7 and value[0:7] == "input()":  # String input
            data[variable_name] = input("enter string: ")
        else:  # Variable assignment - eg str name = name_entered
            data[variable_name] = data[value]
        
    # Execute integer variable assignment
    elif instructions[i] == "vi":
        variable_name = ""
        j = 0
        while values[i][j] != ",":
            variable_name += values[i][j]
            j += 1
        j += 1
        value = values[i][j:]
        
        if "+" in value or "-" in value or "/" in value or "*" in value:  # Expression assignment
            data[variable_name] = int(evaluate_expression(value))
        elif value[0].isdecimal():  # Integer literal - eg int num = 3
            data[variable_name] = int(value)
        elif len(value) >= 7 and value[0:7] == "input()":  # Integer input
            data[variable_name] = int(input("enter int: "))
        else:  # Variable assignment - eg int num = fib
            data[variable_name] = int(data[value])
            
    # Execute float variable assignment
    elif instructions[i] == "vf":
        variable_name = ""
        j = 0
        while values[i][j] != ",":
            variable_name += values[i][j]
            j += 1
        j += 1
        value = values[i][j:]
        
        if "+" in value or "-" in value or "/" in value or "*" in value:  # Expression assignment
            data[variable_name] = float(evaluate_expression(value))
        elif value[0].isdecimal():  # Float literal - eg flt currency = 3.2
            data[variable_name] = float(value)
        elif len(value) >= 7 and value[0:7] == "input()":  # Float input
            data[variable_name] = float(input("enter float: "))
        else:  # Variable assignment - eg flt currency = num
            data[variable_name] = float(data[value])
            
    # Handle closing brace (end of if block)
    elif instructions[i] == "}":
        if len(if_stack) > 0:
            i = if_stack.pop()
            
    # Execute if statement (handles =, >, < comparisons)
    elif instructions[i][0:2] == "if":
        # Parse the two values to compare
        value1 = ""
        j = 0
        while values[i][j] != ",":
            value1 += values[i][j]
            j += 1
        j += 1
        value2 = ""
        while values[i][j] != ",":
            value2 += values[i][j]
            j += 1
        endif = values[i][j+1:]
        if endif[-1] == "\n":
            endif = endif[:-1]
        endif = int(endif)
        
        # Convert value1 to appropriate type
        if value1[0].isalpha():  # Variable or expression with variables
            if "+" in value1 or "-" in value1 or "/" in value1 or "*" in value1:
                value1 = evaluate_expression(value1)
            else:
                value1 = data[value1]
        elif value1[0].isdecimal() and "." not in value1:  # Integer
            if "+" in value1 or "-" in value1 or "/" in value1 or "*" in value1:
                value1 = evaluate_expression(value1)
            else:
                value1 = int(value1)
        elif value1[0].isdecimal():  # Float
            if "+" in value1 or "-" in value1 or "/" in value1 or "*" in value1:
                value1 = evaluate_expression(value1)
            else:
                value1 = float(value1)
        else:  # String literal
            value1 = value1[1:-1]
            
        # Convert value2 to appropriate type
        if value2[0].isalpha():
            if "+" in value2 or "-" in value2 or "/" in value2 or "*" in value2:
                value2 = evaluate_expression(value1)
            else:
                value2 = data[value2]
        elif value2[0].isdecimal() and "." not in value2:
            if "+" in value2 or "-" in value2 or "/" in value2 or "*" in value2:
                value2 = evaluate_expression(value1)
            else:
                value2 = int(value2)
        elif value2[0].isdecimal():
            if "+" in value2 or "-" in value2 or "/" in value2 or "*" in value2:
                value2 = evaluate_expression(value1)
            else:
                value2 = float(value2)
        else:
            value2 = value2[1:-1]

        # Check if it is an if-else statement
        elseFlag = False
        if endif < len(instructions)-1 and instructions[endif+1] == "else":
            endif += 1
            elseFlag = True

        # Evaluate the condition and jump if false
        if instructions[i][2] == "=" and value1 != value2:  # If condition is not true, skip over the block
            i = endif
        elif instructions[i][2] == ">" and value1 <= value2: 
            i = endif 
        elif instructions[i][2] == "<" and value1 >= value2: 
            i = endif
        else:  # Statement is true, but if it's an else statement, skip over the else block
            if elseFlag == True:
                j = endif
                while instructions[j] != "}" and ifs_left == 0:
                    j += 1
                if_stack.append(j)  # When we reach next }, update i to go to last location in if_stack
                
    # Execute goto statement
    if instructions[i] == "goto":
        value = values[i]
        if "+" in value or "-" in value or "/" in value or "*" in value:  # Goto expression result
            i = evaluate_expression(value) - 1
        elif value.isdecimal():  # Goto line number
            i = int(value) - 1
        else:  # Goto variable value
            i = data[value] - 1
        
    i += 1
