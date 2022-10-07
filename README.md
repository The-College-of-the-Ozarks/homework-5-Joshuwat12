# Prog1-HW5

Write a program to tackle the following problem. All programming should use good function and variable names and sufficient comments for improved readability.

The user is going to input a shorthand notation for a playing card, following the table below. Your program will output the full name of the card. For example, an input of QS should give an output of Queen of Spades. Your program must follow all of the specifications below the table.


| Card Value | Full Name | Suit | Full Name |
|:-----:|:----:|:----:|:----:|
| A | Ace | S | Spades |
| 2 | Two | D | Diamonds |
| 3 | Three | C | Clubs |
| ... | ... | H | Hearts |
| 9 | Nine |
| T | Ten |
| J | Jack |
| Q | Queen |
| K | King |


- Create a dictionary to store the value abbreviation/full name as key-value pairs, then use this dictionary to help you output.
- Create a dictionary to store the suit abbreviation/full name as key-value pairs, then use this dictionary to help you output.
- Your program should repeat (request input, give output, repeat) until a specific input is given to exit. Your prompt requesting input should say something like "Input card abbreviation or exit" so the user knows how to actually exit the program.
- Your program should validate the input fully. Unless the exit command is given, any other input should be length 2, the first character must be a valid card value, and the second character must be a valid suit. This validation should use 'in' with your defined dictionaries.
- Write a function which takes one parameter (the abbreviated string obtained from the user) and *returns* a string holding the full name of the card.


***Bonus 1***

Allow 10 or T as valid input for the number Ten.


***Bonus 2***

Store all *valid* inputs in a list, and wait to output anything until the exit command is given. Then, output the full names of all given cards before exiting.
