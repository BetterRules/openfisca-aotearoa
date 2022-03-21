from openfisca_aotearoa.entities import Person
from openfisca_core.model_api import *

"""
#     Benefit: Part 1E Supported Living Payment (eligible self applicant):
#     If applicant.isNZResident
#         and 16 <= applicant.Age
#         and applicant.hasMedicalCertificate
#         and applicant.hasSeriousDisability
#         and threshold.income.SupportedLivingPayment
#     then benefit.isSupportedLivingPayment is PERMITTED
"""


class social_security__is_required_to_give_fulltime_care(Variable):
    value_type = bool
    entity = Person
    definition_period = MONTH
    label = "Eligible for Supported Living Payment."
    reference = """40A (1)(c) People who are required to give full-time care and attention
                at home to some other person (other than their spouse or partner) who is a
                patient requiring care."""


class supported_living_payment__below_income_threshold(Variable):
    value_type = bool
    entity = Person
    definition_period = MONTH
    label = "Income below threshold for supported living payment"
    reference = "TODO"


class social_security__eligible_for_supported_living_payment(Variable):
    value_type = bool
    entity = Person
    definition_period = MONTH
    label = "Eligible for Supported Living Payment."
    reference = """
        http://legislation.govt.nz/act/public/1964/0136/latest/whole.html#DLM5468367
        40A Supported living payment: purpose
        (1) The purpose of the supported living payment is to provide income support
            to people because they are people who fall within any one of the following 3 categories:
        (a) people who have, and are likely to have in the future, a severely restricted
            capacity to support themselves through open employment because of sickness, injury, or disability:
        (b) people who are totally blind:
        (c) people who are required to give full-time care and attention at home to some
            other person (other than their spouse or partner) who is a patient requiring care.
    """

    def formula(persons, period, parameters):
        # The 3 ways of being eligible
        disabled = persons('social_security__has_severely_restricted_capacity_for_work', period)
        blind = persons('social_security__is_totally_blind', period)
        carer = persons('social_security__is_required_to_give_fulltime_care', period)

        # 40B (4) A person who is not both permanently and severely restricted in his or her capacity for
        # work must not be granted a supported living payment under this section, unless he or she is totally blind.

        # 40B (5) A person must not be granted a supported living payment under this section if the chief
        # executive is satisfied that the person's restricted capacity for work, or total blindness, was
        # self-inflicted and brought about by the person with a view to qualifying for a benefit.
        not_self_inflicted = not_(persons('social_security__disability_was_self_inflicted', period))

        # 40B (1A) An applicant for the supported living payment under
        # this section must be aged at least 16 years.
        is_old_enough = persons('age', period.start) >= 16

        # 40B (1B) An applicant for the supported living payment under
        # this section must meet the residential requirements in section 74AA.
        is_resident_or_citizen = persons('is_citizen_or_resident', period)

        resides_in_nz = persons('social_security__meets_residential_requirements_for_certain_benefits', period)

        # # income low enough?
        income = persons('supported_living_payment__below_income_threshold', period)

        return resides_in_nz * (disabled + blind + carer) * not_self_inflicted * is_old_enough * is_resident_or_citizen * income
