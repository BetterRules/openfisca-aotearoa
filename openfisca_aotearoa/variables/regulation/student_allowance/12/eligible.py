
# -*- coding: utf-8 -*-

from openfisca_core.model_api import *
from openfisca_aotearoa.entities import Person


class student_allowance__eligible_for_certain_allowances(Variable):
    value_type = bool
    entity = Person
    definition_period = MONTH
    reference = "http://legislation.govt.nz/regulation/public/1998/0277/latest/whole.html#DLM260337"
    label = "Eligible to certain allowances under Student Allowance Regulations"

    def formula(persons, period, parameters):

        # (1) No student is eligible for an allowance continued by regulation 3(a) to (e) unless—
        #     (a) he or she—
        #         (i) is a New Zealand citizen; or
        is_citizen = persons('is_nz_citizen', period)

        #         (ii) satisfies the chief executive that he or she is ordinarily resident in New Zealand,
        #             as lived in New Zealand for at least 3 years, and has been entitled under the
        #             Immigration Act 2009 to reside indefinitely in New Zealand for at least 3 years; or
        resides_in_nz = persons('social_security__is_ordinarily_resident_in_new_zealand', period)
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
        # NOTE: Uses the age at the start of the month
        under_super_age = persons('age', period.start) < parameters(period).entitlements.superannuation.age_qualification

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

        return (is_citizen + (resides_in_nz * lived_in_nz_3_years) + refugee_or_protected) \
            * under_super_age * ((fulltime * attendance) + overseas + parttime)


class student_allowance__is_enrolled_fulltime(Variable):
    value_type = bool
    entity = Person
    definition_period = MONTH
    label = "is enrolled in a full-time course at a tertiary provider or secondary school"
    reference = "http://legislation.govt.nz/regulation/public/1998/0277/latest/whole.html#DLM260337"


class student_allowance__meets_attendance_and_performance_requirements(Variable):
    value_type = bool
    entity = Person
    definition_period = MONTH
    label = "meets the attendance and performance requirements of that provider or school for tuition"
    reference = "http://legislation.govt.nz/regulation/public/1998/0277/latest/whole.html#DLM260337"


class student_allowance__approved_to_study_overseas(Variable):
    value_type = bool
    entity = Person
    definition_period = MONTH
    label = "is approved to study overseas under regulation 26"
    reference = "http://legislation.govt.nz/regulation/public/1998/0277/latest/whole.html#DLM260337"


class student_allowance__approved_to_study_parttime(Variable):
    value_type = bool
    entity = Person
    definition_period = MONTH
    label = "is approved to study in a part-time course under regulation 12A."
    reference = "http://legislation.govt.nz/regulation/public/1998/0277/latest/whole.html#DLM260337"
