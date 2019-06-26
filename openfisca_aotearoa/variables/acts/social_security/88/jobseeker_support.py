from openfisca_aotearoa.entities import Person
from openfisca_core.model_api import *


class jobseeker_support__is_prepared_for_employment(Variable):
    value_type = bool
    default_value = True
    entity = Person
    label = u"Is prepared for employment?"
    definition_period = MONTH
    reference = "TODO"


class jobseeker_support__meets_age_threshold(Variable):
    value_type = bool
    default_value = True
    entity = Person
    label = u"Meets the age test for Jobseeker Support?"
    definition_period = MONTH
    reference = "http://legislation.govt.nz/act/public/1964/0136/latest/DLM5478527.html"

    def formula(persons, period, parameters):
        # over the simpler age threshold
        jobseeker_age = parameters(period).entitlements.social_security.jobseeker_support.age_threshold
        over_age_threshold = persons("age", period.start) >= jobseeker_age

        # over the threshold for appliants with a dependent child
        jobseeker_age_with_dependent_child = parameters(period).entitlements.social_security.jobseeker_support.age_threshold_with_dependent_child
        has_dependent_child = persons('social_security__has_dependant_child', period)
        over_age_threshold_with_dependent_child = (persons("age", period.start) >= jobseeker_age_with_dependent_child) * has_dependent_child

        return over_age_threshold + over_age_threshold_with_dependent_child


class social_security__eligible_for_jobseeker_support(Variable):
    value_type = bool
    entity = Person
    definition_period = MONTH
    label = "Eligible for Job Seeker Support"
    reference = "http://legislation.govt.nz/act/public/1964/0136/latest/DLM5478527.html"

    def formula(persons, period, parameters):
        # The applicant
        residency_requirements = persons('social_security__meets_residential_requirements_for_certain_benefits', period)

        age_requirement = persons('jobseeker_support__meets_age_threshold', period)

        # income low enough?
        income = persons('jobseeker_support__below_income_threshold', period)

        # Prepared to work
        prepared = persons('jobseeker_support__is_prepared_for_employment', period)

        return age_requirement * income * prepared * residency_requirements
