'''
Mental Math Program
Console-based program for solving mental math
problems
14 March 2024
'''

import submenus

def main():
    menu = ("1) Addition\n2) Subtraction\n" +  
    "3) Multiplication\n4) Division\n5) Records\n6) Quit")
    # for records - print fastest for each category
    print(menu)
    print('\n Please enter a selection: ')

    sel_1 = input()
    while sel_1 != 6:
        if not sel_1.isdigit() or int(sel_1) not in range(1,7):
            print('Please enter a valid int.')
            pass

        if sel_1.isdigit():
            sel_1 = int(sel_1)

        # Addition
        if sel_1 == 1:
            nums = submenus.digit_sel()
            submenus.addition(nums[0], nums[1])
            print(menu)

        # Subtraction
        if sel_1 == 2:
            pass

        # Multiplication
        if sel_1 == 3:
            pass
        
        # Division
        if sel_1 == 4:
            pass

        # Records
        if sel_1 == 5:
            pass 

        if sel_1 == 6:
            return
            
        sel_1 = input()


main()