# Toy Interpreter

A toy interpreter I am currently writing in python from scratch for educational purposes

Commands include: 

```
print()
input()
if{}
else{}
goto
int <variable name> = <data>
str <variable name> = <data>
flt <variable name> = <data>
```

Features:
```
* Expression handling respecting precedence of operations using reverse polish notation
* Nested ifs using if stack
* Tokenisation and parsing before interpreting the parsed representation
```
Data types:

```
* Integers
* Floats
* Strings
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






