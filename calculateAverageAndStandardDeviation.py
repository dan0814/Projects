"""This file contains a function that calculates the average and the standard deviation
(sample or population) of a set of numbers """

# This function calculates the average and the standard deviation (sample or population)
# of a set of numbers from a user defined list

# The user inputs two arguments.  The first argument is a list of numbers and the second
# argument ('sample' or 'population') specifies whether the user wants to calculate the
# sample or population standard deviation

# The function outputs the average and the standard deviation (sample or population)


def calculate_avg_and_sd(user_list_of_num, sample_or_population):
    # 1ST) CALCULATE THE AVERAGE
    total_sum_of_list = 0
    for number in user_list_of_num:
        total_sum_of_list = total_sum_of_list + number
    the_average = total_sum_of_list / len(user_list_of_num)

    # 2ND) CALCULATE THE STANDARD DEVIATION
    # determine the numerator used to determine standard deviation
    individual_terms_for_numerator = []
    for number in user_list_of_num:
        term = (number - the_average) ** 2
        individual_terms_for_numerator.append(term)
    total_sum_of_numerator = 0
    for number in individual_terms_for_numerator:
        total_sum_of_numerator = total_sum_of_numerator + number
    # branch used to calculate the sample or population standard deviation
    if sample_or_population == 'sample':
        the_sd = ((total_sum_of_numerator) / (len(user_list_of_num) - 1)) ** 0.5
    if sample_or_population == 'population':
        the_sd = ((total_sum_of_numerator) / (len(user_list_of_num))) ** 0.5

    # 3RD) RETURN RESULT AS TUPLE
    return the_average, the_sd


# Ex) use the function to calculate the average, the sample standard deviation, and the
# population standard deviation
user_list_of_num = [5, 6, 10, 12, 15]

x = 'sample'
the_answer = calculate_avg_and_sd(user_list_of_num, x)
print('The average is', the_answer[0])
print('The sample standard deviation is', the_answer[1])
print()

y = 'population'
the_answer = calculate_avg_and_sd(user_list_of_num, y)
print('The average is', the_answer[0])
print('The population standard deviation is', the_answer[1])
print()
