from openfisca_core.model_api import *
from openfisca_aotearoa.entities import Person


class acc__corporation_has_regard_to_provide_or_contribute_to_child_care(Variable):
    label = 'deciding whether to provide or contribute to the cost of child care, the Corporation must have regard to'
    value_type = bool
    entity = Person
    definition_period = DAY

    def formula(persons, period, parameters):
        return (
            persons('acc__entitlements__child_care__will_contribute_to_rehabilitation_outcome', period)
            * persons('acc__entitlements__child_care__number_of_claiments_children_requiring_child_care', period)
            * persons('acc__entitlements__child_care__previous_child_care_was_provided_by_household_family_members', period)
            * persons('acc__entitlements__child_care__need_to_avoid_disruption_to_other_family_members', period)
        )

class acc__entitlements__child_care__will_contribute_to_rehabilitation_outcome(Variable):
    label = 'any rehabilitation outcome that would be achieved by providing it'
    value_type = bool
    entity = Person
    definition_period = DAY
    reference = "Schedule 1 clause 15 http://www.legislation.govt.nz/act/public/2001/0049/latest/DLM104598.html"
    # needs more precise reference

class acc__entitlements__child_care__number_of_claimants_children_requiring_child_care(Variable):
    label = 'the number of the claimant’s children and their need for child care'
    value_type = bool
    entity = Person
    definition_period = DAY
    reference = "Schedule 1 clause 15 http://www.legislation.govt.nz/act/public/2001/0049/latest/DLM104598.html"
    # needs more precise reference

class acc__entitlements__child_care__previous_child_care_was_provided_by_household_family_members(Variable):
    label = 'the extent to which child care was provided by other household family members before the claimant’s personal injury'
    value_type = bool
    entity = Person
    definition_period = DAY
    reference = "Schedule 1 clause 15 http://www.legislation.govt.nz/act/public/2001/0049/latest/DLM104598.html"
    # needs more precise reference

class acc__entitlements__child_care__household_family_might_reasonably_provide_care_after_injury(Variable):
    label = 'the extent to which other household family members or other family members might reasonably be expected to provide child care services after the claimant’s personal injury'
    value_type = bool
    entity = Person
    definition_period = DAY
    reference = "Schedule 1 clause 15 http://www.legislation.govt.nz/act/public/2001/0049/latest/DLM104598.html"
    # needs more precise reference

class acc__entitlements__child_care__need_to_avoid_disruption_to_other_family_members(Variable):
    label = 'the need to avoid substantial disruption to the employment or other activities of the household family members.'
    value_type = bool
    entity = Person
    definition_period = DAY
    reference = "Schedule 1 clause 15 http://www.legislation.govt.nz/act/public/2001/0049/latest/DLM104598.html"
    # needs more precise reference
