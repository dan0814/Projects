"""This file contains a function that calculates the results of a Chi-square test of
independence (Chi-square(calc) and degrees of freedom).  The two values can be compared
to critical Chi-square values to determine if p value is small (~0.05) """

# This function performs a Chi-square test of independence and returns the Chi-square(calc)
# value and the degrees of freedom.  The two values can be compared to critical Chi-square
# values to determine if the categories being observed are independent of each other

# The user inputs one argument.  The argument is an organized matrix containing the data of
# observed values

# The function returns the Chi-square(calc) value and the degrees of freedom


def perform_chi_square_independ_test(data_set):
    # 1ST) CALCULATE EXPECTED FREQUENCIES OF OBSERVATIONS
    # calculate the sum of user defined matrix
    sum_of_matrix = 0
    for ii in range(len(data_set)):
        for jj in range(len(data_set[0])):
            sum_of_matrix = sum_of_matrix + float(data_set[ii][jj])

    # get the sum of each row and add to sum_of_each_row list
    sum_of_each_row = []
    for ii in range(len(data_set)):
        sum_row = 0
        for jj in range(len(data_set[0])):
            sum_row = sum_row + float(data_set[ii][jj])
        sum_of_each_row.append(sum_row)

    # get the sum of each column and add to sum_of_each_column list
    sum_of_each_column = [sum(number) for number in zip(*data_set)]

    # calculate the expected frequencies for each row
    exp_freq_of_each_row = []
    for ii in range(len(sum_of_each_row)):
        exp_freq = sum_of_each_row[ii] / sum_of_matrix
        exp_freq_of_each_row.append(exp_freq)

    # calculate the expected frequencies for each column
    exp_freq_of_each_column = []
    for ii in range(len(sum_of_each_column)):
        exp_freq = sum_of_each_column[ii] / sum_of_matrix
        exp_freq_of_each_column.append(exp_freq)

    # 2ND) CREATE A LIST CONTAINING THE NUMBER OF OBSERVATIONS
    list_of_exp_value = []
    for ii in range(len(data_set)):
        for jj in range(len(data_set[0])):
            exp_value = sum_of_matrix * exp_freq_of_each_row[ii] * exp_freq_of_each_column[jj]
            list_of_exp_value.append(exp_value)

    # 3RD) CREATE A LIST USING THE USER DEFINED MATRIX
    list_of_obs_value = []
    for ii in range(len(data_set)):
        for jj in range(len(data_set[0])):
            obs_value = data_set[ii][jj]
            list_of_obs_value.append(obs_value)

    # 4TH) CREATE A LIST CONTAINING THE INDIVIDUAL CHI SQUARE TERMS
    chi_square_contributions = []
    for ii in range(len(list_of_obs_value)):
        value = ((list_of_obs_value[ii] - list_of_exp_value[ii]) ** 2) / (list_of_exp_value[ii])
        chi_square_contributions.append(value)

    # 5TH) CALCULATE CHI SQUARE(CALC)
    chi_square_calc = 0
    for ii in range(len(chi_square_contributions)):
        chi_square_calc = chi_square_calc + chi_square_contributions[ii]

    # 6TH) CALCULATE DEGREES OF FREEDOM
    degrees_of_freedom = (len(data_set) - 1) * (len(data_set[0]) - 1)

    # 7TH) RETURN THE RESULTS AS TUPLE
    return chi_square_calc, degrees_of_freedom


# Ex) use the function to determine the Chi-square(calc) value and the degrees of freedom.  The
# user defined matrix must be organized into the desired categories before inputting into the
# function as an argument
data_set = [[45, 12, 5, 9],
            [41, 14, 6, 12],
            [36, 9, 3, 8],
            [85, 34, 8, 17],
            [74, 17, 15, 11]]

the_answer = perform_chi_square_independ_test(data_set)
print("Chi square(calc) is", the_answer[0])
print("The degrees of freedom is", the_answer[1])

# when the Chi-square(calc) value and the degrees of freedom is compared to critical Chi-square
# values we can conclude that are categories that are represented by the user defined matrix are
# independent (p > 0.05)


