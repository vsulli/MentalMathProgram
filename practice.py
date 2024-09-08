# learning how to use shelve module

import shelve
from datetime import datetime, timedelta

shelve_file = shelve.open("records2")

# username: [[operation, fastest time], []]
user_records = {'vsulli_add': [[1, 1, 5, '2024-09-06 20:52:30.462857'], [2, 1, 8, '2024-09-05 20:52:30.462857']], 
'vsulli_sub': [[1, 1,9, '2024-09-04 20:49:44.771948'], [2, 1, 12, '2024-09-03 20:52:30.462857']],
'vsulli_multi': [[1, 1, 2, '2024-09-02 20:52:30.462857' ], [2, 1,7, '2024-09-01 20:52:30.462857']],
'vsulli_div': [[1, 1, 10, '2024-08-31 20:52:30.462857'], [2, 1, 25, '2024-08-30 20:52:30.462857']]}

shelve_file['user_records'] = user_records

shelve_file.close()
