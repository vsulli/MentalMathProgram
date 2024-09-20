# MENTAL MATH PROGRAM

A personal, console-based program for solving mental math
problems - addition, subtraction, multiplication, and division. 

# Future Changes
- add user selection
- GUI
- add column to record for what problem was associated with that best time
    - exclude 0's, 1's, and 2's 
- mode that excludes typing in the answer for faster reviews -  "honor system" - type 1 for correct, 0 for incorrect
- add option for max number (possibly add column for settings and mode: all numbers, range (start - end), honor system/typed)
- add decimals
- add exponents
- add square roots

# Notes

**Generation of digits for each range**
 10 raised to digit power
- 1 digit ~ up to 9 (1 *0 to digit * 10 - 1)
- 2 digits ~ 10 up to 99 (10^1 to 10^digit - 1)
- 3 digits ~ 100 up to 999 (10^2 to 10^digit - 1 )

if digit is 1: 0-9 
    generate random number(0, 10)

else: 
    10-99
    generate random number in this range(10^(digit - 1),(10^digit))
    * don't need -1 for second digit because python doesn't include last number in range anyway

**Timer**

* from datetime import datetime
current_date = datetime.now()

2024-09-07 20:49:44.771948
year-month-day time
    
**Records**
    Shelve - key is a string and data is any arbitrary object
    https://docs.python.org/3/library/shelve.html
    * using a temp variable is faster and uses less memory than opening dict using writeback = True

    https://stackoverflow.com/questions/28132751/shelve-db-type-could-not-be-determined
    * tried opening 'records' with wrong extension

key: username_operation

username_add: [[digit_1,digit_2, fastest_time, date_achieved], [digit_1, digit_2, fastest_time, date_achieved]]
username_sub:
username_multi:
username_div: 

pickle vs shelve vs json
pickle has some drawbacks: slow, unsafe (between sessions and programs), not language agnostic
shelve allows you to access objects like a dictionary and store nearly any Python object, downside is that changing values requires you to assign them to the shelve again
json: text file that anyone can read, secure (no holes between sessions or programs), downside is that in order to store some python objects you'd have to do extra work to conver to json and back

If I were to start this project from scratch I woudl probably choose json instead of shelve due to it being more well-known, able to be modified by text and usable with more languages.