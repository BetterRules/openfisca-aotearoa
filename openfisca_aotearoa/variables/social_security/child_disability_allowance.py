from openfisca_aotearoa.entities import Person, Family
from openfisca_core.model_api import *


class social_security__eligible_for_child_disability_allowance(Variable):
    value_type = bool
    entity = Person
    definition_period = MONTH
    label = "Eligible for Child Disability Allowance"
    reference = "https://www.workandincome.govt.nz/products/a-z-benefits/child-disability-allowance.html"

    def formula(persons, period, parameters):
        # The applicant
        in_nz = persons('normally_lives_in_nz', period)
        resident_or_citizen = persons('is_resident', period) + \
            persons('is_permanent_resident', period) + \
            persons('is_nz_citizen', period)

        is_principal_carer = persons.has_role(Family.PRINCIPAL_CAREGIVER)
        has_disabled_child = persons.family("social_security__family_has_disabled_child", period)

        return in_nz * \
            resident_or_citizen * \
            is_principal_carer * \
            has_disabled_child


class social_security__family_has_disabled_child(Variable):
    value_type = bool
    entity = Family
    definition_period = MONTH
    label = u'Does the family have a child who meets the criteria for disabled'
    reference = "http://legislation.govt.nz/bill/government/2017/0004/15.0/DLM7512349.html"

    def formula(families, period, parameters):
        has_disability = families.members('social_security__child_meets_child_disability_allowance_criteria', period)
        is_child = families.members('age', period) <= 18
        return families.any((has_disability * is_child), role=Family.CHILD)


class social_security__child_meets_child_disability_allowance_criteria(Variable):
    value_type = bool
    entity = Person
    label = u"Has serious disability"
    definition_period = MONTH

    def formula(persons, period, parameters):
        med_cert_required_months = 12
        return persons('social_security__has_serious_disability', period) * \
            persons('social_security__requires_constant_care_and_attention', period) * \
            (persons('social_security__medical_certification_months', period) >= med_cert_required_months)


class social_security__medical_certification_months(Variable):
    value_type = int
    entity = Person
    label = u"Number of future months the disability is expected to last for, in months"
    definition_period = MONTH


class social_security__has_serious_disability(Variable):
    value_type = bool
    entity = Person
    label = u"Has serious disability"
    definition_period = MONTH


class social_security__requires_constant_care_and_attention(Variable):
    value_type = bool
    entity = Person
    label = u"Requires constant care and attention"
    definition_period = MONTH
