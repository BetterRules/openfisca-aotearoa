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


class social_security__eligible_for_job_seeker_support(Variable):
    value_type = bool
    entity = Person
    definition_period = MONTH
    label = "Eligible for Job Seeker Support"
    reference = "http://legislation.govt.nz/act/public/1964/0136/latest/DLM5478526.html"

    def formula(persons, period, parameters):
        # The applicant
        in_nz = persons('normally_lives_in_nz', period)
        resident_or_citizen = \
            persons('is_resident', period) + \
            persons('is_permanent_resident', period) + \
            persons('is_nz_citizen', period)

        years_in_nz = persons('job_seeker_support__meets_years_in_nz_requirement', period)
        age_requirement = persons('job_seeker_support__meets_age_threshold', period)

        # income low enough?
        income = persons('job_seeker_support__below_income_threshold', period)

        # Prepared to work
        prepared = persons('job_seeker_support__is_prepared_for_employment', period)
         
        # unable to work?
        unable_to_work = persons('is_unable_to_work', period) 
        
        return in_nz * resident_or_citizen * age_requirement * income * years_in_nz * prepared + \
            in_nz * resident_or_citizen * age_requirement * income * years_in_nz * unable_to_work 

class job_seeker_support__is_prepared_for_employment(Variable):
    value_type = bool
    default_value = True
    entity = Person
    label = u"Is prepared for employment?"
    definition_period = MONTH
    reference = "http://legislation.govt.nz/act/public/1964/0136/latest/DLM5478526.html"


class job_seeker_support__meets_age_threshold(Variable):
    value_type = bool
    default_value = True
    entity = Person
    label = u"Meets the age test for job seeker support?"
    definition_period = MONTH
    reference = "http://legislation.govt.nz/act/public/1964/0136/latest/DLM5478526.html"

    def formula(persons, period, parameters):
        # old enough? 
        age_threshold = parameters(period).entitlements.social_security.job_seeker_support.age_threshold
        return persons("age", period) >= age_threshold


class job_seeker_support__meets_years_in_nz_requirement(Variable):
    value_type = bool
    default_value = True
    entity = Person
    label = u"Meets the job seeker support test for number of years lived in nz"
    definition_period = MONTH
    reference = "http://legislation.govt.nz/act/public/1964/0136/latest/DLM363796.html#DLM363796"

    def formula(persons, period, parameters):
        # been in NZ log enough?
        min_years = parameters(period).entitlements.social_security.job_seeker_support.minumum_years_in_nz
        years_in_nz = persons('number_of_years_lived_in_nz', period)
        return years_in_nz >= min_years
