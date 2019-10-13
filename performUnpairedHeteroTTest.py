"""This file contains a function that calculates the results of an unpaired
heteroscedastic t test (t(calc) and degrees of freedom).  The two values can
be compared to critical t values to determine if p value is small (~0.05) """

# This function performs an unpaired heteroscedastic t test and returns the t(calc)
# value and the degrees of freedom.  The two values can be compared to critical t values
# to determine whether the difference between two means of two data sets is significant

# The user inputs two arguments.  The first argument is a list containing data points
# for one set of measurements and the second argument is a list containing data points
# for another set of measurements.

# The function returns the t(calc) value and the degrees of freedom


def perform_unpaired_hetero_t_test(data_set1, data_set2):
    import math
    # 1ST) CALCULATE THE MEANS
    # determine the first mean
    sum_of_data_set1 = 0
    for number in data_set1:
        sum_of_data_set1 = sum_of_data_set1 + number
    mean_data_set1 = sum_of_data_set1 / len(data_set1)
    # determine the second mean
    sum_of_data_set2 = 0
    for number in data_set2:
        sum_of_data_set2 = sum_of_data_set2 + number
    mean_data_set2 = sum_of_data_set2 / len(data_set2)

    # 2ND) CALCULATE THE NUMERATOR FOR T(CALC)
    t_calc_numerator = mean_data_set1 - mean_data_set2

    # 3RD) CALCULATE THE STANDARD DEVIATIONS
    # determine the first standard deviation
    individual_terms_for_numerator1 = []
    for number in data_set1:
        term = (number - mean_data_set1) ** 2
        individual_terms_for_numerator1.append(term)
    total_sum_of_numerator1 = 0
    for number in individual_terms_for_numerator1:
        total_sum_of_numerator1 = total_sum_of_numerator1 + number
    the_sd1 = ((total_sum_of_numerator1) / (len(data_set1) - 1)) ** 0.5
    # determine the second standard deviation
    individual_terms_for_numerator2 = []
    for number in data_set2:
        term = (number - mean_data_set2) ** 2
        individual_terms_for_numerator2.append(term)
    total_sum_of_numerator2 = 0
    for number in individual_terms_for_numerator2:
        total_sum_of_numerator2 = total_sum_of_numerator2 + number
    the_sd2 = ((total_sum_of_numerator2) / (len(data_set2) - 1)) ** 0.5

    # 4TH) CALCULATE THE DENOMINATOR FOR T(CALC)
    denom_first_term_t_calc = ((the_sd1)**2) / (len(data_set1))
    denom_second_term_t_calc = ((the_sd2)**2) / (len(data_set2))
    t_calc_denominator = (denom_first_term_t_calc + denom_second_term_t_calc)**0.5

    # 5TH) CALCULATE T(CALC)
    t_calc = t_calc_numerator / t_calc_denominator

    # 6TH) CALCULATE THE NUMERATOR FOR DEGREES OF FREEDOM
    numerator_degree_freedom = (denom_first_term_t_calc + denom_second_term_t_calc)**2

    # 7TH) CALCULATE THE DENOMINATOR FOR DEGREES OF FREEDOM
    denom_degree_freedom_first_term = ((denom_first_term_t_calc)**2) / (len(data_set1) - 1)
    demon_degree_freedom_second_term = ((denom_second_term_t_calc)**2) / (len(data_set2) - 1)
    degree_freedom_denominator = denom_degree_freedom_first_term + demon_degree_freedom_second_term

    # 8TH) CALCULATE THE DEGREES OF FREEDOM
    degrees_freedom = math.floor(numerator_degree_freedom / degree_freedom_denominator)

    # 9TH) RETURN THE RESULT AS A TUPLE
    return t_calc, degrees_freedom


# Ex) use the function to determine the t(calc) value and the degrees of freedom
data_set1 = [27, 28, 30, 29, 28, 28, 28, 31, 25, 23, 21, 26, 28, 30, 27]
data_set2 = [25, 26, 28, 27, 23, 21, 19, 28, 23, 24, 26, 28, 25, 26, 25, 21, 24]

the_results = perform_unpaired_hetero_t_test(data_set1, data_set2)
print('The t(calc) value is', the_results[0])
print('The degrees of freedom is', the_results[1])

# when the t(calc) value and the degrees of freedom is compared to critical t values we
# can conclude that the mean of the two data sets is significantly different (0.005 < p < 0.01)
