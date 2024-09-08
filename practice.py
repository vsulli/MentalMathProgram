# learning how to use shelve module

import shelve
from datetime import datetime, timedelta

shelve_file = shelve.open("records2")

# username: [[digits_1, digits_2, fastest_time, date_achieved]]
vsulli_add = [[1, 1, 5, '2024-09-06 20:52:30.462857'], [2, 1, 8, '2024-09-05 20:52:30.462857']]
vsulli_sub = [[1, 1,9, '2024-09-04 20:49:44.771948'], [2, 1, 12, '2024-09-03 20:52:30.462857']]
vsulli_multi =  [[1, 1, 2, '2024-09-02 20:52:30.462857' ], [2, 1,7, '2024-09-01 20:52:30.462857']]
vsulli_div = [[1, 1, 10, '2024-08-31 20:52:30.462857'], [2, 1, 25, '2024-08-30 20:52:30.462857']]

shelve_file['vsulli_add'] = vsulli_add
shelve_file['vsulli_sub'] = vsulli_sub
shelve_file['vsulli_multi'] = vsulli_multi
shelve_file['vsulli_div'] = vsulli_div

shelve_file.close()


# retrieving data stored in the shelf file
shelve_file = shelve.open('records2')


# retrieve the hashmap
vsulli_div = shelve_file['vsulli_div']

print(vsulli_div)

print('-------------------')

# update the data
vsulli_div[0][2] = 13

# syncing makes changes permanent
shelve_file.sync() 

print(vsulli_div)

shelve_file.close()

# deleting data stored at a key
shelve_file = shelve.open('records2')

shelve_file['test'] = [1, 2, 3]

print(f"Keys before deleting = {list(shelve_file.keys())}") 

del shelve_file['test']

print(f"Keys before deleting = {list(shelve_file.keys())}") 

shelve_file.close()
