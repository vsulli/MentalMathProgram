import classes
import random
import re
import time

# create function to create/ select user
# load from file
user = classes.User('parosomniac', 0, 0)

# return a list
def digit_sel()->list[int]:
    digits = []
    prompt = input('Select the number of digits for the ' +  
                   'first and second number.ex) 1, 2\n')
    
    match = r'(\d+, \d+)' 
    sel = re.findall(match, prompt)
    if sel:
        sel[0].replace(" ", "")
        digits = sel[0].split(',')
    # turns digits to int
    return [int(i) for i in digits]

        
def addition(d1, d2):
    prompt = ''
    while prompt.lower() != 'q':
        prompt = input(str(d1) + ' + ' + str(d2)+'\n')
        user.q += 1
        match = r'\d+'
        sel = re.findall(match, prompt)
        start_time = time.clock()
        if prompt == 'q':
            print('Qs: ' + str(user.q)+'\n'+
                  'Correct: ' + str(user.c)+'\n'+
                  str(round(user.c / user.q*100, 2))+'%\n')
            
            return
        elif sel[0]:
            stop_time = time.clock()
            print(f"Time: {stop_time - start_time} secs")
            if int(sel[0]) == d1 + d2:
                user.c += 1
                print('Correct\n')
            else:
                print('Wrong\nCorrect Answer: ' + str(d1 + d2) + '\n')


def gen_rand_nums(digit_list)->list[int]:
    for i in range(2):
        # single digit 0-9
        if digit_list[i] == 1:
            digit_list[i] = random.randrange(0,10)
        # all other numbers
        else:
            digit_list[i] = random.randrange(10**(digit_list[i] - 1), 10**digit_list[i])
    return digit_list


