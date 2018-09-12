
# -*- coding: utf-8 -*-

from openfisca_core.model_api import *
from openfisca_aotearoa.entities import Person, Family


class childcare_subsidy__is_child_attending_school(Variable):
    value_type = bool
    entity = Person
    definition_period = MONTH
    label = u"Is child attending school"
    reference = "http://www.legislation.govt.nz/regulation/public/2004/0268/latest/DLM282545.html"


class childcare_subsidy__child_will_be_enrolled_to_school_with_cohort_policy(Variable):
    value_type = bool
    entity = Person
    definition_period = MONTH
    label = u"Child will be enrolled in a school that has a cohort entry policy in place"
    reference = """ http://www.legislation.govt.nz/regulation/public/2004/0268/latest/DLM282545.html

      (ba) who is 5, whose parent, principal caregiver, or guardian intends to enrol the child in a school that has a cohort entry policy in place, and who (under section 5B(2) of the Education Act 1989) may not be enrolled in that school until the term start date of the next term;"""


class social_security__eligible_for_childcare_subsidy(Variable):
    value_type = bool
    entity = Person
    definition_period = MONTH
    label = u"Eligibility of child for payment of childcare subsidy"
    reference = u"http://www.legislation.govt.nz/regulation/public/2004/0268/latest/DLM282545.html"

    def formula(persons, period, parameters):
        is_citizen_or_resident = persons('is_citizen_or_resident', period)

        under_5_years_28_days_not_attending_school = persons.family(
            'social_security__has_child_under_5_not_in_school', period)
        is_5_and_will_be_enrolled = persons.family(
            'social_security__has_child_aged_5_who_will_be_enrolled_in_school', period)
        under_6_with_disability_allowance = persons.family(
            'social_security__has_disability_allowance_child_under_6', period)
        return is_citizen_or_resident * (under_5_years_28_days_not_attending_school + is_5_and_will_be_enrolled + under_6_with_disability_allowance)


class social_security__has_child_under_5_not_in_school(Variable):
    value_type = bool
    entity = Family
    definition_period = MONTH

    def formula(families, period, parameters):
        not_in_school = families.members(
            'childcare_subsidy__is_child_attending_school', period)
        under_5 = families.members('age', period) < 5
        citizens_and_residents = families.members(
            'is_citizen_or_resident', period)
        return families.any((citizen_and_residents * not_in_school * under_5), role=Family.CHILD)


class social_security__has_child_aged_5_who_will_be_enrolled_in_school(Variable):
    value_type = bool
    entity = Family
    definition_period = MONTH

    def formula(families, period, parameters):
        children_to_be_enrolled = families.members(
            'childcare_subsidy__child_will_be_enrolled_to_school_with_cohort_policy', period)
        aged_5 = families.members('age', period) == 5
        citizens_and_residents = families.members(
            'is_citizen_or_resident', period)
        return families.any((citizens_and_residents * children_to_be_enrolled * aged_5), role=Family.CHILD)


class social_security__has_disability_allowance_child_under_6(Variable):
    value_type = bool
    entity = Family
    definition_period = MONTH

    def formula(families, period, parameters):
        eligible_children = families(
            'social_security__family_has_eligible_disabled_child', period)
        under_6 = families.members('age', period) < 6
        citizens_and_residents = families.members(
            'is_citizen_or_resident', period)
        return families.any((citizens_and_residents * eligible_children * under_6), role=Family.CHILD)
