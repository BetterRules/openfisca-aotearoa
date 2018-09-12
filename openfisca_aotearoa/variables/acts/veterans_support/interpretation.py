# -*- coding: utf-8 -*-

from openfisca_core.model_api import *
from openfisca_aotearoa.entities import Person


class veterans_support__received_parents_allowance(Variable):
    value_type = bool
    entity = Person
    definition_period = MONTH
    label = u'Boolean for if a Person is classified as receiving a parents allowance'
    reference = "http://www.legislation.govt.nz/act/public/2007/0097/latest/whole.html#DLM1518484"


class veterans_support__received_childrens_pension(Variable):
    value_type = bool
    entity = Person
    definition_period = MONTH
    label = u'Boolean for if a Person is classified as receiving a parents allowance'
    reference = "http://www.legislation.govt.nz/act/public/2007/0097/latest/whole.html#DLM1518484"
