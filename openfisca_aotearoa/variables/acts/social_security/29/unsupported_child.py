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

    # A person who is a principal caregiver in respect of a dependent child shall be entitled to receive an unsupported child’s benefit in respect of the child if—
    # (a) that person is not the natural parent, adoptive parent, or step-parent of the child; and
    # (b) because of a breakdown in the child’s family, no natural parent, adoptive parent, or step-parent of the child is able to care for the child or to provide fully for the child’s support; and
    # (c) the applicant is likely to be the principal caregiver in respect of the child for at least 1 year from the date of application for the benefit; and
    # (d) the applicant is aged 18 years or over; and
    # (e) either—
    # (i) the child is both resident and present in New Zealand; or
    # (ii) the applicant has been both resident and present in New Zealand for a continuous period of 12 months at any time.

    def formula(persons, period, parameters):
        resident_or_citizen = persons('is_citizen_or_resident', period)

        not_the_parent = not_(
            persons('social_security__is_the_parent_of_dependent_child', period))
        one_year = persons(
            'social_security__is_principal_carer_for_one_year_from_application_date', period)

        is_principal_carer = persons.has_role(Family.PRINCIPAL_CAREGIVER)
        has_a_child = persons.family(
            "social_security__has_child_in_family", period)

        return resident_or_citizen * not_the_parent * one_year * is_principal_carer * has_a_child
