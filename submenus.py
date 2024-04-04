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
 
def gen_rand_nums(digit_list)->list[int]:
    # make a copy of digits selected
    copy_list = list(digit_list)
    for i in range(2):
        # single digit 0-9
        if copy_list[i] == 1:
            copy_list[i] = random.randrange(0,10)
        # all other numbers
        else:
            copy_list[i] = random.randrange(10**(copy_list[i] - 1), 10**copy_list[i])
    # returns 2 random numbers
    return copy_list 

def math_operation(symbol):
    prompt = ''
    correct_ans = None # change to none type to start?
    digits = []
    digits = digit_sel()

    while prompt.lower() != 'q':

        # generate random number with desired # digits
        nums = gen_rand_nums(digits)
        global start_time
        start_time = time.time()

        #TODO input validation for letters
        if symbol == '+':
            prompt = input(str(nums[0]) + ' + ' + str(nums[1]) + ' = \n')
            correct_ans = nums[0] + nums[1]
        elif symbol == '-':
            prompt = input(str(nums[0]) + ' - ' + str(nums[1]) + ' = \n')
            correct_ans = nums[0] - nums[1]
        elif symbol == 'x':
            prompt = input(str(nums[0]) + ' x ' + str(nums[1]) + ' = \n')
            correct_ans = nums[0] * nums[1]
        elif symbol == '/':
            prompt = input(str(nums[0]) + ' / ' + str(nums[1]) + ' = \n')
            correct_ans = nums[0] / nums[1]

        match = r'\d+'
        sel = re.findall(match, prompt)

        if prompt.lower() == 'q':
            print('==========================')
            print('Qs: ' + str(user.q)+'\n'+
                  'Correct: ' + str(user.c)+'\n'+
                  str(round(user.c / user.q*100, 2))+'%')
            print('==========================')
            # reset values
            user.c = 0
            user.q = 0
            return
        
        elif sel[0]:
            global stop_time
            stop_time = time.time()
            print("Time: " + str(round(stop_time - start_time, 2)) + " secs")
            
            # correct answer
            if (int(sel[0]) == correct_ans or (symbol == '-' and -int(sel[0]) == correct_ans)):
                user.c += 1
                user.q += 1
                print('Correct')
                print('-----------------------')
            
            # incorrect answer
            else:
                user.q += 1
                print('Wrong')
                print('Correct Answer: ' + str(correct_ans))
                print('-----------------------')