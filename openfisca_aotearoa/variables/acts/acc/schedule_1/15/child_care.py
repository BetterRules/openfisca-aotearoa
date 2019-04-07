from openfisca_core.model_api import *
from openfisca_aotearoa.entities import Person, Family


class acc__child_care__corporation_has_regard_to_provide_or_contribute(Variable):
    label = 'deciding whether to provide or contribute to the cost of child care, the Corporation must have regard to'
    value_type = bool
    entity = Person
    definition_period = DAY

    def formula(persons, period, parameters):
        return (
            persons('acc__child_care_will_contribute_to_rehabilitation_outcome', period)
            * persons('acc__entitlements__child_care__number_of_claimants_children_requiring_child_care', period)
            * persons('acc__entitlements__child_care__previous_child_care_was_provided_by_household_family_members', period)
            * persons('acc__entitlements__child_care__need_to_avoid_disruption_to_other_family_members', period)
            )


class acc__child_care_is_necessary_and_appropriate(Variable):
    value_type = bool
    entity = Person
    definition_period = MONTH


class acc__child_care_continues_to_be_provided_by_person_who_lives_in_house(Variable):
    label = 'who lives in the claimant’s home or lived in the claimant’s home'
    value_type = bool
    entity = Person
    definition_period = MONTH
    # NOTE: This reference is WRONG
    reference = "http://www.legislation.govt.nz/act/public/2001/0049/latest/DLM104598.html"

    def formula(persons, period, parameters):
        """The Corporation is not required to pay for child care to the extent that
        child care continues to be provided after a claimant’s personal injury by a person—
        (a)   who lives in the claimant’s home or lived in the claimant’s home immediately
              before the claimant suffered his or her personal injury; and
        (b)   who provided child care before the claimant suffered his or her personal injury.
        """

        return (persons('acc__person_provided_child_care_before_claimants_injury_and_continues_to_provide_that_care', period)
                * (persons('acc__child_carer_lived_in_claimants_home_immediately_before', period)
                   + persons('acc__child_carer_currently_lives_in_claimants_home', period)
                   )
                )


class acc__child_care_will_contribute_to_rehabilitation_outcome(Variable):
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


class acc__already_receiving_child_care_from_acc_as_a_child_of_a_desceased_claimant(Variable):
    value_type = bool
    entity = Person
    definition_period = DAY


class acc__family_has_child_care_eligible_children(Variable):
    value_type = bool
    entity = Family
    definition_period = MONTH
    label = u'Family has children eligible to be considered children and needing child care'
    # reference = "http://legislation.govt.nz/bill/government/2017/0004/15.0/DLM7512349.html"

    def formula(families, period, parameters):
        needs_care = families.members('acc__is_child_of_claimant_and_needs_child_care_because_of_his_or_her_physical_or_mental_condition', period)
        already_receiving_fatal = families.members('acc__already_receiving_child_care_from_acc_as_a_child_of_a_desceased_claimant', period)
        already_receiving_general = families.members('acc__child_is_in_reciept_of_attendent_care_or_education_support_or_training_for_independence', period)
        children = families.members('age', period) < 14
        # is a child, or needs care because of ability  AND not already reciving as a child of a deceased claimant
        childcare_eligible = ((children + needs_care) * not_(already_receiving_fatal) * not_(already_receiving_general))
        return families.any(childcare_eligible, role=Family.CHILD)


class acc__child_carer_currently_lives_in_claimants_home(Variable):
    value_type = bool
    entity = Person
    definition_period = MONTH


class acc__child_carer_lived_in_claimants_home_immediately_before(Variable):
    value_type = bool
    entity = Person
    definition_period = MONTH


class acc__person_provided_child_care_before_claimants_injury_and_continues_to_provide_that_care(Variable):
    value_type = bool
    entity = Person
    definition_period = MONTH


class acc__entitlements__child_care__the_corporation_decides_to_provide_or_contribute(Variable):
    value_type = bool
    entity = Person
    definition_period = MONTH


class acc__is_child_of_claimant_and_needs_child_care_because_of_his_or_her_physical_or_mental_condition(Variable):
    value_type = bool
    entity = Person
    definition_period = MONTH


class acc__child_care_is_of_the_quality_required_for_that_purpose(Variable):
    value_type = bool
    entity = Person
    definition_period = MONTH
    label = 'Child Care (key aspect) is of the quality required for that purpose'
    reference = 'section 81 (4) (c) (iv) http://www.legislation.govt.nz/act/public/2001/0049/latest/DLM101426.html'


class acc__assessed_as_having_a_child_care_need_caused_by_this_covered_injury(Variable):
    value_type = bool
    entity = Person
    definition_period = MONTH
    reference = 'Section 84 http://www.legislation.govt.nz/act/public/2001/0049/latest/DLM101430.html'
    label = 'was assess as having a Child Care need caused by this covered injury'
