"""
CS 196 FA18 HW4
Prepared by Andrew, Emilio, and Prithvi

You might find certain default Python packages immensely helpful.
"""

# Good luck!

import string
import itertools
from itertools import combinations

"""
most_common_char

Given an input string s, return the most common character in s.
"""
def most_common_char(s):
    hist_chars = {}
    for character in s:
        if character in hist_chars:
            hist_chars[character] += 1
        else:
            hist_chars[character] = 1
    return sorted(hist_chars, key = hist_chars.get)[-1] 

"""
alphabet_finder

Given an input string s, return the shortest prefix of s (i.e. some s' = s[0:i] for some 0 < i <= n)
that contains all the letters of the alphabet.
If there is no such prefix, return None.
Your function should recognize letters in both cases, i.e. "qwertyuiopASDFGHJKLzxcvbnm" is a valid alphabet.

Example 1:
	Argument:
		"qwertyuiopASDFGHJKLzxcvbnm insensitive paella"
	Return:
		"qwertyuiopASDFGHJKLzxcvbnm"

Example 2:
	Argument:
		"aardvarks are cool!"
	Return:
		None
"""
def alphabet_finder(s):
    lowercase = s.lower()
    abc_dict = {}
    abc_dict = dict.fromkeys(string.ascii_lowercase, 1)
    index = 0
    while (len(abc_dict) > 0 and index < len(lowercase)):
        try:
            abc_dict.pop(lowercase[index])
        except KeyError:
            pass
        index += 1
    return s[:index]


"""
longest_unique_subarray

Given an input list of integers arr,
return a list with two values [a,b] such that arr[a:a+b] is the longest unique subarray.
That is to say, all the elements of arr[a:a+b] must be unique,
and b must be the largest value possible for the array.
If multiple such subarrays exist (i.e. same b, different a), use the lowest value of a.

Example:
	Argument:
		[1, 2, 3, 1, 4, 5, 6]
	Return:
		[1, 6]
"""
def longest_unique_subarray(arr):
    pass

"""
string_my_one_true_love

A former(?) CA for this course really like[d] strings that have the same occurrences of letters.
This means the staff member likes "aabbcc", "ccddee", "abcabcabc", etcetera.

But the person who wrote all of your homework sets wants to trick the staff with really long strings,
that either could be the type of string that the staff member likes,
or a string that the CA would like if you remove exactly one character from the string.

Return True if it's a string that the homework creator made, and False otherwise.
Don't treat any characters specially, i.e. 'a' and 'A' are different characters.

Ungraded food for thought:
Ideally, your method should also work on integer arrays without any modification.

Example 1:
	Argument:
		"abcbabcdcdda"
		There are 3 a's, 3 b's, 3 c's, and 3 d's. That means it is a very likable string!
	Return:
		True

Example 2:
Argument:
		"aaabbbcccddde"
		There are 3 a's, 3 b's, 3 c's, and 3 d's. We have 1 e, which we can remove.
	Return:
		True

Example 3:
	Argument:
		"aaabbbcccdddeeffgg"
		This string is similar to the other ones, except with 2 e's, f's and g's at the end.
		To make this string likable, we need to remove the 2 e's, f's, and g's or we can remove
		one a, b, c, and d. However all of these require more than one removal, so it becomes invalid.
	Return:
		False
"""
def string_my_one_true_love(s):
    char_hist = {}
    for c in s: # Histogram of the letters
        if c not in char_hist:
            char_hist[c] = 1
        else:
            char_hist[c] += 1
    letter_frequency = {}
    for frequency in char_hist.values():
        if frequency not in letter_frequency:
            letter_frequency[frequency] = 1
        else:
            letter_frequency[frequency] += 1
    if len(letter_frequency) <= 1 or (len(letter_frequency) == 2 and letter_frequency[1] == 1):
        return True
    return False

    

"""
alive_people

You are given a 2-dimensional list data. Each element in data is a list [birth_year, age_of_death].
Assume that the person was alive in the year (birth_year + age_of_death).
Given that data, return the year where the most people represented in the list were alive.
If there are multiple such years, return the earliest year.

Example:
	Argument:
		[[1920, 80], [1940, 22], [1961, 10]]
	Return:
		1961
"""
def alive_people(data):
    # Convert the second number to a year
    for date in data:
        date[1] = (date[0] // 100) * 100 + date[1]
        if date[1] < date[0]:
            date[1] += 100

    # Convert it to a histogram of the years people were alive
    alive_people = {}
    for date in data:
        for year in range(date[0],date[1]+1):
            if year not in alive_people:
                alive_people[year] = 1
            else:
                alive_people[year] += 1
    print(alive_people)
    # Return max of the values
    year = 0
    deaths = 0
    for key, value in alive_people.items():
        if value > deaths:
            deaths = value
            year = key
    return year

"""
three_sum

Given an input list of integers arr, and a constant target t,
is there a triplet of distinct elements [a,b,c] so that a + b + c = t?

Return a 2-dimensional list of all the unique triplets as defined above.
Each inner list should be a triplet as we defined above.
We don't care about the order of triplets, nor the order of elements in each triplet.

Example:
	Arguments:
		[-1, 0, 1, 2, -1, -4], 0
	Return:
		[
			[-1, 0, 1],
			[-1, -1, 2]
		]
"""
def three_sum(arr, t):
    return [list(correct_triplets) for correct_triplets in list(set([tuple(sorted(triplet)) for triplet in combinations(arr, 3) if sum(triplet) == t]))]
"""
happy_numbers

Given an input integer n > 0, return the number of happy integers between 1 and n, bounds inclusive.
https://en.wikipedia.org/wiki/Happy_number

Example 1:
	Argument:
		8
		The happy numbers between 1 and 8 are 1 and 7 (7 -> 49 -> 97 -> 130 -> 10 -> 1)
	Return:
		2468 // 1234 (i.e., 2)
Example 2:
	Argument:
		15
	Return:
		4294967296 ** (1 / 16) (i.e., 4)
"""
def happy_numbers(n):
    def test_happiness(num):
        numbers_tried = []
        testNum = num
        while testNum != 1:
            testNum = sum(map(lambda x: int(x)**2, list(str(testNum))))
            if (testNum in numbers_tried):
                return False
            numbers_tried.append(testNum)
            print(testNum)
        return True

    happy_numbers_count = 0
    for i in range(1, n + 1):
        if test_happiness(i):
            happy_numbers_count += 1
    return happy_numbers_count


"""
zero_sum_subarray

Given an input list of integers arr,
return a list with two values [a,b] such that sum(arr[a:a+b]) == 0.
In plain English, give us the location of a subarray of arr that starts at index a
and continues for b elements, so that the sum of the subarray you indicated is zero.
If multiple such subarrays exist, use the lowest valid a, and then lowest valid b,
in that order of priority.
If no such subarray exists, return None.

Ungraded food for thought:
Think about how to generalize your solution to any arbitrary target sum.

Example 1:
	Argument:
		[0, 1, 2, 3, 4, 5]
		Clearly, the first element by itself forms a subarray with sum == 0.
	Return:
		[0, 1]

Example 2:
	Argument:
		[10, 20, -20, 3, 21, 2, -6]
		In this case, arr[1:3] = [20, -20], so there is a zero sum subarray.
	Return:
		[1, 2]
"""
def zero_sum_subarray(arr):
    for i in range(len(arr)):
        cut_arr = arr[i:]
        for j in range(1, len(cut_arr)):
            print(cut_arr[:j])
            if sum(cut_arr[:j]) == 0:
                return [i, j]
    return None

