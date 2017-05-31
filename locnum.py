# ===================================================
#  Application name: locnum
#  Interpreter: Python 3.6
#  Description: class to convert from decimal numbers to location numerals and back
#  Version: 0.1
#  Date: 05/31/2017
#  Author: Denis Abakumov
# ===================================================

class LocalNumeral:
    """class to convert from decimal numbers to location numerals and back."""
    def __init__(self, dictionary="abcdefghijklmnopqrstuvwxyz"):
        """takes dictionary string as input and initializes a dictionary"""
        # check uniqueness of dictionary item
        if len(set(dictionary)) == len(dictionary):
            self.dic = dictionary
            # maximum number to handle
            self.max = 2**len(dictionary)-1
        else:
            raise ValueError("Non-unique character in dictionary")

    def to_loc(self, int_n):
        """method that takes an integer and returns the location numeral in abbreviated form."""
        result = None
        int_n = int(int_n)
        assert (int_n <= self.max)
        if int_n <= self.max:
            result = ""
            while int_n > 0:
                # get nearest smaller log to base 2
                n = int_n.bit_length()-1
                n = int(n)
                result = self.dic[n] + result
                int_n -= 2**n
        else:
            raise ValueError("Unsupported value")
        return result

    def to_int(self, loc_n):
        """method that takes a location numeral and returns its value as an integer."""
        result = 0
        loc_n = str(loc_n)
        for s in loc_n:
            pos = self.dic.find(s)
            if pos >= 0:
                result += 2**pos
            else:
                raise ValueError("Invalid character '{}' in location numeral '{}'".format(s, loc_n))

        return result

    def abbreviate(self, loc_n):
        """method that takes a location numeral and returns it in abbreviated form."""
        result = self.to_loc(self.to_int(loc_n))
        return result

