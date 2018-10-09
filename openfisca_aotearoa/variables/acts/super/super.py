# -*- coding: utf-8 -*-

# Import from openfisca-core the common python objects used to code the legislation in OpenFisca
from openfisca_core.model_api import *
# Import the entities specifically defined for this tax and entitlement system
from openfisca_aotearoa.entities import Person



class super__living_alone(Variable):
    value_type = int
    entity = Person
    definition_period = MONTH
    label = u"Is a person considered as living alone"
    reference = "http://www.legislation.govt.nz/act/public/2001/0084/latest/whole.html#DLM5578822"

class super__age(Variable):
    value_type = int
    entity = Person
    definition_period = MONTH
    label = u"Applicants age"
    reference = "http://www.legislation.govt.nz/act/public/2001/0084/latest/whole.html#DLM113987"

class super__is_receiving_compensation(Variable):
    value_type = bool
    entity = Person
    definition_period = MONTH
    label = u"Is receiving compensation payment through ACC"
    reference = "http://www.legislation.govt.nz/act/public/2001/0049/latest/DLM105404.html#DLM105404"

class super__has_partner(Variable):
    value_type = bool
    entity = Person
    definition_period = MONTH
    label = u"Has a partner"
    reference = "http://www.legislation.govt.nz/act/public/2001/0049/latest/DLM105404.html#DLM105404"

class super__eligibility(Variable):
    value_type = bool
    entity = Person
    definition_period = MONTH
    label = u'Classified as eligible for NZ Super'
    reference = "http://www.legislation.govt.nz/act/public/2001/0084/latest/DLM113985.html"

    def formula(persons, period, parameters):
        persons('super__age', period) +\
        persons('super__is_receiving_compensation', period) +\
        persons('super__has_partner', period)

