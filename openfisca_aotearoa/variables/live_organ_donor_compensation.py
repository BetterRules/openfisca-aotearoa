# -*- coding: utf-8 -*-

# Import from openfisca-core the common python objects used to code the legislation in OpenFisca
from openfisca_core.model_api import *
# Import the entities specifically defined for this tax and benefit system
from openfisca_aotearoa.entities import Titled_Property, Person
from numpy import clip, floor

class weekly_compensation_before_tax(Variable):
    value_type = float
    entity = Person
    definition_period = YEAR # TODO - determine whether we need to get WEEK to work
    label = u"The amount payable as compensation per week before tax"
    def formula(persons, period, parameters):
        return persons('salary_per_pay', period)

class PayFrequency(Enum):
    weekly = u'Weekly'
    fortnightly = u'Fortnightly'
    four_weekly = u'Four Weekly'
    monthly = u'Monthly'

class pay_frequency(Variable):
    value_type = Enum
    possible_values = PayFrequency
    default_value = PayFrequency.weekly  # The default is mandatory
    entity = Person
    definition_period = YEAR
    label = u"The frequency at which a person is paid"

class salary_per_pay(Variable):
    value_type = float
    entity = Person
    definition_period = YEAR # TODO - determine whether we need to get WEEK to work
    label = u"The salary earned by a person before tax"

class kiwisaver_member(Variable):
    value_type = bool
    default_value = True
    entity = Person
    label = u"Whether the person currently pays into Kiwisaver"
    definition_period = YEAR