# -*- coding: utf-8 -*-

from openfisca_aotearoa.entities import Person
from openfisca_core.model_api import *

"""
MSD Policy (retrieved August 2018 from )
    https://www.workandincome.govt.nz/map/card-services/community-services-card/qualifications.html

    To be able to receive a Community Services Card, a client must:

    *   receive an income tested benefit or
    *   be a child for whom an Orphans Benefit, an Unsupported Childs Benefit or a Child Disability Allowance is paid or
    *   receive a Residential Care Subsidy or
    *   receive New Zealand Superannuation and meet an income test or
    *   receive Veteran's Pension or
    *   receive weekly income compensation (paid by Veterans' Affairs) or
    *   receive weekly compensation (paid by Veterans' Affairs) or
    *   be a full time student, generally be ordinarily resident and meet an income test or

    *   for people with dependent children
        *   meet an income test and generally be ordinarily resident in New Zealand or
        *   be eligible to receive Working for Families Tax Credits (where Inland Revenue applies a Residency test)

    *   for people with no children:
        *   meet an income test
        *   generally be ordinarily resident and
        *   be aged over 16 years old, but not be a dependent child
"""


class social_security__eligible_for_community_services_card(Variable):
    value_type = bool
    entity = Person
    definition_period = MONTH
    label = "is eligible for Community Services Card"
    reference = "http://www.legislation.govt.nz/regulation/public/1993/0169/latest/DLM176710.html"

    def formula(persons, period, parameters):
        # The applicant
        resident_or_citizen = persons('is_citizen_or_resident', period)
        in_nz = persons('social_security__is_ordinarily_resident_in_new_zealand', period)
        # NOTE: using the age at the start of the month
        # Age changes on a DAY, but this calculation only has a granularity of MONTH
        age_requirement = persons("age", period.start) >= parameters(
            period).entitlements.social_security.community_services_card.age_threshold
        low_income = persons(
            'community_services_card__below_income_threshold', period)
        dependent_children = persons(
            'social_security__has_dependant_child', period)
        is_fulltime_student = persons(
            'social_security__is_fulltime_student', period)
        received_superannuation = persons(
            'social_security__received_superannuation', period)
        eligible_for_wff = persons(
            'family_scheme__qualifies_for_working_for_families', period)
        childs_benefit = \
            persons('social_security__received_orphans_benefit', period) +\
            persons('social_security__received_unsupported_childs_benefit', period) +\
            persons('social_security__received_child_disability_allowance', period)

        return \
            persons('social_security__received_income_tested_benefit', period.this_year) +\
            persons('social_security__received_residential_care_subsidy', period) +\
            persons('veterans_support__received_veterans_pension', period) +\
            persons('veterans_support__received_weekly_income_compensation', period) +\
            persons('veterans_support__received_weekly_compensation', period) +\
            childs_benefit +\
            (received_superannuation * low_income) +\
            (is_fulltime_student * low_income) +\
            (dependent_children * low_income * (resident_or_citizen + eligible_for_wff)) +\
            not_(dependent_children) * low_income * \
            resident_or_citizen * age_requirement * in_nz


# TODO:
# below are variables that still need to be implemented
class social_security__received_orphans_benefit(Variable):
    value_type = bool
    entity = Person
    definition_period = MONTH
    label = "Received Orphan's Benefit"
    reference = "http://www.legislation.govt.nz/act/public/1964/0136/latest/DLM5468365.html"


class social_security__received_unsupported_childs_benefit(Variable):
    value_type = bool
    entity = Person
    definition_period = MONTH
    label = "Received Unsupported Child's Benefit"
    reference = "http://www.legislation.govt.nz/act/public/1964/0136/latest/DLM361613.html"


class social_security__received_child_disability_allowance(Variable):
    value_type = bool
    entity = Person
    definition_period = MONTH
    label = "Received Child Disability Allowance"
    reference = "http://www.legislation.govt.nz/act/public/1964/0136/latest/DLM361659.html"


class social_security__received_residential_care_subsidy(Variable):
    value_type = bool
    entity = Person
    definition_period = MONTH
    label = "Received Residential Care Subsidy"
    reference = "http://www.legislation.govt.nz/act/public/1964/0136/latest/DLM359124.html"
    """
    residential care services means disability services supplied to a person with a disability in a residential disability care institution or rest
        home within the meaning of section 58(4) of the Health and Disability Services (Safety) Act 2001; and includes—

    (a) supervision and support services; and
    (b) hotel-type services (including the provision of sleeping facilities, meals, laundry, cleaning services and supplies, household furniture and
        furnishings, lighting, heating, hot water, and other household utilities); and
    (c) services that support daily living (including financial management and gardening); and
    (d) personal care services (including toileting, bathing, hair washing, teeth cleaning, nail care, feeding, and mobility); and
    (e) services within that home intended to provide satisfying activity to the person (including the provision of educational, social, recreational,
        and other activities); and
    (f) clinical support services, including personal health services (within the meaning of the New Zealand Public Health and Disability Act 2000),
        consultations with a medical practitioner, pharmaceuticals, incontinence aids, and other treatment costs
    """


class veterans_support__received_veterans_pension(Variable):
    value_type = bool
    entity = Person
    definition_period = MONTH
    label = "Received Veteran's Pension"
    reference = "http://www.legislation.govt.nz/act/public/2014/0056/latest/DLM5537967.html"


class veterans_support__received_weekly_income_compensation(Variable):
    value_type = bool
    entity = Person
    definition_period = MONTH
    label = "Received Weekly Income Compensation"
    reference = "http://legislation.govt.nz/act/public/2014/0056/latest/link.aspx?id=DLM5537962"


class veterans_support__received_weekly_compensation(Variable):
    value_type = bool
    entity = Person
    definition_period = MONTH
    label = "Received Weekly Compensation"
    reference = "http://legislation.govt.nz/act/public/2014/0056/latest/link.aspx?id=DLM5602254"


class social_security__received_superannuation(Variable):
    value_type = bool
    entity = Person
    definition_period = MONTH
    label = "Received Superannuation"
    reference = "http://legislation.govt.nz/act/public/1956/0047/latest/DLM446884.html"


class social_security__is_fulltime_student(Variable):
    value_type = bool
    entity = Person
    definition_period = MONTH
    label = "Is a Full-time student"
    reference = "http://www.legislation.govt.nz/act/public/1964/0136/latest/DLM359124.html"


class has_community_services_card(Variable):
    value_type = bool
    entity = Person
    definition_period = MONTH
    label = u"Has a current Community Services Card"
    reference = u"https://www.workandincome.govt.nz/products/a-z-benefits/community-services-card.html"
