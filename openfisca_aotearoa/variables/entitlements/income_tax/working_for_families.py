# -*- coding: utf-8 -*-

# Import from openfisca-core the common python objects used to code the legislation in OpenFisca
from openfisca_core.model_api import *
# Import the entities specifically defined for this tax and benefit system
from openfisca_aotearoa.entities import Person


class social_security__received_income_tested_benefit(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = u'Boolean for if a Person is classified as receiving an income tested benefit'
    reference = "http://www.legislation.govt.nz/act/public/2007/0097/latest/whole.html#DLM1518484"


class veterans_support__received_parents_allowance(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = u'Boolean for if a Person is classified as receiving a parents allowance'
    reference = "http://www.legislation.govt.nz/act/public/2007/0097/latest/whole.html#DLM1518484"


class veterans_support__received_childrens_pension(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = u'Boolean for if a Person is classified as receiving a parents allowance'
    reference = "http://www.legislation.govt.nz/act/public/2007/0097/latest/whole.html#DLM1518484"


class income_tax__resident(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = u'Boolean for if a Person is classified as meeting residence requirements'
    reference = "http://www.legislation.govt.nz/act/public/2007/0097/latest/DLM1518482.html"
    # This should really be a forumla based variable covering the full residency criteria.


class income_tax__income(Variable):
        value_type = float
        entity = Person
        definition_period = YEAR
        label = u'The annual income for a Person in a Family.'
        reference = ""  # TODO Add


class income_tax__eligible_for_working_for_families(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = u'Boolean for if a Person is classified as eligible for working for families tax credits'
    reference = "http://www.legislation.govt.nz/act/public/2007/0097/latest/DLM1518477.html"

    def formula(person, period, parameters):
        received_tested_benefit = person('social_security__received_income_tested_benefit', period)
        received_parents_allowance = person('veterans_support__received_parents_allowance', period)
        received_childrens_pension = person('veterans_support__received_childrens_pension', period)

        return not_(received_tested_benefit) * not_(received_parents_allowance) * not_(received_childrens_pension)
        # TODO - Add remaining eligibility criteria as per legislation.
