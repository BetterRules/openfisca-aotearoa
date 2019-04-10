# -*- coding: utf-8 -*-

from openfisca_core.model_api import *
from openfisca_aotearoa.entities import Person


class acc__attendant_care__the_corporation_decides_to_provide_or_contribute_care(Variable):
    value_type = bool
    entity = Person
    definition_period = MONTH

    def formula(persons, period, parameters):
        return (
            persons('acc__entitlements__attendant_care__will_contribute_to_rehabilitation_outcome', period)
            * persons('acc__entitlements__attendant_care__extent_of_personal_injury_and_degree_of_impairment', period)
            * persons('acc__entitlements__attendant_care__to_engage_in_vocational_or_educational_activity', period)
            )


class acc__entitlements__attendant_care__will_contribute_to_rehabilitation_outcome(Variable):
    label = 'any rehabilitation outcome that would be achieved by providing it'
    value_type = bool
    entity = Person
    definition_period = DAY
    reference = "Schedule 1 clause 14 http://www.legislation.govt.nz/act/public/2001/0049/latest/DLM104597.html"


class acc__entitlements__attendant_care__extent_of_personal_injury_and_degree_of_impairment(Variable):
    label = 'the nature and extent of the claimant’s personal injury and the degree to which that injury impairs his or her ability to provide for his or her personal care'
    value_type = bool
    entity = Person
    definition_period = DAY
    reference = "Schedule 1 clause 14 http://www.legislation.govt.nz/act/public/2001/0049/latest/DLM104597.html"


class acc__entitlements__attendant_care__to_engage_in_vocational_or_educational_activity(Variable):
    label = 'the extent to which attendant care is necessary to enable the claimant to undertake or continue employment (including agreed vocational training) or to attend a place of education, having regard to any entitlement the claimant has to education support'
    value_type = bool
    entity = Person
    definition_period = DAY
    reference = "Schedule 1 clause 14 http://www.legislation.govt.nz/act/public/2001/0049/latest/DLM104597.html"

    def formula(persons, period, parameters):
        return (
            persons('acc__employment', period)
            * persons('acc__agreed_vocational_training', period)
            * persons('acc__attend_a_place_of_education_with_regard_to_entitlement_to_education_support', period)
            )


class acc__entitlements__attendant_care__household_family_might_reasonably_provide_care_after_injury(Variable):
    label = 'the extent to which household family members or other family members might reasonably be expected to provide attendant care for the claimant after the claimant’s personal injury'
    value_type = bool
    entity = Person
    definition_period = DAY
    reference = "Schedule 1 clause 14 http://www.legislation.govt.nz/act/public/2001/0049/latest/DLM104597.html"


class acc__entitlements__attendant_care__needed_to_give_break_to_household_family_members_or_family_members(Variable):
    label = 'the extent to which attendant care is required to give household family members a break, from time to time, from providing attendant care for the claimant'
    value_type = bool
    entity = Person
    definition_period = DAY
    reference = "Schedule 1 clause 14 http://www.legislation.govt.nz/act/public/2001/0049/latest/DLM104597.html"


class acc__entitlements__attendant_care__need_to_avoid_disruption_to_other_household_family_members_or_family_members(Variable):
    label = 'the need to avoid substantial disruption to the employment or other activities of the household family members.'
    value_type = bool
    entity = Person
    definition_period = DAY
    reference = "Schedule 1 clause 14 http://www.legislation.govt.nz/act/public/2001/0049/latest/DLM104597.html"


class acc__attendant_care_is_necessary_and_appropriate(Variable):
    value_type = bool
    entity = Person
    definition_period = MONTH
    label = 'key aspect is necessary and appropriate for that purpose'
    reference = 'section 81 (4) (c) (iv) http://www.legislation.govt.nz/act/public/2001/0049/latest/DLM101426.html'


class acc__attendant_care_is_of_the_quality_required_for_that_purpose(Variable):
    value_type = bool
    entity = Person
    definition_period = MONTH
    label = 'Attendant Care (key aspect) is of the quality required for that purpose'
    reference = 'section 81 (4) (c) (iv) http://www.legislation.govt.nz/act/public/2001/0049/latest/DLM101426.html'


class acc__attendant_care__assessed_as_having_a_need_caused_by_this_covered_injury(Variable):
    value_type = bool
    entity = Person
    definition_period = MONTH
    reference = 'Section 84 http://www.legislation.govt.nz/act/public/2001/0049/latest/DLM101430.html'
    label = 'was assess as having an Attendant Care need caused by this covered injury'

    # (4)      # The matters to be taken into account in an assessment or reassessment include—
    #   (a)    # the level of independence a claimant had before suffering the personal injury:
    #   (b)    # the level of independence a claimant has after suffering the personal injury:
    #   (c)    # the limitations suffered by a claimant as a result of the personal injury:
    #   (d)    # the kinds of social rehabilitation that are appropriate for a claimant to minimise those limitations:
    #   (e)    # the rehabilitation outcome that would be achieved by providing particular social rehabilitation:
    #   (f)    # the alternatives and options available for providing particular social rehabilitation so as to achieve the relevant rehabilitation outcome in the most cost effective way:
    #   (g)    # any social rehabilitation (not provided as vocational rehabilitation) that may reasonably be provided to enable a claimant who is entitled to vocational rehabilitation to participate in employment:
    #   (h)    # the geographical location in which a claimant lives:
    #   (i)    # in the case of a reassessment,—
    #     (i)  # whether any item that the Corporation provided for the purposes of social rehabilitation is in such a condition as to need replacing:
    #     (ii) # changes in the claimant’s condition or circumstances since the last assessment was undertaken.
