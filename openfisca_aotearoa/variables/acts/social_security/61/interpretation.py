from openfisca_aotearoa.entities import Person
from openfisca_core.model_api import *

"""
http://legislation.govt.nz/act/public/1964/0136/latest/whole.html#DLM5468373
"""


class social_security__has_accomodation_costs(Variable):
    value_type = bool
    entity = Person
    label = u"Person has accommodation costs"
    definition_period = MONTH

    reference = "http://legislation.govt.nz/act/public/1964/0136/latest/whole.html#DLM362802"
    """
        accommodation costs, in relation to any person for any given period, means, -
        (a) in relation to premises rented by the person, the amount payable by the person for
            rent of the premises, excluding any service costs included in that rent and any arrears:
        (b) in relation to premises that are owned by the person, the total amount of all
            payments (including essential repairs and maintenance, local authority rates, and
            house insurance premiums, but excluding any service costs and any arrears) that -
        (i) subject to section 68A, are required to be made under any mortgage security for
            money advanced under that security to acquire the premises, or to repay advances
            similarly secured; or
        (ii) the chief executive is satisfied are reasonably required to be made:
        (c)in relation to a person who is a boarder or lodger in any premises, 62% of the amount
            paid for board or lodging (excluding any arrears):
        provided that, where a person is a joint tenant or owner in common of any premises with
            another person or other persons living in the premises, that applicant's accommodation
            costs shall be the share of the total accommodation costs of the premises that the
            chief executive is satisfied the person is paying
        """


class social_security__is_a_beneficiary(Variable):
    value_type = bool
    entity = Person
    label = "Person is a beneficiary"
    definition_period = MONTH
    reference = "http://www.legislation.govt.nz/act/public/1964/0136/latest/DLM362802.html#DLM362810"
    """beneficiary means any person who is being paid -
    (a) jobseeker support, sole parent support, a supported living payment,
        a youth payment, a young parent payment, or an emergency benefit; or
    (b) New Zealand superannuation or a veteran's pension
    """
    def formula(persons, period, parameters):
        return persons('social_security__is_being_paid_jobseeker_benefit', period) + \
            persons('social_security__is_being_paid_sole_parent_support', period) + \
            persons('social_security__is_being_paid_a_supported_living_payment', period) + \
            persons('social_security__is_being_paid_a_youth_payment', period) + \
            persons('social_security__is_being_paid_a_young_parent_payment', period) + \
            persons('social_security__is_being_paid_an_emergency_benefit', period) + \
            persons('super__is_being_paid_nz_superannuation', period) + \
            persons('veterans_support__is_being_paid_a_veterans_pension', period)


class social_security__is_being_paid_jobseeker_benefit(Variable):
    value_type = bool
    entity = Person
    label = "Is being paid Jobseeker"
    definition_period = MONTH


class social_security__is_being_paid_sole_parent_support(Variable):
    value_type = bool
    entity = Person
    label = "Is being paid sole parent support"
    definition_period = MONTH


class social_security__is_being_paid_a_supported_living_payment(Variable):
    value_type = bool
    entity = Person
    label = "Is being paid a supported living payment"
    definition_period = MONTH


class social_security__is_being_paid_a_youth_payment(Variable):
    value_type = bool
    entity = Person
    label = "Is being paid a a youth payment"
    definition_period = MONTH


class social_security__is_being_paid_a_young_parent_payment(Variable):
    value_type = bool
    entity = Person
    label = "Is being paid a a young parent payment"
    definition_period = MONTH


class social_security__is_being_paid_an_emergency_benefit(Variable):
    value_type = bool
    entity = Person
    label = "Is being paid a young parent payment"
    definition_period = MONTH
