from openfisca_aotearoa.entities import Person, Family
from openfisca_core.model_api import *

"""
MSD Policy (retrieved August 2018 from )
    https://www.workandincome.govt.nz/products/a-z-benefits/sole-parent-support.html

You may get Sole Parent Support if you are:

    * aged 20 or older
    * a single parent or caregiver with one or more dependent children under 14
    * not in a relationship
    * without adequate financial support
    * a New Zealand citizen or permanent resident who has been here for at least two years
    at any one time since becoming a citizen or permanent resident, and who normally lives here.
"""


class social_security__eligible_for_sole_parent_support(Variable):
    value_type = bool
    entity = Person
    definition_period = MONTH
    label = "Eligible for Sole Parent Support"
    reference = "https://www.workandincome.govt.nz/map/income-support/main-benefits/sole-parent-support/qualifications.html"

    def formula(persons, period, parameters):
        # The applicant
        resides_in_nz = persons('social_security__meets_residential_requirements_for_certain_benefits', period)
        resident_or_citizen = persons('is_citizen_or_resident', period)

        years_in_nz = persons('sole_parent_support__meets_years_in_nz_requirement', period)
        age_requirement = persons('sole_parent_support__meets_age_threshold', period)
        child_age_requirement = persons.family('sole_parent_support__family_has_child_under_age_limit', period)

        relationship_test = persons('sole_parent_support__meets_relationship_qualification', period)
        # TODO isInadequatelySupportedByPartner
        # TODO isMaintainingChild

        # income low enough?
        low_income = persons('sole_parent_support__below_income_threshold', period)

        return resides_in_nz * resident_or_citizen * years_in_nz *\
            age_requirement * child_age_requirement * \
            relationship_test * low_income


class sole_parent_support__meets_relationship_qualification(Variable):
    value_type = bool
    default_value = True
    entity = Person
    label = u"Meets the sole parent support test for not being in a relationship"
    definition_period = MONTH
    reference = "https://www.workandincome.govt.nz/map/income-support/main-benefits/sole-parent-support/qualifications.html"

    """
     be one of the following:
        * living apart from their partner and lost the support or being inadequately
            maintained by the spouse or partner
        * divorced or had their civil union dissolved
        * single (never had a partner)
        * has lost the regular support of their partner as their partner has been imprisoned or
            is subject to release or detention conditions that prevent employment or
        * their spouse or partner has died
    """
    def formula(persons, period, parameters):
        # Do they have a partner
        no_partners = (persons('has_a_partner', period) == 0)
        not_supported = (persons('is_adequately_supported_by_partner', period) == 0)
        # no partner, OR not supported by partner
        return no_partners + not_supported


class sole_parent_support__family_has_child_under_age_limit(Variable):
    value_type = bool
    entity = Family
    definition_period = MONTH
    label = u'Does the family have a child who meets the criteria for disabled'

    def formula(families, period, parameters):
        youngest_child_age_threshold = parameters(period).entitlements.social_security.sole_parent_support.youngest_child_age_threshold
        youngest_ages = families('age_of_youngest', period.start)
        return youngest_ages < youngest_child_age_threshold


class sole_parent_support__meets_age_threshold(Variable):
    value_type = bool
    default_value = True
    entity = Person
    label = u"Meets the age test for sole parent support?"
    definition_period = MONTH
    reference = "https://www.workandincome.govt.nz/products/a-z-benefits/sole-parent-support.html"

    def formula(persons, period, parameters):
        # old enough?
        age_threshold = parameters(period).entitlements.social_security.sole_parent_support.age_threshold
        return persons("age", period.start) >= age_threshold


class sole_parent_support__meets_years_in_nz_requirement(Variable):
    value_type = bool
    default_value = True
    entity = Person
    label = u"Has lived continuously in New Zealand for 2 years or more at any one time since becoming a New Zealand citizen or permanent resident?"
    definition_period = MONTH
    reference = "TODO"

    def formula(persons, period, parameters):
        # been in NZ log enough?
        min_years = parameters(period).entitlements.social_security.sole_parent_support.minumum_continuous_time_in_nz
        years_in_nz = persons('number_of_years_lived_in_nz', period)
        return years_in_nz >= min_years
