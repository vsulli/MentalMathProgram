# MENTAL MATH PROGRAM

# TODO LIST
- fix timer for submenu
- add subtraction
- add multiplication
- add division
- add try/catch - error handling
- add user selection
- format records.txt

category; time; problem; digits_1; digits_2
* of digits in first number, # of digits in 2nd number

 # TODO - have to figure out a way to generate ranges based on digits?
    # multiplied by 10? --- 10 raised to digit power
    # 1 digit ~ up to 9 (1 *0 to digit * 10 - 1)
    # 2 digits ~ 10 up to 99 (10^1 to 10^digit - 1)
    # 3 digits ~ 100 up to 999 (10^2 to 10^digit - 1 )

    if digit is 1: 0-9 
    generate random number(0, 10)

    else: 
    10-99
    generate random number in this range(10^(digit - 1),(10^digit))
    * don't need -1 for second digit because python doesn't include last number in range anyway

    * Fixing the timer
    https://diveintopython.org/learn/date/time
    Have to create a timer module?