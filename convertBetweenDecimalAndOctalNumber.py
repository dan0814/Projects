"""This file contains two functions.  The first function converts a decimal number to an
octal number and the second function converts an octal number to a decimal number """

# This function converts a decimal number to an octal number
# The user inputs a decimal number
# The function returns the equivalent octal number


def convert_decimal_to_octal(decimal_num):
    # 1ST) PRODUCE EMPTY STRING USED TO HOLD EQUIVALENT OCTAL NUMBER
    octal_num = ""

    # 2ND) CALCULATE INDIVIDUAL TERMS OF EQUIVALENT OCTAL NUMBER AND
    # PLACE THE TERMS INTO "octal_num"
    while decimal_num > 0:
        remainder = decimal_num % 8
        octal_num = octal_num + str(remainder)
        decimal_num = decimal_num // 8

    # 3RD) REARRANGE THE RESULT FROM 2ND STEP (MOST SIGNIFICANT DIGIT TO THE
    # LEAST SIGNIFICANT DIGIT) TO OBTAIN THE EQUIVALENT OCTAL NUMBER AND
    # RETURN THE VALUE
    return octal_num[::-1]


# This function converts an octal number to a decimal number
# The user inputs an octal number
# The function returns the equivalent decimal number


def convert_octal_to_decimal(octal_num):
    # 1ST) PRODUCE A LIST USING USER DEFINED OCTAL NUMBER
    octal_num_list = []
    for x in str(octal_num):
        octal_num_list.append(int(x))

    # 2ND) CALCULATE THE INDIVIDUAL TERMS TO BE SUMMED TO GET THE EQUIVALENT
    # DECIMAL NUMBER AND PUT THE TERMS INTO "num_to_sum"
    num_to_sum = []
    ii = len(octal_num_list) - 1
    for jj in octal_num_list:
        digit = (8**ii) * jj
        num_to_sum.append(digit)
        ii -= 1

    # 3RD) SUM THE VALUES FROM "num_to_sum" TO OBTAIN EQUIVALENT DECIMAL
    # NUMBER
    decimal_num = 0
    for kk in range(len(num_to_sum)):
        decimal_num = decimal_num + int(num_to_sum[kk])

    # 4TH) RETURN THE EQUIVALENT DECIMAL NUMBER
    return decimal_num


# Ex) use first function to convert decimal to octal
print(convert_decimal_to_octal(1264))
# Ex) use second function to convert octal to decimal
print(convert_octal_to_decimal(612))

