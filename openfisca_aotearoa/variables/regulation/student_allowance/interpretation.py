# -*- coding: utf-8 -*-

from openfisca_core.model_api import *
from openfisca_aotearoa.entities import Person, Family


class student_allowance__is_childless(Variable):
    value_type = bool
    entity = Person
    definition_period = MONTH


class student_allowance__combined_income(Variable):
    value_type = float
    entity = Person
    definition_period = MONTH
    label = """
    combined income, in relation to any student, means—
    (a) the personal income of that student; and
    (b) the spousal or partner’s income of that student
    """


class student_allowance__is_a_dependent_student(Variable):
    value_type = bool
    entity = Person
    definition_period = MONTH
    label = """dependent student, in relation to a parent whose income is being assessed, means a child of that parent—
    (a) who is attending a full-time course at a tertiary provider or a secondary school; and
    (b) who is not younger than 16 on 31 December in the year before the year of application
        and is not older than 23 on 1 January in the year of application; and
    (c) who has not been awarded an independent circumstances grant; and
    (d) in respect of whom an orphan’s benefit is not paid; and
    (e) in respect of whom an unsupported child’s benefit is not paid; and
    (f) who receives financial support from that parent"""


class student_allowance__income_before_tax(Variable):
    value_type = bool
    entity = Person
    definition_period = MONTH
    label = """income before tax includes gains before tax and profits before tax"""


class student_allowance__is_living_with_a_parent(Variable):
    value_type = bool
    entity = Person
    definition_period = MONTH
    label = """living with a parent has the same meaning as in section 3(1) of the Social Security Act 1964"""


class student_allowance__is_married(Variable):
    value_type = bool
    entity = Person
    definition_period = MONTH
    label = """married
        (a) means having a spouse; and
        (b) for the avoidance of doubt, does not include a person who is legally married
            but who does not have a spouse (as that term is defined in this subclause)
        """
