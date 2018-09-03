# -*- coding: utf-8 -*-

from openfisca_core.model_api import *
from openfisca_aotearoa.entities import Person


class student_allowance__eligible_for_basic_grant(Variable):
    value_type = bool
    entity = Person
    definition_period = MONTH
    reference = u"""
    7 Eligibility for basic grant
    (1) Every student is eligible for a basic grant if he or she is—
        (a) a secondary student of or over 16 but younger than 18 who is married or partnered with a supported child or children; or
        (b) a tertiary student of or over 16 but younger than 18 who has a supported child or children; or
        (c) a secondary student or tertiary student who is of or over 18, whether living at home or away from home.
    """

    def formula(persons, period, parameters):
        has_children = persons('student_allowance__has_a_supported_child', period)
        is_secondary_student = persons('is_secondary_student', period)
        is_tertiary_student = persons('is_tertiary_student', period)

        is_or_over_16 = persons('age', period) >= 16
        is_under_18 = persons('age', period) < 18
        is_over_18 = persons('age', period) >= 18

        is_married_or_partnered = persons('student_allowance__is_married_or_partnered', period)

        criteria_a = is_secondary_student * is_or_over_16 * is_under_18 * is_married_or_partnered * has_children
        criteria_b = is_tertiary_student * is_or_over_16 * is_under_18 * has_children
        criteria_c = (is_secondary_student + is_tertiary_student) * is_over_18

        return criteria_a + criteria_b + criteria_c

    """
    TODO:
    (1A)

    As from the commencement of 1 January 2004, the students who are eligible for a basic grant
    include a single tertiary student of or over 16 but younger than 18 who—
    (a)

    has completed a course of secondary instruction to year 13 level; or
    (b)

    has not completed a course of secondary instruction to year 13 level but—
    (i)

    has obtained, in the University Bursaries Examination, 3 "“C”" grade passes or better; or
    (ii)

    has obtained, at level 3 of the National Certificate of Educational Achievement, 42 credits or more.
    """
