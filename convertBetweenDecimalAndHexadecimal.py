"""This file contains two functions.  The first function converts a decimal number
to a hexadecimal number and the second function converts a hexadecimal number to a
decimal number """

# This function converts a decimal number to a hexadecimal number
# The user inputs a decimal number
# The function returns the equivalent hexadecimal number


def convert_decimal_to_hexadecimal(decimal_num):
    # 1ST) CALCULATE INDIVIDUAL TERMS OF EQUIVALENT HEXADECIMAL NUMBER AND
    # PLACE THE TERMS INTO A LIST NAMED "hexadecimal_num"
    hexadecimal_num = []
    while decimal_num > 0:
        remainder = decimal_num % 16
        hexadecimal_num.append(remainder)
        decimal_num = decimal_num // 16

    # 2ND) REARRANGE THE RESULT FROM 1ST STEP (MOST SIGNIFICANT DIGIT TO THE
    # LEAST SIGNIFICANT DIGIT)
    hexadecimal_num.reverse()

    # 3RD) CONVERT THE INTEGERS 10, 11, 12, 13, 14, AND 15 TO EQUIVALENT LETTER
    for ii in range(len(hexadecimal_num)):
        if hexadecimal_num[ii] == 10:
            hexadecimal_num[ii] = 'A'
        elif hexadecimal_num[ii] == 11:
            hexadecimal_num[ii] = 'B'
        elif hexadecimal_num[ii] == 12:
            hexadecimal_num[ii] = 'C'
        elif hexadecimal_num[ii] == 13:
            hexadecimal_num[ii] = 'D'
        elif hexadecimal_num[ii] == 14:
            hexadecimal_num[ii] = 'E'
        elif hexadecimal_num[ii] == 15:
            hexadecimal_num[ii] = 'F'

    # 4TH) CONVERT "hexadecimal_num" TO STRING AND RETURN THE VALUE
    hexadecimal_number = ''
    for jj in range(len(hexadecimal_num)):
        hexadecimal_number = hexadecimal_number + str(hexadecimal_num[jj])
    return hexadecimal_number


# This function converts a hexadecimal number to a decimal number
# The user inputs a hexadecimal number as a string.  The letters in the hexadecimal
# number can be lower case or capital
# The function returns the equivalent decimal number


def convert_hexadecimal_to_decimal(hexadecimal_num):
    # 1ST) PLACE USER DEFINED HEXADECIMAL NUMBER INTO A LIST
    hexadecimal_num_list = []
    for ii in range(len(hexadecimal_num)):
        hexadecimal_num_list.append(hexadecimal_num[ii])

    # 2ND) CONVERT ALL THE ELEMENTS IN "hexadecimal_num_list" TO INTEGERS
    for ii in range(len(hexadecimal_num_list)):
        if hexadecimal_num_list[ii] == 'A' or hexadecimal_num_list[ii] == 'a':
            hexadecimal_num_list[ii] = 10
        elif hexadecimal_num_list[ii] == 'B' or hexadecimal_num_list[ii] == 'b':
            hexadecimal_num_list[ii] = 11
        elif hexadecimal_num_list[ii] == 'C' or hexadecimal_num_list[ii] == 'c':
            hexadecimal_num_list[ii] = 12
        elif hexadecimal_num_list[ii] == 'D' or hexadecimal_num_list[ii] == 'd':
            hexadecimal_num_list[ii] = 13
        elif hexadecimal_num_list[ii] == 'E' or hexadecimal_num_list[ii] == 'e':
            hexadecimal_num_list[ii] = 14
        elif hexadecimal_num_list[ii] == 'F' or hexadecimal_num_list[ii] == 'f':
            hexadecimal_num_list[ii] = 15
    for ii in range(len(hexadecimal_num_list)):
        hexadecimal_num_list[ii] = int(hexadecimal_num_list[ii])

    # 3RD) CALCULATE THE INDIVIDUAL TERMS TO BE SUMMED TO GET THE EQUIVALENT
    # DECIMAL NUMBER AND PUT THE TERMS INTO "num_to_sum"
        num_to_sum = []
        ii = len(hexadecimal_num_list) - 1
        for jj in hexadecimal_num_list:
            digit = (16**ii) * jj
            num_to_sum.append(digit)
            ii -= 1

    # 4TH) SUM THE VALUES FROM "num_to_sum" TO OBTAIN EQUIVALENT DECIMAL
    # NUMBER
    decimal_num = 0
    for kk in range(len(num_to_sum)):
        decimal_num = decimal_num + int(num_to_sum[kk])

    # 5TH) RETURN THE EQUIVALENT DECIMAL NUMBER
    return decimal_num


# Ex) use the first function to convert decimal to hexadecimal
print(convert_decimal_to_hexadecimal(43785))
# Ex) use the second function to convert hexadecimal to decimal
print(convert_hexadecimal_to_decimal('ab09'))


