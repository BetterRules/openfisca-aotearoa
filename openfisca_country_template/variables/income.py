# -*- coding: utf-8 -*-

# This file defines the variables of our legislation.
# A variable is property of a person, or an entity (e.g. a household).
# See https://doc.openfisca.fr/variables.html

# Import from openfisca-core the common python objects used to code the legislation in OpenFisca
from openfisca_core.model_api import *
# Import the entities specifically defined for this tax and benefit system
from openfisca_country_template.entities import *


# This variable is a pure input: it doesn't have a formula
class salary(Variable):
    column = FloatCol
    entity = Person
    definition_period = MONTH
    label = "Salary"
    url = "https://law.gov.example/salary"  # Always use the most official source


class disposable_income(Variable):
    column = FloatCol
    entity = Person
    definition_period = MONTH
    label = "Actual amount available to the person at the end of the month"
    url = "https://stats.gov.example/disposable_income"  # Some variables represent quantities used in economic models, and not defined by law. Always give the source of your definition.

    def formula(person, period, legislation):
        return (
            + person('salary', period)
            + person('basic_income', period)
            - person('income_tax', period)
            - person('social_security_contribution', period)
            )
