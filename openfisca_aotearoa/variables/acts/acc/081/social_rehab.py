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
                * persons('acc__assessed_as_having_an_attendant_care_need_caused_by_this_covered_injury', period)
                * persons('acc__the_corporation_decides_to_provide_or_contribute_to_attendant_care', period)
                * persons('acc__attendant_care_is_necessary_and_appropriate', period)
                * persons('acc__attendant_care_is_of_the_quality_required_for_that_purpose', period)
                * (persons('acc__is_present_in_nz', period)
                   + persons('acc__number_of_days_outside_nz', period) <= 28)
                + persons('acc__the_corporation_exercised_discretion_for_attendant_care_as_per_section_68_3', period))  # TODO move 28 to a parameter


class acc__is_entitled_to_child_care(Variable):
    value_type = bool
    entity = Person
    definition_period = MONTH
    reference = "Section 81 & 82 http://www.legislation.govt.nz/act/public/2001/0049/latest/DLM101425.html"

    def formula(persons, period, parameters):
        return (
            (persons('acc__claimant_has_child_care_eligible_children', period)
             + persons('acc__the_corporation_exercised_discretion_for_child_care_as_per_section_68_3', period)
             )
            * persons('acc__has_a_covered_injury', period)
            * persons('acc__part_3__has_lodged_claim', period)
            * persons('acc__assessed_as_having_a_child_care_need_caused_by_this_covered_injury', period)
            * persons('acc__the_corporation_decides_to_provide_or_contribute_to_child_care', period)
            * persons('acc__child_care_is_necessary_and_appropriate', period)
            * persons('acc__child_care_is_of_the_quality_required_for_that_purpose', period)
            * persons('acc__is_present_in_nz', period)
            * persons('acc__corporation_has_regard_to_provide_or_contribute_to_child_care', period)
            * persons('acc__child_care_continues_to_be_provided_by_person_who_lives_in_house', period)

            )


class acc__person_provided_child_care_before_claimants_injury:
    label = 'who lives in the claimant’s home or lived in the claimant’s home'
    value_type = bool
    entity = Person
    definition_period = MONTH


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


class acc__is_entitled_to_training_for_independence(Variable):
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


class acc__child_is_in_reciept_of_attendent_care_or_education_support_or_training_for_independence(Variable):
    value_type = bool
    entity = Person
    definition_period = MONTH


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
    label = "lodges a claim for entitlement"


class acc__assessed_as_having_a_child_care_need_caused_by_this_covered_injury(Variable):
    value_type = bool
    entity = Person
    definition_period = MONTH
    reference = "Section 84 http://www.legislation.govt.nz/act/public/2001/0049/latest/DLM101430.html"
    label = "was assess as having a Child Care need caused by this covered injury"


class acc__assessed_as_having_an_attendant_care_need_caused_by_this_covered_injury(Variable):
    value_type = bool
    entity = Person
    definition_period = MONTH
    reference = "Section 84 http://www.legislation.govt.nz/act/public/2001/0049/latest/DLM101430.html"
    label = "was assess as having an Attendant Care need caused by this covered injury"

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


class acc__attendant_care_is_necessary_and_appropriate(Variable):
    value_type = bool
    entity = Person
    definition_period = MONTH
    label = "key aspect is necessary and appropriate for that purpose"
    reference = "section 81 (4) (c) (iv) http://www.legislation.govt.nz/act/public/2001/0049/latest/DLM101426.html"


class acc__attendant_care_is_of_the_quality_required_for_that_purpose(Variable):
    value_type = bool
    entity = Person
    definition_period = MONTH
    label = "Attendant Care (key aspect) is of the quality required for that purpose"
    reference = "section 81 (4) (c) (iv) http://www.legislation.govt.nz/act/public/2001/0049/latest/DLM101426.html"


class acc__child_care_is_of_the_quality_required_for_that_purpose(Variable):
    value_type = bool
    entity = Person
    definition_period = MONTH
    label = "Child Care (key aspect) is of the quality required for that purpose"
    reference = "section 81 (4) (c) (iv) http://www.legislation.govt.nz/act/public/2001/0049/latest/DLM101426.html"
