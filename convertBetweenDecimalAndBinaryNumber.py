"""This file contains two functions.  The first function converts a decimal number
to a binary number and the second function converts a binary number to a decimal
number """

# This function converts a decimal number to a binary number
# The user inputs a decimal number
# The function returns the equivalent binary number


def convert_decimal_to_binary(decimal_num):
    # 1ST) PRODUCE EMPTY STRING USED TO HOLD EQUIVALENT BINARY NUMBER
    binary_num = ""

    # 2ND) CALCULATE INDIVIDUAL TERMS OF EQUIVALENT BINARY NUMBER AND
    # PLACE THE TERMS INTO "binary_num"
    while decimal_num > 0:
        remainder = decimal_num % 2
        binary_num = binary_num + str(remainder)
        decimal_num = decimal_num // 2

    # 3RD) REARRANGE THE RESULT FROM 2ND STEP (MOST SIGNIFICANT BIT TO THE
    # LEAST SIGNIFICANT BIT) TO OBTAIN THE EQUIVALENT BINARY NUMBER AND
    # RETURN THE VALUE
    return binary_num[::-1]


# This function converts a binary number to a decimal number
# The user inputs a binary number
# The function returns the decimal number equiv


def convert_binary_to_decimal(binary_num):
    # 1ST) PRODUCE A LIST USING USER DEFINED BINARY NUMBER
    binary_num_list = []
    for x in str(binary_num):
        binary_num_list.append(int(x))

    # 2ND) CALCULATE THE INDIVIDUAL TERMS TO BE SUMMED TO GET THE EQUIVALENT
    # DECIMAL NUMBER AND PUT THE TERMS INTO "binary_num_list"
    num_to_sum = []
    ii = len(binary_num_list) - 1
    for jj in binary_num_list:
        digit = (2**ii) * jj
        num_to_sum.append(digit)
        ii -= 1

    # 3RD) SUM THE VALUES FROM "binary_num_list" TO OBTAIN EQUIVALENT DECIMAL
    # NUMBER
    decimal_num = 0
    for kk in range(len(num_to_sum)):
        decimal_num = decimal_num + int(num_to_sum[kk])

    # 4TH) RETURN THE EQUIVALENT DECIMAL NUMBER
    return decimal_num


# Ex) use the first function to convert decimal to binary
print(convert_decimal_to_binary(142))
# Ex) use the second function to convert binary to decimal
print(convert_binary_to_decimal(10001110))

