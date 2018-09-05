
# -*- coding: utf-8 -*-

from openfisca_core.model_api import *
from openfisca_aotearoa.entities import Person


class student_allowance__eligible_for_certain_allowances(Variable):
    value_type = bool
    entity = Person
    definition_period = MONTH
    reference = """
        https://legislation.govt.nz/regulation/public/1998/0277/latest/whole.html#DLM260337
        Eligibility for certain allowances

        (1) No student is eligible for an allowance continued by regulation 3(a) to (e) unless—
            (a) he or she—
                (i) is a New Zealand citizen; or
                (ii) satisfies the chief executive that he or she is ordinarily resident in New Zealand,
                    as lived in New Zealand for at least 3 years, and has been entitled under the
                    Immigration Act 2009 to reside indefinitely in New Zealand for at least 3 years; or
                (iii) satisfies the chief executive that he or she is recognised under the Immigration
                    Act 2009 as a refugee or a protected person and is entitled under the Immigration
                    Act 2009 to reside indefinitely in New Zealand; or
                (iv) satisfies the chief executive that he or she is entitled under the Immigration Act
                    2009 to reside indefinitely in New Zealand and was sponsored into New Zealand by a
                    family member who, at the time of the student’s entry into New Zealand,—
                    (A) was recognised under the Immigration Act 1987 or the Immigration Act 2009 as a
                        refugee or protected person; and
                    (B) held a residence permit issued under the Immigration Act 1987 or a residence class
                        visa issued under the Immigration Act 2009; and
                        (ab) if the allowance is in respect of a course of study commencing on or after 1 January
                            2014, he or she is, when the course of study commences, under the age specified in
                            section 7(1) of the New Zealand Superannuation and Retirement Income Act 2001; and
            (ab) if the allowance is in respect of a course of study commencing on or after 1 January 2014,
                he or she is, when the course of study commences, under the age specified in section 7(1) of
                the New Zealand Superannuation and Retirement Income Act 2001; and
            (b) he or she makes an application for an allowance in accordance with Part 7; and
            (c) he or she either—
                (i) is enrolled in a full-time course at a tertiary provider or secondary school and meets
                    the attendance and performance requirements of that provider or school for tuition; or
                (ii) is approved to study overseas under regulation 26; or
                (iii) is approved to study in a part-time course under regulation 12A.
        (1A) [Revoked]

        (2) [Revoked]

        (2A) [Revoked]

        (3) No student may be awarded an allowance continued by regulation 3(a) to (e) who—
            (a) either—
                (i) has been granted a temporary permit to enter New Zealand for the purposes of study,
                    training, or paid employment, which permit requires that student to leave New Zealand
                    after completing that study, training, or paid employment; or
                (ii) is the spouse or partner of such a student and is not a New Zealand citizen; and
            (b) is not or has not subsequently become a person to whom subclause (1)﻿(a) applies.

        (4) Subclauses (1) to (3) are subject to—
            (a) regulation 47B (which relates to the effect of the 1 September 2013 changes to residence-related eligibility periods); and
            (b) regulation 47C (which contains an exception to the ineligibility ground introduced on 1 September 2013).
        """

    def formula(persons, period, parameters):

        # (1) No student is eligible for an allowance continued by regulation 3(a) to (e) unless—
        #     (a) he or she—
        #         (i) is a New Zealand citizen; or
        is_citizen = persons('is_nz_citizen', period)

        #         (ii) satisfies the chief executive that he or she is ordinarily resident in New Zealand,
        #             as lived in New Zealand for at least 3 years, and has been entitled under the
        #             Immigration Act 2009 to reside indefinitely in New Zealand for at least 3 years; or
        normally_in_nz = persons('normally_lives_in_nz', period)
        lived_in_nz_3_years = persons('number_of_years_lived_in_nz', period) >= 3

        #         (iii) satisfies the chief executive that he or she is recognised under the Immigration
        #             Act 2009 as a refugee or a protected person and is entitled under the Immigration
        #             Act 2009 to reside indefinitely in New Zealand; or
        refugee_or_protected = persons('immigration__is_recognised_refugee', period) + persons('immigration__is_protected_person', period)

        #         (iv) satisfies the chief executive that he or she is entitled under the Immigration Act
        #             2009 to reside indefinitely in New Zealand and was sponsored into New Zealand by a
        #             family member who, at the time of the student’s entry into New Zealand,—
        #             (A) was recognised under the Immigration Act 1987 or the Immigration Act 2009 as a
        #                 refugee or protected person; and
        #             (B) held a residence permit issued under the Immigration Act 1987 or a residence class
        #                 visa issued under the Immigration Act 2009; and
        #                 (ab) if the allowance is in respect of a course of study commencing on or after 1 January
        #                     2014, he or she is, when the course of study commences, under the age specified in
        #                     section 7(1) of the New Zealand Superannuation and Retirement Income Act 2001; and
        # TODO!!!

        # (ab) if the allowance is in respect of a course of study commencing on or after 1 January 2014,
        #     he or she is, when the course of study commences, under the age specified in section 7(1) of
        #     the New Zealand Superannuation and Retirement Income Act 2001; and
        under_super_age = persons('age', period) < parameters(period).entitlements.superannuation.age_qualification

        #     (b) he or she makes an application for an allowance in accordance with Part 7; and
        #     (c) he or she either—
        #         (i) is enrolled in a full-time course at a tertiary provider or secondary school and meets
        #             the attendance and performance requirements of that provider or school for tuition; or
        fulltime = persons('student_allowance__is_enrolled_fulltime', period)
        attendance = persons('student_allowance__meets_attendance_and_performance_requirements', period)

        #         (ii) is approved to study overseas under regulation 26; or
        overseas = persons('student_allowance__approved_to_study_overseas', period)
        #         (iii) is approved to study in a part-time course under regulation 12A.
        parttime = persons('student_allowance__approved_to_study_parttime', period)

        return (is_citizen + (normally_in_nz * lived_in_nz_3_years) + refugee_or_protected) \
            * under_super_age * ((fulltime * attendance) + overseas + parttime)


class student_allowance__is_enrolled_fulltime(Variable):
    value_type = bool
    entity = Person
    definition_period = MONTH
    label = "is enrolled in a full-time course at a tertiary provider or secondary school"
    reference = "https://legislation.govt.nz/regulation/public/1998/0277/latest/whole.html#DLM260337"


class student_allowance__meets_attendance_and_performance_requirements(Variable):
    value_type = bool
    entity = Person
    definition_period = MONTH
    label = "meets the attendance and performance requirements of that provider or school for tuition"
    reference = "https://legislation.govt.nz/regulation/public/1998/0277/latest/whole.html#DLM260337"


class student_allowance__approved_to_study_overseas(Variable):
    value_type = bool
    entity = Person
    definition_period = MONTH
    label = "is approved to study overseas under regulation 26"
    reference = "https://legislation.govt.nz/regulation/public/1998/0277/latest/whole.html#DLM260337"


class student_allowance__approved_to_study_parttime(Variable):
    value_type = bool
    entity = Person
    definition_period = MONTH
    label = "is approved to study in a part-time course under regulation 12A."
    reference = "https://legislation.govt.nz/regulation/public/1998/0277/latest/whole.html#DLM260337"
