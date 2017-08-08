# Author        : Prasanna Krishnan
# Date          : 2017-08-03
# Title         : Return a random supplier name for testing
# Description   : Return a random supplier name for testing
import random

class genSupplierName:
    def genSupplierName(self):
        #The supplier names below, have to be in the system
        supplierName = [
            'Internal'
            , 'Consulting Inc_Edited'
            , 'First Management'
            , 'IT Solutions'
            , 'Staffing Plus'
            , 'Ampcus_Edited'
            , 'Bridge Technical_Edited'
            , 'Computer Alliance LLC 1_Edited'
            , 'Corporate Technologies'
            , 'Edge Technology Services'
            , 'Eliassen Group LLC'
            , 'Endurix National Staffing'
            , 'ExecuSearch Group'
            , 'Experis US Inc'
            , 'Extension Inc'
            , 'FastSwitch'
            , 'Jaci Carroll Staffing'
            , 'Judge Technical Services'
            , 'Kforce'
            , 'Lenmar Consulting'
            , 'Manpower Inc'
            , 'Marcum Staffing LLC'
            , 'Monroe Staffing Services'
            , 'Nesco Resource'
            , 'Ridgefield LLC'
            , 'Right Click Recruiting'
            , 'Software Solutions'
            , 'Solomon Page'
            , 'Tailored Management'
            , 'vLink'
            , 'James LLC'
            , 'LAUNCH 1.0'
            , 'James 1099'
            , 'Extra supplier'
            , 'Extra supplier1'
            , 'Endurix National Staffing1'
            , 'James 5'
            , 'Adecco'
            , 'Top Recruiters'
        ]
        return (random.choice(supplierName))