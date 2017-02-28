# -*- coding: utf-8 -*-

# Import all the python objects necessary to code the legislation in OpenFisca
# This line must be copy pasted to all files defining OpenFisca variables
from openfisca_country_template.base import *


# This variable is a pure input: it doesn't have a formula
class salary(Variable):
    column = FloatCol
    entity = Person
    definition_period = MONTH
    label = "Salary"


# This variable can be calculated from its formula
class income_tax(Variable):
    column = FloatCol
    entity = Person
    definition_period = MONTH

    # The formula to compute the income tax for a given person at a given period
    def function(person, period, legislation):
        return person('salary', period) * legislation(period).income_tax_rate


