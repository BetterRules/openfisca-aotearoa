# -*- coding: utf-8 -*-

from openfisca_core.model_api import *
from openfisca_aotearoa.entities import Person


class student_allowance__is_tertiary_student(Variable):
    value_type = bool
    entity = Person
    label = u"a tertiary student"
    reference = """
    tertiary provider means a university, polytechnic, college of education, or
    wananga, a private training establishment continued by the Act, or any other
    education provider approved by the chief executive of the Ministry of Education for the purpose
    """
    definition_period = MONTH
    default_value = False


class student_allowance__is_secondary_student(Variable):
    value_type = bool
    entity = Person
    label = u"a secondary student"
    reference = """
    secondary school means
    (a) a secondary school established under Part 12 of the Act or registered under section 35A of the Act; or
    (b) a school that provides secondary instruction and is a correspondence school under section 145 of the
        Act or is designated as a correspondence school under section 152 of the Act; or
    (c) a special school that provides secondary instruction and is continued by Part 3 of the Education Act
        1964, or a specified institution in Schedule 5 of the Act
    """
    definition_period = MONTH
    default_value = False
