# Author        : Prasanna Krishnan
# Date          : 2017-08-02
# Title         : Return random job title
# Description   : Return a random job title for testing
import random

class genJobTitle:
    def genJT(self):
        jobTitles = [
            'Project Manager'
            ,'Manager'
            ,'Java Developer'
            ,'.NET Developer'
            ,'Tester'
            ,'Financial Analyst'
            ,'Admin'
            ,'Analyst Type I'
            ,'Analyst Type II'
            ,'Analyst Type III'
            ,'Leverager'
            ,'Database Admin'
        ]
        return (random.choice(jobTitles))

