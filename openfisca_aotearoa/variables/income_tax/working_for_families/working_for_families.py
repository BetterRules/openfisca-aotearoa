# -*- coding: utf-8 -*-

# Import from openfisca-core the common python objects used to code the legislation in OpenFisca
from openfisca_core.model_api import *
# Import the entities specifically defined for this tax and benefit system
from openfisca_aotearoa.entities import Titled_Property, Person
from numpy import clip, floor

class received_income_tested_benefit_as_per_social_security(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = u'Number of Persons classified as receiving an income tested benefit'
    reference = "http://www.legislation.govt.nz/act/public/2007/0097/latest/whole.html#DLM1518484"

class received_parents_allowance_as_per_veterans_support(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = u'Number of Persons classified as receiving a parents allowance'
    reference = "http://www.legislation.govt.nz/act/public/2007/0097/latest/whole.html#DLM1518484"

class received_childrens_pension_as_per_veterans_support(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = u'Number of Persons classified as receiving a parents allowance'
    reference = "http://www.legislation.govt.nz/act/public/2007/0097/latest/whole.html#DLM1518484"


class dependants_as_per_income_tax(Variable):
    value_type = bool
    entity = Person
    definition_period = MONTH
    label = u'Number of Persons classified as financially dependant'
    reference = "http://www.legislation.govt.nz/act/public/2007/0097/latest/whole.html#DLM1520883"

    def formula(person, period, parameters):
        age = person('age', period)
        return age <= 18 # It's not this simple, this needs to be tweaked to inlcude the edge criteria.


