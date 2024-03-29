'''
Mental Math Program
Console-based program for solving mental math
problems
14 March 2024
'''

import submenus

#total questions practiced
tot_q = 0
# correct count
correct = 0

def main():
    menu = ("1) Addition\n2) Subtraction\n" +  
    "3) Multiplication\n4) Division\n5) Records\n6) Quit")
    # for records - print fastest for each category
    print(menu)
    print('\n Please enter a selection: ')

    sel_1 = input()
    while not sel_1.isdigit():
        print('Please enter a valid int.')
        
        while sel_1 in range(1,7):
            # Addition
            if sel_1 == 1:
                pass

            # Subtraction
            elif sel_1 == 2:
                pass

            # Multiplication
            elif sel_1 == 3:
                pass
            
            # Division
            elif sel_1 == 4:
                pass

            # Records
            elif sel_1 == 5:
                pass 

            elif sel_1 == 6:
                return
            
        sel_1 = input()


main()