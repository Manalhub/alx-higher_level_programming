# 0x12. JavaScript - Warm up

## Table of Contents

- [Description](#description)
- [Learning Objectives](#learning-objectives)
- [Project Tasks](#project-tasks)
  - [0. First constant, first print](#0-first-constant-first-print)
  - [1. 3 languages](#1-3-languages)
  - [2. Arguments](#2-arguments)
  - [3. Value of my argument](#3-value-of-my-argument)
  - [4. Create a sentence](#4-create-a-sentence)
  - [5. An Integer](#5-an-integer)
  - [6. Loop to languages](#6-loop-to-languages)
  - [7. I love C](#7-i-love-c)
  - [8. Square](#8-square)
  - [9. Add](#9-add)
  - [10. Factorial](#10-factorial)
  - [11. Second biggest!](#11-second-biggest)
  - [12. Object](#12-object)
  - [13. Add file](#13-add-file)

## Description

This project covers various JavaScript warm-up tasks aimed at familiarizing you with the basics of the JavaScript programming language. The tasks involve working with variables, functions, loops, conditionals, and more.

## Learning Objectives

By completing this project, one must gain a solid understanding of the following JavaScript concepts:

- Creating variables and constants
- Data types in JavaScript
- Conditional statements (if, if...else)
- Loops (while, for)
- Functions and function parameters
- Handling command-line arguments
- Basic arithmetic operations
- Working with objects
- Basic error handling

---

## Project Tasks

### 0. First constant, first print

Write a script that prints "JavaScript is amazing."

- Create a constant variable called `myVar` with the value "JavaScript is amazing."
- Use `console.log(...)` to print the output.
- You are not allowed to use `var`.

Example:

```shell
$ ./0-javascript_is_amazing.js
JavaScript is amazing
```

### 1. 3 languages

Write a script that prints three lines:

- The first line: "C is fun"
- The second line: "Python is cool"
- The third line: "JavaScript is amazing"

Use `console.log(...)` to print all output. You are not allowed to use `var`.

Example:

```shell
$ ./1-multi_languages.js
C is fun
Python is cool
JavaScript is amazing
```

### 2. Arguments

Write a script that prints a message depending on the number of arguments passed:

- If no arguments are passed to the script, print "No argument."
- If only one argument is passed to the script, print "Argument found."
- Otherwise, print "Arguments found."

Use `console.log(...)` to print all output. You are not allowed to use `var`. Reference: `process.argv`

Example:

```shell
$ ./2-arguments.js
No argument
$ ./2-arguments.js Best
Argument found
$ ./2-arguments.js Best School
Arguments found
```

### 3. Value of my argument

Write a script that prints the first argument passed to it:

- If no arguments are passed to the script, print "No argument."
- Use `console.log(...)` to print all output.
- You are not allowed to use `var`.
- You are not allowed to use `length`.

Example:

```shell
$ ./3-value_argument.js
No argument
$ ./3-value_argument.js School
School
```

### 4. Create a sentence

Write a script that prints two arguments passed to it in the following format: " is "

- Use `console.log(...)` to print all output.
- You are not allowed to use `var`.

Example:

```shell
$ ./4-concat.js c cool
c is cool
$ ./4-concat.js c
c is undefined
$ ./4-concat.js
undefined is undefined
```

### 5. An Integer

Write a script that prints "My number: " followed by the first argument converted to an integer:

- If the argument can't be converted to an integer, print "Not a number."
- Use `console.log(...)` to print all output.
- You are not allowed to use `var`.
- You are not allowed to use try/catch.

Example:

```shell
$ ./5-to_integer.js
Not a number
$ ./5-to_integer.js 89
My number: 89
$ ./5-to_integer.js "89"
My number: 89
$ ./5-to_integer.js 89.89
My number: 89
$ ./5-to_integer.js School
Not a number
```

### 6. Loop to languages

Write a script that prints three lines using an array of strings and a loop:

- The first line: "C is fun"
- The second line: "Python is cool"
- The third line: "JavaScript is amazing"

Use `console.log(...)` to print all output.
You are not allowed to use any if/else statement.
You can use only one `console.log`.
You must use a loop (while, for, etc.).

Example:

```shell
$ ./6-multi_languages_loop.js
C is fun
Python is cool
JavaScript is amazing
```

### 7. I love C

Write a script that prints "C is fun" x times:

- Where x is the first argument of the script.
- If the first argument can't be converted to an integer, print "Missing number of occurrences."
- Use `console.log(...)` to print all output.
- You are not allowed to use `var`.
- You can use only two `console.log`.
- You must use a loop (while, for, etc.).

Example:

```shell
$ ./7-multi_c.js 2
C is fun
C is fun
$ ./7-multi_c.js 5
C is fun
C is fun
C is fun
C is fun
C is fun
$ ./7-multi_c.js
Missing number of occurrences
$ ./7-multi_c.js -3
```

### 8. Square

Write a script that prints a square:

- The first argument is the size of the square.
- If the first argument can't be converted to an integer, print "Missing size."
- Use the character "X" to print the square.
- Use `console.log(...)` to print all output.
- You are not allowed to use `var`.
- You must use a loop (while, for, etc.).

Example:

```shell
$ ./8-square.js
Missing size
$ ./8-square.js School
Missing size
$ ./8-square.js 2
XX
XX
$ ./8-square.js 6
XXXXXX
XXXXXX
XXXXXX
XXXXXX
XXXXXX
XXXXXX
$ ./8-square.js -3
```

### 9. Add

Write a script that prints the addition of two integers:

- The first argument is the first integer.
- The second argument is the second integer.
- Define a function with the prototype `function add(a, b)`.
- Use `console.log(...)` to print all output.
- You are

 not allowed to use `var`.

Example:

```shell
$ ./9-add.js
NaN
$ ./9-add.js 1
NaN
$ ./9-add.js 1 7
8
$ ./9-add.js 13 89
102
```

### 10. Factorial

Write a script that computes and prints a factorial:

- The first argument is an integer used for computing the factorial.
- The factorial of NaN is 1.
- You must implement it recursively.
- You must use a function.
- Use `console.log(...)` to print all output.
- You are not allowed to use `var`.

Example:

```shell
$ ./10-factorial.js
1
$ ./10-factorial.js 3
6
$ ./10-factorial.js 89
1.6507955160908452e+136
$ ./10-factorial.js 333
Infinity
```

### 11. Second biggest!

Write a script that searches for the second biggest integer in the list of arguments:

- You can assume all arguments can be converted to integers.
- If no argument is passed, print 0.
- If the number of arguments is 1, print 0.
- Use `console.log(...)` to print all output.
- You are not allowed to use `var`.

Example:

```shell
$ ./11-second_biggest.js
0
$ ./11-second_biggest.js 1
0
$ ./11-second_biggest.js 4 2 5 3 0 -3
4
```

### 12. Object

Update the provided script to replace the value 12 with 89:

- You are not allowed to use `var`.

Example:

```shell
$ cat 12-object.js
#!/usr/bin/node
const myObject = {
  type: 'object',
  value: 12
};
console.log(myObject);
/*
YOUR CODE HERE
*/
console.log(myObject);
$ ./12-object.js
{ type: 'object', value: 12 }
{ type: 'object', value: 89 }
```

### 13. Add file

Write a function that returns the addition of two integers.

- The function must be visible from outside.
- The name of the function must be `add`.
- You are not allowed to use `var`.

Example:

```shell
$ cat 13-main.js
#!/usr/bin/node
const add = require('./13-add').add;
console.log(add(3, 5));
$ ./13-main.js
8
```

---

**Author:** Guillaume, ALX School

