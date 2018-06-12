# -*- coding: utf-8 -*-

# Import from openfisca-core the common python objects used to code the legislation in OpenFisca
from openfisca_core.model_api import *
# Import the entities specifically defined for this tax and benefit system
from openfisca_aotearoa.entities import Person, Family


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


class income_tax__residence(Variable):
    value_type = bool
    entity = Person
    definition_period = MONTH
    default_value = True  # TODO residency is required as defined in the act
    label = u'Boolean for if a Person is classified as meeting residence requirements'
    reference = "http://www.legislation.govt.nz/act/public/2007/0097/latest/DLM1518482.html"
    # This should really be a forumla based variable covering the full residency criteria.


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


class income_tax__family_has_dependent_children(Variable):
    value_type = bool
    entity = Family
    definition_period = MONTH
    label = u'A family has one or more people who qualify as financially dependant children'
    reference = "http://legislation.govt.nz/act/public/2007/0097/latest/DLM1518480.html"

    def formula(families, period, parameters):
        return families.max(families.members("income_tax__dependent_child", period))


class income_tax__dependent_child(Variable):
    value_type = bool
    entity = Person
    definition_period = MONTH
    label = u'Determines if a Person is classified as financially dependant'
    reference = "http://legislation.govt.nz/act/public/2007/0097/latest/DLM1520575.html#DLM1520883"

    def formula(person, period, parameters):
        age = person('age', period)
        # TODO - It's not this simple, this needs to be tweaked to include the edge criteria above.
        # not in a marriage, civil union, or de facto relationship
        # is or less than 15
        # or 16 and 17 and not financially independant
        # is 18 and many conditions (see act)
        return age <= 18
