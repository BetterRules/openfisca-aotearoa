from openfisca_aotearoa.entities import Person
from openfisca_core.model_api import *

# """
# Benefit: JobSeeker Support (eligibility):
#     If applicant.employmentStatus != "full-time"
#         and 18 <= applicant.Age
#         and applicant.isNZResident
#         and applicant.hasLivedInNZfor2Years
#         and applicant.normallyLivesInNZ
#         and recipient.prepareForEmployment
#         and threshold.income.JobSeekerSupport
#     then benefit.isJobSeekerSupport is PERMITTED
# """


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
    An applicant for jobseeker support
        (a) must be aged at least 18 years, in the case of an applicant without a dependent child:
        (b) must be aged at least 20 years, in any other case.
    """

    def formula(persons, period, parameters):
        # over the simpler age threshold
        jobseeker_age = parameters(period).entitlements.social_security.jobseeker_support.age_threshold
        over_age_threshold = persons("age", period) >= jobseeker_age

        # over the threshold for appliants with a dependent child
        jobseeker_age_with_dependent_child = parameters(period).entitlements.social_security.jobseeker_support.age_threshold_with_dependent_child
        has_dependent_child = persons('social_security__has_dependant_child', period)
        over_age_threshold_with_dependent_child = (persons("age", period) >= jobseeker_age_with_dependent_child) * has_dependent_child

        print(over_age_threshold_with_dependent_child)

        return over_age_threshold + over_age_threshold_with_dependent_child


class jobseeker_support__meets_years_in_nz_requirement(Variable):
    value_type = bool
    default_value = True
    entity = Person
    label = u"Meets the Jobseeker Support test for number of years lived in nz"
    definition_period = MONTH
    reference = "TODO"

    def formula(persons, period, parameters):
        # been in NZ log enough?
        min_years = parameters(period).entitlements.social_security.jobseeker_support.minumum_years_in_nz
        years_in_nz = persons('number_of_years_lived_in_nz', period)
        return years_in_nz >= min_years


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
        in_nz = persons('normally_lives_in_nz', period)
        resident_or_citizen = persons('is_citizen_or_resident', period)

        years_in_nz = persons('jobseeker_support__meets_years_in_nz_requirement', period)

        age_requirement = persons('jobseeker_support__meets_age_threshold', period)

        # income low enough?
        income = persons('jobseeker_support__below_income_threshold', period)

        # Prepared to work
        prepared = persons('jobseeker_support__is_prepared_for_employment', period)

        return in_nz * resident_or_citizen * \
            age_requirement * income * prepared * years_in_nz
