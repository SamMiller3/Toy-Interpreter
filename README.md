# Toy Interpreter

A toy interpreter I am currently writing in python 

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
* Expression handling respecting precedence of operations
* Nested ifs
* Functions w/ recursion
* Tokenisation and parsing before interpreting the parsed representation
```
Data types:

```
* Integers
* Floata
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

### Assigning variables

variables can be assigned their primative datatypes

```
int meaning_of_life = 42
str test = "Hello World!"
flt currency = 99.3
```
note: int, str and flt must precede every decleration and each time a value is assigned 

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

## Expression handling

Expressions can be evaluated respecting BIDMAS
```
int num = count * 3 + 2 
```
Expressions can be used anywhere, for example in if statements, GOTO statements, etc



