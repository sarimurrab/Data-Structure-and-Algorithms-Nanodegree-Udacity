"""
Read file into texts and calls.
It's ok if you don't understand how to read files
"""
import csv
with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    tot = {}

    for call in list(reader):
        caller, receive, timestamp, sec = call
        sec = int(sec)

        tot[caller] = tot[caller] + sec if caller in tot else sec
        tot[receive] = tot[receive] + sec if receive in tot else sec

# Retrieve the key (telephone number) of the largest value (duration)
phone = max(tot.keys(), key=(lambda k: tot[k]))

print('{} spent the longest time, {} seconds, on the phone during September 2016.'.format(phone,tot[phone]))

"""
TASK 2: Which telephone number spent the longest time on the phone
during the period? Don't forget that time spent answering a call is
also time spent on the phone.
Print a message:
"<telephone number> spent the longest time, <total time> seconds, on the phone during 
September 2016.".
"""

