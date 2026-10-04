#!/usr/bin/env python3
"""Display a game-night report using the functions students complete in lab.py.

This supplied driver contains event data and calls, not function solutions.
Run the doctests in lab.py to check whether each calculation is correct.
"""

from copy import deepcopy

import lab


PLAYERS = ['Ada', 'Teal', 'Sam', 'Jo', 'Lin', 'Mo']
ROUND_RESULTS = [12, 7, 15, 4, 18, 9]
ROUNDS = [[12, 7, 15], [4, 18, 9], [6, 11, 20]]

# Each row names a lab function, gives its inputs, and labels its report result.
# All rows use inputs with a non-None answer, so None means unfinished here.
REPORT = [
    ('Date and player groups', [
        ('is_leap_year', (2028,), 'February 29 is available in 2028'),
        ('is_even', (len(PLAYERS),), 'Everyone on the six-player roster can pair up'),
        ('is_odd', (len(PLAYERS) + 1,), 'One late arrival leaves an odd player count'),
        ('factorial', (len(PLAYERS),), 'Possible playing orders'),
    ]),
    ('Score comparisons and cumulative totals', [
        ('absolute_value', (-7,), 'Size of the score change'),
        ('max_num', (18, 23), 'Higher of two scores'),
        ('max_num_4', (18, 23, 7, 15), 'Highest of four scores'),
        ('max_num_abs', (-12, 9), 'Change with the largest magnitude'),
        ('median', (18, 23, 7), 'Middle of three scores'),
        ('sum_between', (1, 5), 'Total tokens awarded from one through five'),
    ]),
    ('Number-puzzle cards', [
        ('num_digits', (4072,), 'Digits on the code card'),
        ('is_prime', (29,), 'The 29 card passes the prime-number rule'),
        ('is_perfect_square', (49,), 'The 49 tiles can form a square'),
        ('fibonacci', (8,), 'Eighth Fibonacci clue'),
        ('near_ten', (38,), 'The 38 card is near a multiple of ten'),
        ('love6', (14, 8), 'The 14 and 8 cards satisfy the six rule'),
        ('funny_sum', (5, 5, 11), 'Points after ignoring repeated values'),
    ]),
    ('Comic rule cards', [
        ('cigar_party', (70, True), 'The squirrels approve their weekend party'),
        ('speeding_fine', (84, True), 'Fine on the birthday traffic card'),
    ]),
    ('Report from ordered round results', [
        ('largest', (ROUND_RESULTS,), 'Highest score'),
        ('last_element', (ROUND_RESULTS,), 'Last reported score'),
        ('last_element_list', (ROUND_RESULTS,), 'Last score as a one-item list'),
        ('first_three', (ROUND_RESULTS,), 'First three reported scores'),
        ('last_three', (ROUND_RESULTS,), 'Last three reported scores'),
        ('largest3', (ROUND_RESULTS,), 'Top three scores in ascending order'),
        ('filter_odd', (ROUND_RESULTS,), 'Scores remaining after odd values are removed'),
        ('filter_even', (ROUND_RESULTS,), 'Scores remaining after even values are removed'),
        ('bigger_than_10', (ROUND_RESULTS,), 'Number of scores above ten'),
        ('second_largest', (ROUND_RESULTS,), 'Second-largest score'),
        ('has_index_at_value', ([5, 9, 2, 8],), 'A bonus token matches its position'),
    ]),
    ('Results collected across rounds', [
        ('nested_filter_odd', (ROUNDS,), 'Even scores from all three rounds'),
        ('flatten', (ROUNDS,), 'All scores in round order'),
        ('filter_flatten', (ROUNDS,), 'First, second, and third featured scores'),
    ]),
]


def main():
    print('GAME-NIGHT REHEARSAL')
    print('Players:', ', '.join(PLAYERS))
    print('Round results:', ROUND_RESULTS)
    print('Rounds:', ROUNDS)
    unfinished = 0
    errors = 0
    displayed = 0
    for heading, rows in REPORT:
        print('\n' + heading)
        for name, arguments, label in rows:
            try:
                # A valid implementation may sort its input list in place.
                # Give each call fresh data so that later rows keep their order.
                result = getattr(lab, name)(*deepcopy(arguments))
            except Exception as error:
                print(f'  {label}: ERROR in {name}: {type(error).__name__}: {error}')
                errors += 1
                continue
            if result is None:
                print(f'  {label}: unfinished ({name} returned None)')
                unfinished += 1
            else:
                print(f'  {label}: {result!r}')
                displayed += 1
    print(f'\nReport: {displayed} displayed, {unfinished} unfinished, {errors} errors.')
    print('Use python3 -m doctest lab.py to check correctness and boundary cases.')


if __name__ == '__main__':
    main()
