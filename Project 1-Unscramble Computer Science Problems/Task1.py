"""
Read file into texts and calls.
It's ok if you don't understand how to read files.
"""




tel = [] #defining an empty llist so that I can  store the number here
import csv  
with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    for text in list(reader):
        tel.extend(text[:2])

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    for call in list(reader):
        tel.extend(call[:2])

tel = list(set(tel))  # set data structure don't accept the repeated values
print('There are {} different telephone numbers in the records.'.format(len(tel)))


"""
TASK 1:
How many different telephone numbers are there in the records? 
Print a message:
"There are <count> different telephone numbers in the records."
"""
