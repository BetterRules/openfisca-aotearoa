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


class veterans_support__is_entitled_to_be_paid_veterans_pension(Variable):
    value_type = bool
    entity = Person
    definition_period = MONTH
    label = u"Applicant is a entitled to be paid veterans pension in a Pacific country"
    reference = "http://www.legislation.govt.nz/act/public/2014/0056/latest/DLM5537707.html"
