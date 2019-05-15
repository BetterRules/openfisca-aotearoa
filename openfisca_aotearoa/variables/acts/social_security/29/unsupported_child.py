# -*- coding: utf-8 -*-

from openfisca_aotearoa.entities import Person, Family
from openfisca_core.model_api import *


class social_security__eligible_for_unsupported_childs_benefit(Variable):
    value_type = bool
    entity = Person
    definition_period = MONTH
    label = "Eligible for Unsupported child’s benefit"
    reference = "http://www.legislation.govt.nz/act/public/1964/0136/latest/whole.html#DLM361606"
    # Unsupported child’s benefit

    # A person who is a principal caregiver in respect of a dependent child shall be entitled
    #    to receive an unsupported child’s benefit in respect of the child if—
    # (a) that person is not the natural parent, adoptive parent, or step-parent of the child; and
    # (b) because of a breakdown in the child’s family, no natural parent, adoptive parent, or step-parent
    #  of the child is able to care for the child or to provide fully for the child’s support; and
    # (c) the applicant is likely to be the principal caregiver in respect of the child for at least
    #  1 year from the date of application for the benefit; and
    # (d) the applicant is aged 18 years or over; and
    # (e) either—
    # (i) the child is both resident and present in New Zealand; or
    # (ii) the applicant has been both resident and present in New Zealand for a continuous period of 12 months at any time.

    def formula(persons, period, parameters):
        resident_or_citizen = persons('is_citizen_or_resident', period)
        normally_in_nz = persons("social_security__is_ordinarily_resident_in_new_zealand", period)

        age_test = persons('age', period.start) >= 18

        not_the_parent = not_(
            persons('social_security__is_the_parent_of_dependent_child', period))
        one_year = persons(
            'social_security__is_principal_carer_for_one_year_from_application_date', period)

        is_principal_carer = persons.has_role(Family.PRINCIPAL_CAREGIVER)

        has_unsupported_child_in_family = persons.family(
            'social_security__has_unsupported_child_in_family', period)

        return resident_or_citizen * normally_in_nz * age_test * not_the_parent * one_year * is_principal_carer * has_unsupported_child_in_family


class social_security__has_unsupported_child_in_family(Variable):
    value_type = bool
    entity = Family
    definition_period = MONTH
    reference = "http://www.legislation.govt.nz/act/public/1964/0136/latest/whole.html#DLM361613"
    label = "Family has an unsupported child"

    def formula(families, period, parameters):
        children = families.members('social_security__is_a_child', period)
        parents_unable = families.members(
            'social_security__parents_unable_to_provide_sufficient_care', period)
        resident_or_citizen = families.members(
            'is_citizen_or_resident', period)

        return families.any((children * parents_unable * resident_or_citizen), role=Family.CHILD)


class social_security__is_the_parent_of_dependent_child(Variable):
    value_type = bool
    entity = Person
    definition_period = ETERNITY
    default_value = True
    label = "Is the parent of their dependent child"


class social_security__is_principal_carer_for_one_year_from_application_date(Variable):
    value_type = bool
    entity = Person
    definition_period = MONTH
    label = "Is the principal carer for one year (or more) from the application date"


class social_security__parents_unable_to_provide_sufficient_care(Variable):
    value_type = bool
    entity = Person
    definition_period = MONTH
    label = u'because of a breakdown in the child’s family, no natural parent, adoptive parent, or step-parent of the child is able to care for the child or to provide fully for the child’s support'
