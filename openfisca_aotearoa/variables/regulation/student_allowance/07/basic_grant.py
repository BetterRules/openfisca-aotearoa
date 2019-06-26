# -*- coding: utf-8 -*-

from openfisca_core.model_api import *
from openfisca_aotearoa.entities import Person
from numpy import invert


class student_allowance__eligible_for_basic_grant(Variable):
    value_type = bool
    entity = Person
    definition_period = MONTH
    label = u"eligibily for Student Allowance basic grant"
    reference = "http://legislation.govt.nz/regulation/public/1998/0277/latest/whole.html#DLM260306"

    def formula(persons, period, parameters):
        has_children = persons('student_allowance__has_a_supported_child', period)
        is_secondary_student = persons('student_allowance__is_secondary_student', period)
        is_tertiary_student = persons('student_allowance__is_tertiary_student', period)

        # NOTE: using the age at the start of the month
        # Age changes on a DAY, but this calculation only has a granularity of MONTH
        is_or_over_16 = persons('age', period.start) >= 16
        is_under_18 = persons('age', period.start) < 18
        is_or_over_18 = persons('age', period.start) >= 18

        is_married_or_partnered = persons('student_allowance__is_married_or_partnered', period)

        criteria_a = is_secondary_student * is_or_over_16 * is_under_18 * is_married_or_partnered * has_children
        criteria_b = is_tertiary_student * is_or_over_16 * is_under_18 * has_children
        criteria_c = (is_secondary_student + is_tertiary_student) * is_or_over_18

        student_allowance__eligible_for_certain_allowances = persons('student_allowance__eligible_for_certain_allowances', period)

        partner_or_person_receives_certain_allowances = invert(persons("student_allowance__partner_or_person_receiving_certain_allowances", period))

        return (criteria_a + criteria_b + criteria_c) * student_allowance__eligible_for_certain_allowances * partner_or_person_receives_certain_allowances

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
