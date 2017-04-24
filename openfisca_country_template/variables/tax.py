# -*- coding: utf-8 -*-

# Import from openfisca-core the common python objects used to code the legislation in OpenFisca
from openfisca_core.model_api import *
# Import the entities specifically defined for this tax and benefit system
from openfisca_country_template.entities import *


class income_tax(Variable):
    column = FloatCol
    entity = Person
    definition_period = MONTH
    label = u"Income tax"
    url = "https://law.gov.example/income_tax"  # Always use the most official source

    # The formula to compute the income tax for a given person at a given period
    def function(person, period, legislation):
        return person('salary', period) * legislation(period).tax.income_tax_rate


class social_security_contribution(Variable):
    column = FloatCol
    entity = Person
    definition_period = MONTH
    label = u"Progressive contribution paid on salaries to finance social security"
    url = "https://law.gov.example/social_security_contribution"  # Always use the most official source

    def function(person, period, legislation):
        salary = person('salary', period)
        scale = legislation(period).tax.social_security_contribution

        return scale.calc(salary)
