import re

# return a list
def digit_sel()->list[int]:
    digits = []
    prompt = input('Select the number of digits for the ' +  
                   'first and second number.ex) 1, 2\n')
    
    match = r'(\d+, \d+)' 
    sel = re.findall(match, prompt)
    if sel:
        print(type(sel))
       # sel.replace(" ", "")
       # digits = sel.split(',')
       # print(digits)
    return digits
    

def addition(d1, d2):
    pass

digit_sel()