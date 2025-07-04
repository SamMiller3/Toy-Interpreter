# Toy Interpreter

A complete toy interpreter built from scratch in Python as an educational exploration of language implementation concepts. This project was intentionally developed without referencing formal grammar theory, Abstract Syntax Trees (ASTs), or existing interpreter architectures. Instead, it discovers fundamental compiler and interpreter concepts through hands-on experimentation and creative problem-solving.

The interpreter implements a simple but complete programming language supporting variables, expressions, control flow, and I/O operations. It follows a multi-pass design with distinct tokenization, parsing, and execution phases - patterns that emerged naturally during development rather than being copied from textbooks. 

The philosophy was to learn by rediscovering core concepts rather than implementing established patterns. This approach provides deeper insight into *why* formal methods exist and how language implementation challenges are solved.

## Commands include: 

```
- print()
- input()
- if <condition> {
  # code
  }
- else{
    # code
    }
- goto <value> 
- int <variable name> = <data>
- str <variable name> = <data>
- flt <variable name> = <data>
```

## Features at a glance:
```
- Expression evaluation with proper operator precedence (using Reverse Polish Notation)
- Nested control structures with stack-based management  
- Multi-pass design: tokenization → parsing → execution
- Dynamic typing with explicit type declarations
- Simple but complete language supporting variables, conditionals, loops (via goto), and I/O
```

## Example programs include:
```
The `/Example-Programs` directory contains working examples:
- Fibonacci sequence calculator
- Euclidean algorithm for GCD
- Login System (using nested ifs)
- Mathematical approximations (e.g., approximating e)
- Binary Search guessing game
- Raise base to an exponent
```

## Data types:

```
- Integers
- Floats
- Strings
```

## Explanation of syntax:

### print:

variables can be printed:

```print(num)```

primative datatypes can be printed:

```
print("Hello World!")

print(42)

print(4.2)
```

### Comments

Comments can be made by leaving #

```
# this is a comment
```

### Assigning variables

variables can be assigned their primative datatypes

```
int meaning_of_life = 42
str test = "Hello World!"
flt currency = 99.3
```
note: int, str and flt *must* precede every decleration and each time a value is assigned not just the initial decleration 

variables can also be assigned values of other variables

```
int meaning_of_life = count
str test = name
flt currency = num
```

input can also be prompted from the user and stored to variables

```
int meaning_of_life = input()
str test = input()
flt currency = input()
```

### Expression handling

Expressions can be evaluated respecting BIDMAS
```
int num = count * 3 + 2 
```
Expressions can be used anywhere, for example in if statements, GOTO statements, etc

### Goto statements

GOTO statements can be used to branch to other pieces of code, it can either branch to an immediate line number, an expression, or a variable

```
goto 3
goto 3+count
goto program_counter
```

## If statements

If statements can be used to check the boolean value of a condition

```
if 2 = 2 {
  print("hello world!")
}
```
note: indentation is optional
The start and end of an if statement is signified by { and }

If statements can be used in conjuction with goto statements for conditional branching

```
if count = 10 {
  goto 32 # end of program
}
```

If statements can also be used with else statements 

```
if number = 42 {
  print("correct!")
}
else{
  print("incorrect!")
}
```

Nested if statements can be used to check multiple conditions at once

```
if number = 42 {
  print("correct!")

  if answer = "Hello World"{ # this code will ONLY execute if number = 42
    print("Amazing!")
  else{
    print("At least you got 42..)
  }

}
else{
  print("incorrect!")
}
```






