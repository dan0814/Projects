"""This file contains a function that calculates the results of a Chi-square goodness of
fit test (Chi-square(calc) and degrees of freedom).  The two values can be compared to
critical Chi-square values to determine if p value is small (~0.05) """

# This function performs a Chi-square goodness of fit test and returns the Chi-square(calc)
# value and the degrees of freedom.  The two values can be compared to critical Chi-square
# values to determine if the observed frequencies is significantly different from the expected
# frequencies

# The user inputs three arguments.  The first argument is a list containing data points for a
# set of measurements, the second argument is a list containing expected frequencies (as
# fractions) which is based on the mathematical model being used by the user, and the third
# argument is the number of parameters which is based on the mathematical model being used by
# the user

# The function returns the Chi-square(calc) value and the degrees of freedom


def perform_chi_square_good_fit_test(data_set, expected_freq, num_parameters):
    # SORT data_set AND expected_freq ARGUMENTS IN ASCENDING ORDER BEFORE THE FIRST STEP
    data_set.sort()
    expected_freq.sort()

    # 1ST) CALCULATE EXPECTED NUMBER OF OBSERVATIONS
    sum_of_experimental_observations = 0
    for number in data_set:
        sum_of_experimental_observations = sum_of_experimental_observations + number
    expected_num_observations = []
    ii = 0
    for number in expected_freq:
        number = expected_freq[ii] * sum_of_experimental_observations
        expected_num_observations.append(number)
        ii = ii + 1

    # 2ND) CALCULATE EACH TERM TO BE SUMMED TO OBTAIN CHI-SQUARE(CALC) VALUE
    terms_to_be_summed = []
    for jj in range(len(data_set)):
        term = ((data_set[jj] - expected_num_observations[jj])**2) / (expected_num_observations[jj])
        terms_to_be_summed.append(term)

    # 3RD) CALCULATE CHI-SQUARE(CALC) VALUE
    chi_square_calc_value = 0
    for number in terms_to_be_summed:
        chi_square_calc_value = chi_square_calc_value + number

    # 4TH) CALCULATE THE DEGREES OF FREEDOM
    degrees_freedom = (len(data_set)) - (num_parameters) - (1)

    # 5TH) RETURN THE RESULT AS A TUPLE
    return chi_square_calc_value, degrees_freedom


# Ex) use the function to determine the Chi-square(calc) value and the degrees of freedom.
# the expected frequencies assumes that each "category" has an equal chance of occurring and
# the number of "parameters" for such a model is zero
data_set = [2, 4, 8, 9, 3, 10]
expected_freq = [1/6, 1/6, 1/6, 1/6, 1/6, 1/6]
num_parameters = 0

the_results = perform_chi_square_good_fit_test(data_set, expected_freq, num_parameters)
print('The Chi-square(calc) value is', the_results[0])
print('The degrees of freedom is', the_results[1])

# when the Chi-square(calc) value and the degrees of freedom is compared to critical Chi-square
# values we can conclude that the observed frequencies and the expected frequencies are not
# significantly different (0.1 < p < 0.05)

