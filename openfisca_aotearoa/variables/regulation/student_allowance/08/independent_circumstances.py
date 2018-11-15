# -*- coding: utf-8 -*-

from openfisca_core.model_api import *
from openfisca_aotearoa.entities import Person


class student_allowance__eligible_for_independent_circumstances(Variable):
    value_type = bool
    entity = Person
    definition_period = MONTH
    reference = "http://legislation.govt.nz/regulation/public/1998/0277/latest/whole.html#DLM260312"
    label = "Eligible for Student Allowance Independent Circumstances Grant"
    """
    8 Eligibility for independent circumstances grant
    (1) A single student without a supported child or children is eligible for an independent circumstances grant, if—
        (a) either—
            (i) the student is of or over 16 and younger than 24, and is undertaking a course at a tertiary provider; or
            (ii) is of or over 18 and younger than 24, and is undertaking a course at a secondary school; and
                (b) the student is neither living in a parental home nor receiving financial assistance from any parent of that student; and
                (c) the chief executive considers that it would, by reason of exceptional circumstances, be unreasonable
                    for the student to live with a parent and receive financial assistance from any parent of that student.
        (2) [Revoked]
        (3) Despite subclause (1), no student is eligible for an independent circumstances grant if the student receives
            a basic grant. (4) This regulation is subject to regulations 12 to 16, 20, 28 to 31, 34, 35, 40, and 44 to 48.
    """
    # Forumla todo
