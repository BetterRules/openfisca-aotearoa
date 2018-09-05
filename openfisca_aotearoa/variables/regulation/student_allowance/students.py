# -*- coding: utf-8 -*-

from openfisca_core.model_api import *
from openfisca_aotearoa.entities import Person


class student_allowance__is_tertiary_student(Variable):
    value_type = bool
    entity = Person
    label = u"a tertiary student"
    reference = "http://legislation.govt.nz/regulation/public/1998/0277/latest/whole.html#DLM259980"
    definition_period = MONTH
    default_value = False


class student_allowance__is_secondary_student(Variable):
    value_type = bool
    entity = Person
    label = u"a secondary student"
    reference = "http://legislation.govt.nz/regulation/public/1998/0277/latest/whole.html#DLM259943"
    definition_period = MONTH
    default_value = False
