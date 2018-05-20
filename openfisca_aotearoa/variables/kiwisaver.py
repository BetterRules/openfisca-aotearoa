# -*- coding: utf-8 -*-

# Import from openfisca-core the common python objects used to code the legislation in OpenFisca
from openfisca_core.model_api import *
# Import the entities specifically defined for this tax and benefit system
from openfisca_aotearoa.entities import Titled_Property, Person
from numpy import clip

#All variables are according to the reference link http://www.legislation.govt.nz/act/public/2006/0040/latest/DLM379487.html#DLM379487

class ks_duration(Variable):
    value_type = int
    entity = Person
    definition_period = MONTH
    label = u"Years the prospective home buyer has been a member of a kiwisaver account"

class ks_contrib_duration(Variable):
    value_type = int
    entity = Person
    definition_period = MONTH
    label = u"Years the prospective home buyer has been contributing continuously to their kiwisaver account"

class ks_contrib_duration_satisfied(Variable):
    value_type = bool
    entity = Person
    definition_period = MONTH
    label = u"This flag returns true or false if the contribution period is valid"

    def formula(persons, period):
        return persons('ks_contrib_duration', period) >= 3

class homestart_grant(Variable):
    value_type = float
    entity = Person
    definition_period = MONTH
    label = u"Amount available to you from the Homestart grant"

    def formula(persons, period):
        duration = persons('ks_contrib_duration', period)
        HS_grant = persons('ks_contrib_duration', period) * persons('ks_contrib_duration_satisfied', period) * 1000
        return clip(HS_grant,0,5000)

class purc_price(Variable):
    value_type = int
    entity = Titled_Property
    definition_period = YEAR
    label = u"Purchase price of the proposed home"

class indv_income_per_hs_grant(Variable):
    value_type = int
    entity = Person
    definition_period = YEAR
    set_input = set_input_divide_by_period
    # Check how to set input by user and check against the threshold

class combined_income_per_hs_grant(Variable):
    value_type = int
    entity = Person
    definition_period = YEAR
    set_input = set_input_divide_by_period  # Allows user to declare a salary for a year. 
    # Check how to set input by user and check against the threshold
    label = "Combined income"
