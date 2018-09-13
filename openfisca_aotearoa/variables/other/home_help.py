# -*- coding: utf-8 -*-

from openfisca_core.model_api import *
from openfisca_aotearoa.entities import Person

class home_help__had_multiple_birth(Variable):
    value_type = bool
    entity = Person
    definition_period = MONTH
    label = u"Had a multiple birth from the same pregnancy"
    reference = "https://www.workandincome.govt.nz/products/a-z-benefits/home-help.html"


class home_help__adopted_2_or_more_children(Variable):
    value_type = bool
    entity = Person
    definition_period = MONTH
    label = u"Have or adopted twins, and already has another child under 5."
    reference = "https://www.workandincome.govt.nz/products/a-z-benefits/home-help.html"


class home_help__has_no_immediate_family(Variable):
    value_type = bool
    entity = Person
    definition_period = MONTH
    label = u"Has no immediate family or anyone else living with you who can help"
    reference = u"https://www.workandincome.govt.nz/products/a-z-benefits/home-help.html"


class home_help__eligible_for_home_help(Variable):
    value_type = bool
    entity = Person
    definition_period = MONTH
    label = u"Eligible for Home Help"
    reference = u"https://www.workandincome.govt.nz/products/a-z-benefits/home-help.html"

    def formula(persons, period, parameters):
        is_citizen = persons('is_nz_citizen', period)

        return is_citizen *\
            persons('home_help__had_multiple_birth', period) +\
            persons('home_help__adopted_2_or_more_children', period) +\
            persons('home_help__has_no_immediate_family', period) *\
            persons('has_community_services_card', period)
