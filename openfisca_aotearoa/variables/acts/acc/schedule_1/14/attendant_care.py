# -*- coding: utf-8 -*-

from openfisca_core.model_api import *
from openfisca_aotearoa.entities import Person


class acc__the_corporation_decides_to_provide_or_contribute_to_attendant_care(Variable):
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
    # needs more precise reference

class acc__entitlements__attendant_care__extent_of_personal_injury_and_degree_of_impairment(Variable):
    label = 'the nature and extent of the claimant’s personal injury and the degree to which that injury impairs his or her ability to provide for his or her personal care'
    value_type = bool
    entity = Person
    definition_period = DAY
    reference = "Schedule 1 clause 14 http://www.legislation.govt.nz/act/public/2001/0049/latest/DLM104597.html"
    # needs more precise reference

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
    # needs more precise reference

class acc__entitlements__attendant_care__needed_to_give_break_to_household_family_members_or_family_members(Variable):
    label = 'the extent to which attendant care is required to give household family members a break, from time to time, from providing attendant care for the claimant'
    value_type = bool
    entity = Person
    definition_period = DAY
    reference = "Schedule 1 clause 14 http://www.legislation.govt.nz/act/public/2001/0049/latest/DLM104597.html"
    # needs more precise reference

class acc__entitlements__attendant_care__need_to_avoid_disruption_to_other_household_family_members_or_family_members(Variable):
    label = 'the need to avoid substantial disruption to the employment or other activities of the household family members.'
    value_type = bool
    entity = Person
    definition_period = DAY
    reference = "Schedule 1 clause 14 http://www.legislation.govt.nz/act/public/2001/0049/latest/DLM104597.html"
    # needs more precise reference
