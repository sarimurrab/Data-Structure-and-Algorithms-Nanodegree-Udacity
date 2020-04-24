"""
Read file into texts and calls.
It's ok if you don't understand how to read files.
"""
import csv

white_list = []
caller = []


with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    for text in list(reader):
        send, receive, timestamp = text
        white_list.extend([send, receive])  #adding file to white list

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    for call in list(reader):
        call, receive1, timestamp, sec = call
        caller.append(call)
        white_list.append(receive1)


caller = list(set(caller)) #repeated elements are removed using set data strcuture
white_list = list(set(white_list))


annoying_number = set(caller).difference(white_list) #telemarketers = calls minus list of white numbers

print('These numbers could be telemarketers:')
for phone_number in sorted(annoying_number):
    print(phone_number)

"""
TASK 4:
The telephone company want to identify numbers that might be doing
telephone marketing. Create a set of possible telemarketers:
these are numbers that make outgoing calls but never send texts,
receive texts or receive incoming calls.

Print a message:
"These numbers could be telemarketers: "
<list of numbers>
The list of numbers should be print out one per line in lexicographic order with no duplicates.
"""

