#!/usr/bin/env python3

'''Practice functions and doctests.

Assignment instructions: https://csci40.rtealwitter.com/topics/02_python/lab.html
'''


################################################################################
# PART I:
# These functions review the control flow and math operations
################################################################################

def is_even(n):
    '''
    Return True if n is even and False if n is odd.

    HINT: Use the modulus operator %

    >>> is_even(0)
    True
    >>> is_even(1)
    False
    >>> is_even(2000)
    True
    >>> is_even(-8)
    True
    >>> is_even(-9)
    False
    >>> type(is_even(0))
    <class 'bool'>
    '''


def is_odd(n):
    '''
    Return True if n is odd and False if n is even.

    >>> is_odd(0)
    False
    >>> is_odd(1)
    True
    >>> is_odd(2000)
    False
    >>> is_odd(-8)
    False
    >>> is_odd(-9)
    True
    >>> type(is_odd(0))
    <class 'bool'>
    '''


def absolute_value(n):
    '''
    Return the absolute value of n.

    HINT:
    Use an if statement.

    >>> absolute_value(5)
    5
    >>> absolute_value(-5)
    5
    >>> absolute_value(5.5)
    5.5
    >>> absolute_value(-5.5)
    5.5
    '''


def max_num(a, b):
    '''
    Return the maximum of a and b.

    HINT:
    Use an if statement.

    >>> max_num(4, 5)
    5
    >>> max_num(5, 4)
    5
    >>> max_num(-4, -5)
    -4
    >>> max_num(4, 4)
    4
    >>> type(max_num(4, 4))
    <class 'int'>
    '''


def max_num_4(a, b, c, d):
    '''
    Return the maximum of a, b, c, and d.

    HINT:
    Use many if statements.

    >>> max_num_4(1,2,3,4)
    4
    >>> max_num_4(2,3,4,1)
    4
    >>> max_num_4(3,4,1,2)
    4
    >>> max_num_4(4,1,2,3)
    4
    >>> max_num_4(10,1,2,3)
    10
    '''


def max_num_abs(a, b):
    '''
    Return the number with the highest absolute value.

    HINT:
    Use an if statement, but be careful about the condition.

    >>> max_num_abs(4,5)
    5
    >>> max_num_abs(4,5)
    5
    >>> max_num_abs(-4,-5)
    -5
    >>> max_num_abs(4,4)
    4
    >>> type(max_num_abs(4, 4))
    <class 'int'>
    '''


def is_leap_year(n):
    '''
    Return True if n is a leap year and False otherwise.

    HINT:
    The formula for calculating leap years is more complicated than you might think.
    You can find the formula at <https://www.mathsisfun.com/leap-years.html>.

    >>> is_leap_year(1582)
    False
    >>> is_leap_year(2000)
    True
    >>> is_leap_year(2018)
    False
    >>> is_leap_year(2019)
    False
    >>> is_leap_year(2020)
    True
    >>> is_leap_year(2200)
    False
    >>> is_leap_year(2400)
    True
    '''


def num_digits(n):
    '''
    Return the number of digits in the input n.

    NOTE:
    A negative sign does not count as a digit,
    only numbers do.

    HINT:
    Use a while loop.
    In each iteration, divide the number by 10 to reduce the number of digits by 1.

    HINT:
    This function is implemented in one of your quiz practice problems.

    >>> num_digits(5)
    1
    >>> num_digits(10)
    2
    >>> num_digits(45678)
    5
    >>> num_digits(123456789012345678901234567890)
    30
    >>> num_digits(-5)
    1
    >>> num_digits(-10)
    2
    >>> type(num_digits(4))
    <class 'int'>
    '''


def factorial(n):
    '''
    Return the factorial of n.
    Recall that the factorial of n is defined to be: 1*2*3*...*(n-1)*n

    HINT:
    Use a for loop from 1 to n.
    On each iteration, multiply the current result by the current iteration number.

    >>> factorial(1)
    1
    >>> factorial(2)
    2
    >>> factorial(3)
    6
    >>> factorial(4)
    24
    >>> factorial(10)
    3628800
    >>> factorial(100)
    93326215443944152681699238856266700490715968264381621468592963895217599993229915608941463976156518286253697920827223758251185210916864000000000000000000000000
    '''


def is_prime(n):
    '''
    Return True if n is prime, and False otherwise.
    Recall that a prime number is divisible only by itself and 1,
    and by convention 1 is not considered to be a prime number.

    HINT:
    Use a for loop to check if every number between 2 and n-1 divides n

    >>> is_prime(1)
    False
    >>> is_prime(2)
    True
    >>> is_prime(3)
    True
    >>> is_prime(4)
    False
    >>> is_prime(97)
    True
    >>> is_prime(99)
    False
    '''


def is_perfect_square(n):
    '''
    Return True if n is is the product of two integers.
    That is, return True if there exists an integer i such that i*i==n.

    HINT:
    Use a for loop to check each number i between 0 and n.

    >>> is_perfect_square(1)
    True
    >>> is_perfect_square(2)
    False
    >>> is_perfect_square(4)
    True
    >>> is_perfect_square(81)
    True
    >>> is_perfect_square(97)
    False
    >>> is_perfect_square(0)
    True
    >>> is_perfect_square(-144)
    False
    >>> is_perfect_square(144)
    True
    '''


def fibonacci(n):
    '''
    Return the nth fibonacci number.
    Recall that the fibonacci numbers are calculated by the following formula:

        fibonacci(0) = 0
        fibonacci(1) = 1
        fibonacci(n) = fibonacci(n-1) + fibonacci(n-2)

    HINT:
    The following "pseudocode" describes how to calculate the nth fibonacci number:

    Let f0 = 0
    Let f1 = 1
    In a for loop from 0 to n,
        Let fn = f0 + f1
        Let f0 = f1
        Let f1 = fn


    >>> fibonacci(0)
    0
    >>> fibonacci(1)
    1
    >>> fibonacci(2)
    1
    >>> fibonacci(3)
    2
    >>> fibonacci(4)
    3
    >>> fibonacci(5)
    5
    >>> fibonacci(6)
    8
    >>> fibonacci(7)
    13
    >>> fibonacci(1000)
    43466557686937456435688527675040625802564660517371780402481729089536555417949051890403879840079255169295922593080322634775209689623239873322471161642996440906533187938298969649928516003704476137795166849228875
    >>> type(fibonacci(4))
    <class 'int'>
    '''


################################################################################
# PART II:
#
# The problems below use all the same techniques as the problems above.
# But they don't contain any hints about how to solve them.
# So you will have to figure out for yourself when to use if/for/while statements.
################################################################################


def cigar_party(cigars, is_weekend):
    '''
    When squirrels get together for a party, they like to have cigars.
    A squirrel party is successful when the number of cigars is between 40 and 60, inclusive.
    Unless it is the weekend, in which case there is no upper bound on the number of cigars.
    Return True if the party with the given values is successful, or False otherwise.

    >>> cigar_party(30, False)
    False
    >>> cigar_party(50, False)
    True
    >>> cigar_party(70, True)
    True
    >>> cigar_party(10, True)
    False
    >>> cigar_party(40, False)
    True
    '''


def speeding_fine(speed, birthday):
    '''
    The police department needs a function that computes the size of a fine to give to someone pulled over for speeding,
    and its your job to translate the law into code to implement this function.

    The law states that:
    if the speed was 60 or less, the fine is 0 dollars.
    If the speed is between 61-80 inclusive, the fine is 100 dollars.
    And if the speed is greater than 80, the fine is 2000 dollars.
    The law has a strange provision, however, that when it is someone's birthday they are allowed to drive 5 mph faster in all cases.

    >>> speeding_fine(60, False)
    0
    >>> speeding_fine(60, True)
    0
    >>> speeding_fine(61, False)
    100
    >>> speeding_fine(61, True)
    0
    >>> speeding_fine(65, True)
    0
    >>> speeding_fine(80, True)
    100
    >>> speeding_fine(81, True)
    100
    >>> speeding_fine(86, True)
    2000
    >>> speeding_fine(81, False)
    2000
    >>> speeding_fine(101, True)
    2000
    >>> speeding_fine(90, False)
    2000
    '''


def near_ten(x):
    '''
    Return True if num is within 2 of a multiple of 10.

    >>> near_ten(10)
    True
    >>> near_ten(6)
    False
    >>> near_ten(8)
    True
    >>> near_ten(19)
    True
    >>> near_ten(78921)
    True
    >>> near_ten(-43)
    False
    >>> near_ten(-42)
    True
    '''


def love6(a, b):
    '''
    The number 6 is a truly great number.
    Return True if:
    either input number equals 6 or their sum or difference is 6.

    >>> love6(6, 5)
    True
    >>> love6(4, 5)
    False
    >>> love6(3, 3)
    True
    >>> love6(3, 2)
    False
    >>> love6(-3, 3)
    True
    >>> love6(10, 4)
    True
    >>> love6(121, 5)
    False
    >>> love6(-3, -3)
    False
    >>> love6(123, 6)
    True
    '''


def funny_sum(a, b, c):
    '''
    Return the sum of the input values.
    However, if one of the values is the same as another of the values, it does not count towards the sum.

    >>> funny_sum(1, 2, 3)
    6
    >>> funny_sum(3, 2, 3)
    2
    >>> funny_sum(3, 3, 3)
    0
    >>> funny_sum(3, 2, -3)
    2
    >>> funny_sum(3, 3, -3)
    -3
    >>> funny_sum(1, 3, 3)
    1
    >>> funny_sum(3, 3, 2)
    2
    >>> funny_sum(3, 2, 1)
    6
    >>> funny_sum(5, 2, 6)
    13
    '''


def median(a, b, c):
    '''
    Given 3 int values, return the value in the middle.

    >>> median(1, 2, 3)
    2
    >>> median(2, 1, 3)
    2
    >>> median(3, 1, 2)
    2
    >>> median(2, 2, 1)
    2
    >>> median(5, 4, 4)
    4
    >>> median(-3, -2, 7)
    -2
    '''


def sum_between(a, b):
    '''
    Find the sum of all numbers between a and b inclusive.

    >>> sum_between(1, 2)
    3
    >>> sum_between(1, 3)
    6
    >>> sum_between(1, 5)
    15
    >>> sum_between(2, 1)
    3
    >>> sum_between(-5, 5)
    0
    >>> sum_between(5, 10)
    45
    >>> sum_between(1000, 10000)
    49505500
    >>> sum_between(10, -1000)
    -500445
    >>> sum_between(0, 123456)
    7620753696
    '''

################################################################################
# PART III:
# These functions require you to use python lists.
################################################################################

def largest(xs):
    '''
    Return the largest element in a list.

    HINT:
    There is a built-in function on your cheat sheet that performs this task.

    >>> largest([1,2,3])
    3
    >>> largest([99,-56,80,100,90])
    100
    >>> largest(list(range(0,100)))
    99
    >>> largest([10])
    10
    >>> largest([])
    '''


def last_element(xs):
    '''
    Return the last element of the input list.
    If the input list has no last element, return None.

    HINT:
    Use negative indexes.

    >>> last_element([0,1,2,3,4,5,6,7,8,9])
    9
    >>> last_element(['a','b','c','d'])
    'd'
    >>> last_element([0,1])
    1
    >>> last_element([])
    '''


def last_element_list(xs):
    '''
    Return a list containing only the last element.

    HINT:
    Use negative indexes.

    >>> last_element_list([0,1,2,3,4,5,6,7,8,9])
    [9]
    >>> last_element_list(['a','b','c','d'])
    ['d']
    >>> last_element_list([0,1])
    [1]
    >>> last_element_list([])
    []
    '''


def first_three(xs):
    '''
    Return a list containing the first three elements of the input list.
    If the list contains three or fewer elements,
    then return the entire list.

    HINT:
    Use slices.

    >>> first_three([0,1,2,3,4,5,6,7,8,9])
    [0, 1, 2]
    >>> first_three(['a','b','c','d'])
    ['a', 'b', 'c']
    >>> first_three([0,1])
    [0, 1]
    >>> first_three([])
    []
    '''


def last_three(xs):
    '''
    Return a list containing the last three elements of the input list.
    If the list contains three or fewer elements, then return the entire list.

    HINT:
    Use slices.

    >>> last_three([0,1,2,3,4,5,6,7,8,9])
    [7, 8, 9]
    >>> last_three(['a','b','c','d'])
    ['b', 'c', 'd']
    >>> last_three([0,1])
    [0, 1]
    '''


def largest3(xs):
    '''
    Return the largest 3 elements in a list in sorted order.

    >>> largest3([1,2,3])
    [1, 2, 3]
    >>> largest3([99,-56,80,100,90])
    [90, 99, 100]
    >>> largest3(list(range(0,100)))
    [97, 98, 99]
    >>> largest3([10])
    [10]
    >>> largest3([])
    []
    '''


def filter_odd(xs):
    '''
    Return a list with all the odd elements removed.

    HINT:
    Use the accumulator pattern with a for loop.

    >>> filter_odd([2,4,6])
    [2, 4, 6]
    >>> filter_odd([1,3,5])
    []
    >>> filter_odd([4,5,6,7])
    [4, 6]
    >>> filter_odd([20,13,4,16,8,19,10])
    [20, 4, 16, 8, 10]
    '''


def filter_even(xs):
    '''
    Return a list with all the even elements removed.

    HINT:
    Use the accumulator pattern with a for loop.

    >>> filter_even([1,3,5])
    [1, 3, 5]
    >>> filter_even([2,4,6])
    []
    >>> filter_even([4,5,6,7])
    [5, 7]
    >>> filter_even([20,13,4,16,8,19,10])
    [13, 19]
    '''


def bigger_than_10(xs):
    '''
    Return the number of elements in the list bigger than 10

    >>> bigger_than_10([])
    0
    >>> bigger_than_10([10])
    0
    >>> bigger_than_10([11,1,12,2,13,3,14,4,15,5])
    5
    >>> bigger_than_10([4,5,6,11])
    1
    '''


def second_largest(xs):
    '''
    Return the second largest element in a list.
    If the list has less than 2 elements, return None.

    HINT:
    Use the .sort() function and lists indexing.

    >>> second_largest([1,2,3])
    2
    >>> second_largest([99,-56,80,100,90])
    99
    >>> second_largest(list(range(0,100)))
    98
    >>> second_largest([10])
    >>> second_largest([])
    '''


def has_index_at_value(xs):
    '''
    Return True if xs[i] == i for any i.

    HINT:
    For this problem, you need access to the both the indexes and the values.
    Therefore, you cannot use a for loop that looks like

        for x in xs:

    and instead you must use a for loop that looks like

        for i in range(len(xs)):

    >>> has_index_at_value([0])
    True
    >>> has_index_at_value([1])
    False
    >>> has_index_at_value([1, 1])
    True
    >>> has_index_at_value([1, 0])
    False
    >>> has_index_at_value([0, 0])
    True
    >>> has_index_at_value([7, 3, 2, 8])
    True
    >>> has_index_at_value([2, 9, 5, 6, 19, 6, 6, 6, 6, 6])
    True
    >>> has_index_at_value([2, 9, 5, 4, 19, 4, 4, 4, 4, 4])
    False
    '''


def nested_filter_odd(xss):
    '''
    Convert a list of lists into a single list that contains only the even elements.

    >>> nested_filter_odd([[2, 4, 5], [1, 3, 6]])
    [2, 4, 6]
    >>> nested_filter_odd([[1, 3, 6]])
    [6]
    >>> nested_filter_odd([[4, 5], [6, 7]])
    [4, 6]
    >>> nested_filter_odd([[20],[13,4,16,8,19],[10], [15, 13, 1]])
    [20, 4, 16, 8, 10]
    '''


def flatten(xss):
    '''
    Convert a list of lists into a single list that contains the same elements.

    >>> flatten([[True,False],[False,True]])
    [True, False, False, True]
    >>> flatten([[1,2,3],[4,5,6],[7,8,9]])
    [1, 2, 3, 4, 5, 6, 7, 8, 9]
    >>> flatten([['a','b','c','d'],['e','f','g','h'],['i','j','k','l'],['m','n','o','p']])
    ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p']
    >>> flatten([[10]])
    [10]
    '''


def filter_flatten(xss):
    '''
    This function takes as input a list of lists and returns a single list.
    The first element of the returned list is equal to the first element in the first nested list,
    the second element of the returned list is equal to the second element in the second nested list,
    and in general the n-th element of the returned list is equal to the n-th element in the n-th nested list.

    HINT:
    You will need to have access to the indexes and not just values.
    So your for loop should look something like

        for i in range(len(xss)):
            # do something here with xss[i]

    >>> filter_flatten([[True,False],[False,True]])
    [True, True]
    >>> filter_flatten([[1,2,3],[4,5,6],[7,8,9]])
    [1, 5, 9]
    >>> filter_flatten([['a','b','c','d'],['e','f','g','h'],['i','j','k','l'],['m','n','o','p']])
    ['a', 'f', 'k', 'p']
    >>> filter_flatten([[10]])
    [10]
    '''
