# -*- coding: utf-8 -*-

from openfisca_core.model_api import *
from openfisca_aotearoa.entities import Person


class acc__is_entitled_to_attendant_care(Variable):
    value_type = bool
    entity = Person
    definition_period = MONTH
    reference = "Section 81 & 82 http://www.legislation.govt.nz/act/public/2001/0049/latest/DLM101425.html"

    def formula(persons, period, parameters):
        return (
            persons('acc__has_a_covered_injury', period)
            * persons('acc__lodges_a_claim_for_entitlement', period)
            * persons('acc__assessed_as_having_a_need_caused_by_this_covered_injury', period)
            * person('acc__the_corporation_decides_to_provide_or_contribute_to_attendant_care', period)
            * (person('acc__is_present_in_nz', period)
               + person('acc__number_of_days_outside_nz', period) <= 28)) # TODO move 28 to a parameter


class acc__has_a_covered_injury(Variable):
    value_type = bool
    entity = Person
    definition_period = MONTH


class acc__lodges_a_claim_for_entitlement(Variable):
    value_type = bool
    entity = Person
    definition_period = MONTH


class acc__assessed_as_having_a_need_caused_by_this_covered_injury(Variable):
    value_type = bool
    entity = Person
    definition_period = MONTH
    reference = "Section 84 http://www.legislation.govt.nz/act/public/2001/0049/latest/DLM101430.html"

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
