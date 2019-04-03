# -*- coding: utf-8 -*-

from openfisca_core.model_api import *
from openfisca_aotearoa.entities import Person, Family


class acc__is_entitled_to_aids_and_appliances(Variable):
    value_type = bool
    entity = Person
    definition_period = MONTH
    reference = "Section 81 & 82 http://www.legislation.govt.nz/act/public/2001/0049/latest/DLM101425.html"


class acc__is_entitled_to_attendant_care(Variable):
    value_type = bool
    entity = Person
    definition_period = MONTH
    reference = "Section 81 & 82 http://www.legislation.govt.nz/act/public/2001/0049/latest/DLM101425.html"

    def formula(persons, period, parameters):
        return (persons('acc__has_a_covered_injury', period)
                * persons('acc__part_3__has_lodged_claim', period)
                * persons('acc__assessed_as_having_a_need_caused_by_this_covered_injury', period)
                * persons('acc__the_corporation_decides_to_provide_or_contribute_to_attendant_care', period)
                * persons('acc__key_aspect_is_necessary_and_appropriate', period)
                * persons('acc__key_aspect_is_of_the_quality_required_for_that_purpose', period)
                * (persons('acc__is_present_in_nz', period)
                   + persons('acc__number_of_days_outside_nz', period) <= 28)
                + persons('acc__the_corporation_exercised_descretion_for_attendant_care_as_per_section_68_3', period))  # TODO move 28 to a parameter


class acc__is_entitled_to_child_care(Variable):
    value_type = bool
    entity = Person
    definition_period = MONTH
    reference = "Section 81 & 82 http://www.legislation.govt.nz/act/public/2001/0049/latest/DLM101425.html"

    def formula(persons, period, parameters):
        return (
            (persons('acc__claminant_has_child_care_eligible_children', period)
             + persons('acc__the_corporation_exercised_descretion_for_child_care_as_per_section_68_3', period)
             )
            * persons('acc__has_a_covered_injury', period)
            * persons('acc__part_3__has_lodged_claim', period)
            * persons('acc__assessed_as_having_a_need_caused_by_this_covered_injury', period)
            * persons('acc__the_corporation_decides_to_provide_or_contribute_to_child_care', period)
            * persons('acc__key_aspect_is_necessary_and_appropriate', period)
            * persons('acc__key_aspect_is_of_the_quality_required_for_that_purpose', period)
            * persons('acc__is_present_in_nz', period)
            * persons('acc__corporation_has_regard_to_provide_or_contribute_to_child_care', period)

            )


class acc__claminant_has_child_care_eligible_children(Variable):
    # TODO any child in family who is 14 or under
    # OR 14+ and needs care due to phydical or mental condition
    value_type = bool
    entity = Person
    definition_period = MONTH

    def formula(persons, period, parameters):
        return persons.family("acc__family_has_child_care_eligible_children", period)


class acc__family_has_child_care_eligible_children(Variable):
    value_type = bool
    entity = Family
    definition_period = MONTH
    label = u''
    # reference = "http://legislation.govt.nz/bill/government/2017/0004/15.0/DLM7512349.html"

    def formula(families, period, parameters):
        needs_care = families.members('acc__needs_child_care_because_of_his_or_her_physical_or_mental_condition', period)
        already_receiving = families.members('acc__already_receiving_child_care_from_acc_as_a_child_of_a_desceased_claimant', period)
        children = families.members('age', period) < 14
        # is a child, or needs care because of ability  AND not already reciving as a child of a deceased claimant
        childcare_eligible = ((children + needs_care) * not_(already_receiving))
        return families.any(childcare_eligible, role=Family.CHILD)


class acc__is_entitled_to_education_support(Variable):
    value_type = bool
    entity = Person
    definition_period = MONTH
    reference = "Section 81 & 82 http://www.legislation.govt.nz/act/public/2001/0049/latest/DLM101425.html"

    def formula(persons, period, parameters):
        return persons('acc__is_present_in_nz', period)


class acc__is_entitled_to_home_help(Variable):
    value_type = bool
    entity = Person
    definition_period = MONTH
    reference = "Section 81 & 82 http://www.legislation.govt.nz/act/public/2001/0049/latest/DLM101425.html"

    def formula(persons, period, parameters):
        return persons('acc__is_present_in_nz', period)


class acc__is_entitled_to_modifications_to_the_home(Variable):
    value_type = bool
    entity = Person
    definition_period = MONTH
    reference = "Section 81 & 82 http://www.legislation.govt.nz/act/public/2001/0049/latest/DLM101425.html"

    def formula(persons, period, parameters):
        return persons('acc__is_present_in_nz', period)


class acc__is_entitled_to_training_for_indepence(Variable):
    value_type = bool
    entity = Person
    definition_period = MONTH
    reference = "Section 81 & 82 http://www.legislation.govt.nz/act/public/2001/0049/latest/DLM101425.html"

    def formula(persons, period, parameters):
        return persons('acc__is_present_in_nz', period)


class acc__is_entitled_to_transport_for_indepence(Variable):
    value_type = bool
    entity = Person
    definition_period = MONTH
    reference = "Section 81 & 82 http://www.legislation.govt.nz/act/public/2001/0049/latest/DLM101425.html"

    def formula(persons, period, parameters):
        return persons('acc__is_present_in_nz', period)


class acc__has_a_covered_injury(Variable):
    value_type = bool
    entity = Person
    definition_period = MONTH
    label = "has an ACC covered injury"

# IS this needed?
# will we say really "No, you're not entitled because you've not lodged a claim"


class acc__lodges_a_claim_for_entitlement(Variable):
    value_type = bool
    entity = Person
    definition_period = MONTH
    label = "lodges a claim for entitilement"


class acc__assessed_as_having_a_need_caused_by_this_covered_injury(Variable):
    value_type = bool
    entity = Person
    definition_period = MONTH
    reference = "Section 84 http://www.legislation.govt.nz/act/public/2001/0049/latest/DLM101430.html"
    label = "was assess as having a need caused by this covered injury"

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


class acc__key_aspect_is_necessary_and_appropriate(Variable):
    value_type = bool
    entity = Person
    definition_period = MONTH
    label = "key aspect is necessary and appropriate for that purpose"
    reference = "section 81 (4) (c) (iv) http://www.legislation.govt.nz/act/public/2001/0049/latest/DLM101426.html"


class acc__key_aspect_is_of_the_quality_required_for_that_purpose(Variable):
    value_type = bool
    entity = Person
    definition_period = MONTH
    label = "key aspect is of the quality required for that purpose"
    reference = "section 81 (4) (c) (iv) http://www.legislation.govt.nz/act/public/2001/0049/latest/DLM101426.html"
