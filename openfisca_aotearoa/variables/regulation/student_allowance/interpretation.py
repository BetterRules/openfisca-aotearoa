# -*- coding: utf-8 -*-

from openfisca_core.model_api import *
from openfisca_aotearoa.entities import Person


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


class student_allowance__is_married_or_partnered(Variable):
    value_type = bool
    entity = Person
    definition_period = MONTH
    label = "married or partnered as per Student Allowances Regulations 1998"
    reference = """
        https://legislation.govt.nz/regulation/public/1998/0277/latest/whole.html#DLM259903
        (a) means having a spouse; and
        (b) for the avoidance of doubt, does not include a person who is legally married
            but who does not have a spouse (as that term is defined in this subclause)
        """

    def formula(families, period, parameters):
        return persons('student_allowance__has_a_spouse')


class student_allowance__has_a_supported_child(Variable):
    value_type = bool
    entity = Person
    definition_period = MONTH
    label = "has a supported child as per Student Allowances Regulations 1998"
    reference = """
    https://legislation.govt.nz/regulation/public/1998/0277/latest/whole.html#DLM259968
    supported child, in relation to a student applying for an allowance, means a person younger than 24—
        (a)

        whose well-being and financial support are the responsibility of the student; and
        (b) who lives with that student at least half of the time; and
        (c) who is not in receipt of—
            (i) an allowance continued by regulation 3(a) to (c); or
            (ii) jobseeker support, sole parent support, an emergency benefit, or a supported living payment under the Social Security Act 1964; or
            (iii) New Zealand superannuation under the New Zealand Superannuation and Retirement Income Act 2001 or a veteran’s pension under
                the Veterans’ Support Act 2014; or
            (iv) payments under any government-assisted scheme (other than the Student Loan Scheme) which, in the opinion of the chief executive,
                is similar to a benefit under the Social Security Act 1964; or
            (v) income before tax from employment or self-employment which exceeds $80 per week; and
        (d) in respect of whom no orphan’s benefit or unsupported child’s benefit is payable under the Social Security Act 1964
    """


class student_allowance__partner_has_a_supported_child(Variable):
    value_type = bool
    entity = Person
    definition_period = MONTH
    label = "their spouse has a supported child, as per Student Allowances Regulations 1998"


class student_allowance__has_a_spouse(Variable):
    value_type = bool
    entity = Person
    definition_period = MONTH
    label = "Has spouse as per Student Allowances Regulations 1998"
    reference = """
    https://legislation.govt.nz/regulation/public/1998/0277/latest/whole.html#DLM259958
    Spouse, in relation to an applicant, means a person who is legally married to that applicant if—
        (a) both of them are of or over 24; or
        (b) one or both of them are younger than 24 and at least 1 of them has a supported child"""

    def formula(families, period, parameters):
        part_a = (persons('age', period) >= 24) * (persons('age_of_partner', period) >= 24)
        part_b = ((persons('age', period) >= 24) + (persons('age_of_partner', period) >= 24)) * \
            (persons('student_allowance__has_a_supported_child', period) + persons('student_allowance__partner_has_a_supported_child'))

        return part_a + part_b


class student_allowance__is_a_student(Variable):
    value_type = bool
    entity = Person
    definition_period = MONTH
    label = "student means a person who is enrolled or intends to enrol in a recognised course of study"
