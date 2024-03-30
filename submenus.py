import re

#total questions practiced
TOT_Q = 0
# correct count
CORRECT = 0

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
        global TOT_Q
        TOT_Q += 1
        match = r'\d+'
        sel = re.findall(match, prompt)
        if prompt == 'q':
            print('Qs: ' + str(TOT_Q)+'\n'+
                  'Correct: ' + str(CORRECT)+'\n'+
                  str(round(CORRECT/TOT_Q)*100, 2)+'%')
            
            return
        elif sel[0]:
            if int(sel[0]) == d1 + d2:
                global CORRECT
                CORRECT += 1
                print('Correct\n')
            else:
                print('Wrong\nCorrect Answer: ' + str(d1 + d2) + '\n')