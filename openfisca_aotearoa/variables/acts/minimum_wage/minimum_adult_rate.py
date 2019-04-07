# -*- coding: utf-8 -*-

from openfisca_core.model_api import *
from openfisca_aotearoa.entities import Person


class minimum_wage__minimum_adult_rate_wages(Variable):
    value_type = float
    entity = Person
    definition_period = DAY
    label = u"Weekly earnings"
    reference = "http://legislation.govt.nz/act/public/1983/0115/29.0/DLM74414.html"
    # note order: http://www.legislation.govt.nz/regulation/public/2018/0010/latest/whole.html
