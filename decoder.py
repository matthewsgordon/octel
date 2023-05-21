# Function to return a string of decimaL codes from a string
# of octal codes
# Matthew Gordon
# 24840416
# 18/11/21
def decode(code: str) -> str:
    # string to return list of decimal codes as empty string
    decimal_codes = ''
    # split octal codes into a list of codes by space
    octal_codes = code.split(' ')
    # loop through the list of codes
    for octal in octal_codes:
        # set the decimal number to zero
        decimal_number = 0 
        # find the number of digits in the octal
        len_octal = len(octal)
        # octal to decimal function as per
        # https://pencilprogrammer.com/python-programs/convert-octal-to-decimal/
        # for each digit in the octal string
        for digit in octal:
            # decrement to digit length by one
            len_octal = len_octal - 1
            # add eight power len_octal x integer of the digit
            # Python 
            decimal_number += pow(8 , len_octal) * int(digit) 
        # add the decimal number to the string of decimal codes
        # add a space on the end
        decimal_codes = decimal_codes + str(decimal_number) + ' '
    # remove white space from the decimal codes
    return decimal_codes.rstrip()