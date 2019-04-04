# -*- coding: utf-8 -*-

from openfisca_core.model_api import *
from openfisca_aotearoa.entities import Person, Family


class acc__is_entitled_to_aids_and_appliances(Variable):
    value_type = bool
    entity = Person
    definition_period = MONTH
    reference = 'Section 81 & 82 http://www.legislation.govt.nz/act/public/2001/0049/latest/DLM101425.html'


class acc__is_entitled_to_attendant_care(Variable):
    value_type = bool
    entity = Person
    definition_period = MONTH
    reference = 'Section 81 & 82 http://www.legislation.govt.nz/act/public/2001/0049/latest/DLM101425.html'

    def formula(persons, period, parameters):
        return (persons('acc__has_a_covered_injury', period)
                * persons('acc__part_3__has_lodged_claim', period)
                * persons('acc__attendant_care__assessed_as_having_a_need_caused_by_this_covered_injury', period)
                * persons('acc__attendant_care__the_corporation_decides_to_provide_or_contribute_care', period)
                * persons('acc__attendant_care_is_necessary_and_appropriate', period)
                * persons('acc__attendant_care_is_of_the_quality_required_for_that_purpose', period)
                * (persons('acc__is_present_in_nz', period)
                   + persons('acc__number_of_days_outside_nz', period) <= 28)
                + persons('acc__the_corporation_exercised_discretion_for_attendant_care_as_per_section_68_3', period))  # TODO move 28 to a parameter


class acc__is_entitled_to_child_care(Variable):
    value_type = bool
    entity = Person
    definition_period = MONTH
    reference = 'Section 81 & 82 http://www.legislation.govt.nz/act/public/2001/0049/latest/DLM101425.html'

    def formula(persons, period, parameters):
        return (
            (persons.family('acc__family_has_child_care_eligible_children', period)
             + persons('acc__the_corporation_exercised_discretion_for_child_care_as_per_section_68_3', period)
             )
            * persons('acc__has_a_covered_injury', period)
            * persons('acc__part_3__has_lodged_claim', period)
            * persons('acc__assessed_as_having_a_child_care_need_caused_by_this_covered_injury', period)
            * persons('acc__entitlements__child_care__the_corporation_decides_to_provide_or_contribute', period)
            # ?? Is this a duplicate of the above line
            * persons('acc__child_care__corporation_has_regard_to_provide_or_contribute', period)
            * persons('acc__child_care_is_necessary_and_appropriate', period)
            * persons('acc__child_care_is_of_the_quality_required_for_that_purpose', period)
            * persons('acc__is_present_in_nz', period)
            * not_(persons('acc__child_care_continues_to_be_provided_by_person_who_lives_in_house', period))
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
    reference = 'Section 81 & 82 http://www.legislation.govt.nz/act/public/2001/0049/latest/DLM101425.html'

    def formula(persons, period, parameters):
        return persons('acc__is_present_in_nz', period)


class acc__is_entitled_to_home_help(Variable):
    value_type = bool
    entity = Person
    definition_period = MONTH
    reference = 'Section 81 & 82 http://www.legislation.govt.nz/act/public/2001/0049/latest/DLM101425.html'

    def formula(persons, period, parameters):
        return persons('acc__is_present_in_nz', period)


class acc__is_entitled_to_modifications_to_the_home(Variable):
    value_type = bool
    entity = Person
    definition_period = MONTH
    reference = 'Section 81 & 82 http://www.legislation.govt.nz/act/public/2001/0049/latest/DLM101425.html'

    def formula(persons, period, parameters):
        return persons('acc__is_present_in_nz', period)


class acc__is_entitled_to_training_for_independence(Variable):
    value_type = bool
    entity = Person
    definition_period = MONTH
    reference = 'Section 81 & 82 http://www.legislation.govt.nz/act/public/2001/0049/latest/DLM101425.html'

    def formula(persons, period, parameters):
        return persons('acc__is_present_in_nz', period)


class acc__is_entitled_to_transport_for_indepence(Variable):
    value_type = bool
    entity = Person
    definition_period = MONTH
    reference = 'Section 81 & 82 http://www.legislation.govt.nz/act/public/2001/0049/latest/DLM101425.html'

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
    label = 'has an ACC covered injury'


class acc__lodges_a_claim_for_entitlement(Variable):
    value_type = bool
    entity = Person
    definition_period = MONTH
    label = 'lodges a claim for entitlement'
