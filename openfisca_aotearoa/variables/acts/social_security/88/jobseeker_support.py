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
    reference = """
    88B Jobseeker support: standard eligibility requirements
    An applicant for jobseeker support
        (a) must be aged at least 18 years, in the case of an applicant without a dependent child:
        (b) must be aged at least 20 years, in any other case.
    http://legislation.govt.nz/act/public/1964/0136/latest/whole.html#DLM5478527
    """

    def formula(persons, period, parameters):
        # over the simpler age threshold
        jobseeker_age = parameters(period).entitlements.social_security.jobseeker_support.age_threshold
        over_age_threshold = persons("age", period) >= jobseeker_age

        # over the threshold for appliants with a dependent child
        jobseeker_age_with_dependent_child = parameters(period).entitlements.social_security.jobseeker_support.age_threshold_with_dependent_child
        has_dependent_child = persons('social_security__has_dependant_child', period)
        over_age_threshold_with_dependent_child = (persons("age", period) >= jobseeker_age_with_dependent_child) * has_dependent_child

        return over_age_threshold + over_age_threshold_with_dependent_child


class social_security__eligible_for_jobseeker_support(Variable):
    value_type = bool
    entity = Person
    definition_period = MONTH
    label = "Eligible for Job Seeker Support"
    reference = """
    88B Jobseeker support: standard eligibility requirements
        (1) A person is entitled to jobseeker support if he or she satisfies the criteria in subsections (2), (3), and (4), and
        (a) is not in full-time employment, but
            (i) is seeking it; and
            (ii) is available for it; and
            (iii) is willing and able to undertake it; and
            (iv) has taken reasonable steps to find it; or
        (b) is not in full-time employment, but would comply with subparagraphs (i) to (iv) of paragraph (a) but for circumstances that would qualify the person
            for an exemption under section 105 from some or all work test obligations; or
        (c) is not in full-time employment and is willing to undertake it but, because of sickness, injury, or disability, is limited in his or her capacity to
            seek, undertake, or be available for it; or
        (d) is in employment, but is losing earnings because, through sickness or injury, he or she is not working at all, or is working only at a
            reduced level.
        """

    def formula(persons, period, parameters):
        # The applicant
        residency_requirements = persons('social_security__meets_residential_requirements_for_certain_benefits', period)

        age_requirement = persons('jobseeker_support__meets_age_threshold', period)

        # income low enough?
        income = persons('jobseeker_support__below_income_threshold', period)

        # Prepared to work
        prepared = persons('jobseeker_support__is_prepared_for_employment', period)

        return age_requirement * income * prepared * residency_requirements
