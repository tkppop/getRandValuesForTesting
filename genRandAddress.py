# Author        : Prasanna Krishnan
# Date          : 2017-08-03
# Title         : Return random address
# Description   : Return a random address for testing
import random
from genRandNumber import genRandomNumber
from genRandUSStateName import genRandomUSState

class genAddress:
    def genAddress(self):
        streetTitles = [
            'Avenue'
            ,'Street'
            ,'Main Street'
            ,'Park Street'
            ,'Washington Ave'
            ,'Hill St'
            ,'Lake Ave'
            ,'Elm St'
            ,'Cedar Ave'
            ,'Pine St'
            ,'Maple Street'
            ,'Road'
            ,'Oak Lane'
            ,'Lane'
        ]
        t = genRandomNumber()
        address1 = str(t.genRandomWithNDigits(3)) + ", " + str(t.genRandomWithNDigits(2)) + " " + random.choice(streetTitles)
        t1 = genRandomUSState()
        city, state = t1.genRandomUSStateName()
        postal = t.genRandomWithNDigits(5)
        return address1,city,state,postal
