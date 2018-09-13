# -*- coding: utf-8 -*-

from openfisca_core.model_api import *
from openfisca_aotearoa.entities import Person


class has_community_services_card(Variable):
    value_type = bool
    entity = Person
    definition_period = MONTH
    label = u"Has a current Community Services Card"
    reference = u"https://www.workandincome.govt.nz/products/a-z-benefits/community-services-card.html"
