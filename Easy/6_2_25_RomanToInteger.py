#Challenge: Given a roman numeral, convert it to an integer.

class Solution(object):
    def romanToInt(self, s):
        #docstring, s is a string and returns an integer (rtype)
        """
        :type s: str
        :rtype: int
        """
        # dictionary for storing key:value pairs
        romanValue = {
            'I': 1, 'V': 5, 'X': 10, 'L': 50,
            'C': 100, 'D': 500, 'M': 1000
        }

        total = 0 # store final integer result
        prev_value = 0  # as we loop through the string "s" this variable keeps track of the prev numeral value

        # iterate through roman numerals string "s" from left to right 
        for char in s:
            curr_value = romanValue[char]  # get integer value of current character e.g. V is 5 from dictionary

            # if the previous value is smaller, subtract it
            if prev_value < curr_value:
                total += curr_value - 2 * prev_value  # subtract the previous addition
            else:
                total += curr_value  # otherwise, just add the value

            prev_value = curr_value  # update previous value for next iteration

            # formula
            # XIV = 14 or 10 + 4
            # left to right -> X = 10, I = 1, V = 5
            # beginning from X, curr_value = 10 
            # I = 1 and V = 5, if we continue to add XIV becomes 16
            # hence, first loop goes -> curr_value = 10, prev_value = 0
            # total = 10 - 2 * 0. multiplication goes first, so 2 becomes 0 and 10 - 0 = 0
            # loop again, curr_value is 1 and prev_value is 10. prev_value bigger, so else.
            # prev_value is now 1, current value is 5
            # prev value is smaller, so total add 5 - 2 * 1 = 3 plus total of 11 = 14

        return total     