"""
Read file into texts and calls.
It's ok if you don't understand how to read files.
"""
import csv
import re





def companies(phone_number): #if a telemarker company calls
    return phone_number[:3] == '140'


def mob(phone_number): #cellphone
    return phone_number[:1] in ['7', '8', '9']

def bangalore_check(phone_number): # If a bangalore bumber
    return phone_number[:5] == '(080)'

landline_phone = re.compile(r'^\((0[0-9]+)\)')
# for pattern matching using regular expression
def land_line(phone_number): # getting land_line 
    return landline_phone.match(phone_number) is not None


def get_area_code(phone_number): #for are code
    if companies(phone_number):
        return '140'
    if mob(phone_number):
        return phone_number[:4]
    if land_line(phone_number):
        return landline_phone.match(phone_number).group(1)
    return ''


with open('calls.csv', 'r') as f:  # by this cuatomatically file is closed
    reader = csv.reader(f)
    calls = list(reader)

    tot__from_bang = 0
    tot_to_bang = 0
    area_codes = []

    for call in calls:
        calling, receiving, timestamp, seconds = call

        if not bangalore_check(calling):
            continue

        area_code = get_area_code(receiving)
        if not area_code:
            continue

        area_codes.append(area_code)
        tot__from_bang += 1

        if bangalore_check(receiving):
            tot_to_bang += 1

area_codes = sorted(list(set(area_codes)))   # set is used to remove repeated values # sorted function used to sort


print('The numbers called by people in Bangalore have codes:')
for area_code in area_codes:
    print(area_code)

bang_bang = '{:,.2%}'.format(tot_to_bang / tot__from_bang)
print('{} percent of calls from fixed lines in Bangalore are calls to other fixed lines in Bangalore.'.format(bang_bang))

"""
TASK 3:
(080) is the area code for fixed line telephones in Bangalore.
Fixed line numbers include parentheses, so Bangalore numbers
have the form (080)xxxxxxx.)

Part A: Find all of the area codes and mobile prefixes called by people
in Bangalore.
 - Fixed lines start with an area code enclosed in brackets. The area
   codes vary in length but always begin with 0.
 - Mobile numbers have no parentheses, but have a space in the middle
   of the number to help readability. The prefix of a mobile number
   is its first four digits, and they always start with 7, 8 or 9.
 - Telemarketers' numbers have no parentheses or space, but they start
   with the area code 140.

Print the answer as part of a message:
"The numbers called by people in Bangalore have codes:"
 <list of codes>
The list of codes should be print out one per line in lexicographic order with no duplicates.

Part B: What percentage of calls from fixed lines in Bangalore are made
to fixed lines also in Bangalore? In other words, of all the calls made
from a number starting with "(080)", what percentage of these calls
were made to a number also starting with "(080)"?

Print the answer as a part of a message::
"<percentage> percent of calls from fixed lines in Bangalore are calls
to other fixed lines in Bangalore."
The percentage should have 2 decimal digits
"""
