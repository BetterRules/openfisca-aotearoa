from openfisca_aotearoa.entities import Person, Family
from openfisca_core.model_api import *


class social_security__eligible_for_orphans_benefit(Variable):
    value_type = bool
    entity = Person
    definition_period = MONTH
    label = u"Eligible for Orphan's benefit"
    reference = """http://www.legislation.govt.nz/act/public/1964/0136/latest/whole.html#DLM361606
        Orphans' benefits
        A person who is a principal caregiver in respect of a dependent child shall be entitled to receive an orphan's benefit in respect of that child if
        (a) each of the child's natural or adoptive parents is dead, or cannot be found, or suffers a serious long-term disablement which renders him or her unable to care for the child and
        (b) the applicant is likely to be the principal caregiver in respect of the child for at least 1 year from the date of application for the benefit; and
        (c) the applicant is aged 18 years or over; and
        (d) either
        (i) the child is both resident and present in New Zealand or
        (ii) the applicant has been both resident and present in New Zealand for a continuous period of 12 months at any time.
    """

    def formula(persons, period, parameters):
        resident_or_citizen = persons('is_citizen_or_resident', period)
        normally_in_nz = persons("social_security__is_ordinarily_resident_in_new_zealand", period)

        age_test = persons('age', period.start) >= 18

        not_the_parent = not_(
            persons('social_security__is_the_parent_of_dependent_child', period))
        one_year = persons(
            'social_security__is_principal_carer_for_one_year_from_application_date', period)

        is_principal_carer = persons.has_role(Family.PRINCIPAL_CAREGIVER)

        has_orphaned_child_in_family = persons.family(
            'social_security__has_orphaned_child_in_family', period)

        return resident_or_citizen * normally_in_nz * age_test * not_the_parent * one_year * is_principal_carer * has_orphaned_child_in_family


class social_security__has_orphaned_child_in_family(Variable):
    value_type = bool
    entity = Family
    definition_period = MONTH
    reference = "http://www.legislation.govt.nz/act/public/1964/0136/latest/whole.html#DLM361606"
    label = "Family is caring for an orphan as per Social Security Act 1964"

    def formula(families, period, parameters):
        children = families.members(
            'social_security__is_a_child', period)
        orphaned = families.members('social_security__is_orphaned', period)
        resident_or_citizen = families.members(
            'is_citizen_or_resident', period)

        return families.any((children * orphaned * resident_or_citizen), role=Family.CHILD)


class social_security__is_orphaned(Variable):
    value_type = bool
    entity = Person
    definition_period = MONTH
    label = u"each of the child's natural or adoptive parents is dead, or cannot be found, or suffers a serious long-term disablement which renders him or her unable to care for the child"
