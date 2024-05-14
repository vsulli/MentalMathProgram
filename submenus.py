import classes
import random
import re
import shelve
import time

# create function to create/ select user
# load from file
user = classes.User('test', 0, 0)

# return a list
def digit_sel()->list[int]:
    digits = []
    prompt = input('Select the number of digits for the ' +  
                   'first and second number.ex) 1, 2\n')
    
    match = r'(\d+, \d+)' 
    sel = re.findall(match, prompt)
    try:
        if sel:
            sel[0].replace(" ", "")
            digits = sel[0].split(',')
        # turns digits to int
    except:
        print("Invalid Format")
        
    return [int(i) for i in digits]
 
def gen_rand_nums(digit_list)->list[int]:
    # make a copy of digits selected
    copy_list = list(digit_list)
    rand_num = 0

    for i in range(2):
        # single digit  -9 -> 9 excluding 0
        if digit_list[i] == 1:
            # can't have division by 0 in 2nd position
            if i == 1:
                while rand_num == 0:
                    rand_num = random.randrange(-9,9)
                copy_list[i] = rand_num 
            else:
                rand_num = random.randrange(-9,9)
                copy_list[i] = rand_num
            # have to reset rand_num 
            rand_num = 0
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
        
        # matches negative number | negative number.number | number | number.number
        match = r"[-+]?\d*\.?\d+|[-+]?\d+"
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
            # for division need to check if matches rounded to 1 decimal point
            # TODO check this line - may not be getting correct selection with sel[0]?
            if float(sel[0]) == correct_ans or round(float(sel[0]), 2) == round(correct_ans, 2):
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

def modify_record(file, key, value):
    record_dict = shelve.open(file) 
    curr_val = record_dict[key]
    # don't update if current record exists and has lower time
    if curr_val[0] and curr_val[0] < value[0]:
        return
    #when you open dict without writeback=True, have to do the following:
    temp = record_dict[key]             # extracts the copy
    temp.append(value)             # mutates the copy
    record_dict[key] = temp             # stores the copy right back, to persist it
    record_dict.close()

def retrieve_record(file):
    record_dict = shelve.open(file)

