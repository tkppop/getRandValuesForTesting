# Author        : Prasanna Krishnan
# Date          : 2017-06-09
# Title         : return random number
# Description   : Create random number with n digits
from random import randint

class genRandomNumber:
    def genRandomWithNDigits(self,n):
        range_start = 10 ** (n - 1)
        range_end = (10 ** n) - 1
        return randint(range_start, range_end)