"""
Read file into texts and calls.
It's ok if you don't understand how to read files.
"""
import csv
with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    send, receive, time_stamp = list(reader)[0]  #at index zero
    print('First one from text_dataset , {} texts {} at  {}'.format(send,receive,time_stamp))


with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    call, receive, time_stamp, sec = list(reader)[-1] # -1 is for last index 
    print('Last one from call_dataset, {} calls {} at time {}, lasting {} seconds'.format(call,receive,time_stamp,sec))


"""
TASK 0:
What is the first record of texts and what is the last record of calls?
Print messages:
"First record of texts, <incoming number> texts <answering number> at time <time>"
"Last record of calls, <incoming number> calls <answering number> at time <time>, lasting <during> seconds"
"""

