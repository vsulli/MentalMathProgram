import re

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
    prompt = input(str(d1) + ' + ' + str(d2)+'\n')
    match = r'\d+'
    sel = re.findall(match, prompt)
    if sel[0]:
        if int(sel[0]) == d1 + d2:
            print('Correct\n')
        else:
            print('Wrong\nCorrect Answer: ' + str(d1 + d2) + '\n')


addition(2, 1)