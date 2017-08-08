# Author        : Prasanna Krishnan
# Date          : 2017-08-02
# Title         : Return a random date for testing
# Description   : Return a random date for testing

from datetime import datetime
import random

class genDate:
    def genDate(self):
        year = random.randint(2010, 2019)
        month = random.randint(1, 12)
        day = random.randint(1, 28)
        return datetime(year, month, day)