# -*- coding: utf-8 -*-

from openfisca_core.model_api import *
from openfisca_aotearoa.entities import Person


class acc__fullfils_purpose_of_act(Variable):
    label = "The purpose of this Act is to enhance the public good and reinforce the social contract represented by the first accident compensation scheme by providing for a fair and sustainable scheme for managing personal injury that has, as its overriding goals, minimising both the overall incidence of injury in the community, and the impact of injury on the community (including economic, social, and personal costs),"
    value_type = bool
    entity = Person
    definition_period = MONTH
    reference = "Section 3 http://www.legislation.govt.nz/act/public/2001/0049/latest/DLM100100.html"

    def formula(persons, period, parameters):
        return (
            (persons('acc__promotes_measures_to_reduce_incidence_and_severity_of_personal_injury', period)
             + persons('acc__the_corporation_exercised_discretion_for_child_care_as_per_section_68_3', period)
             )
            * persons('acc__has_a_covered_injury', period)
            * persons('acc__part_3__has_lodged_claim', period)
            * persons('acc__assessed_as_having_a_need_caused_by_this_covered_injury', period)
            )


class acc__promotes_measures_to_reduce_incidence_and_severity_of_personal_injury(Variable):
    value_type = bool
    entity = Person
    definition_period = MONTH
    label = "establishing as a primary function of the Corporation the promotion of measures to reduce the incidence and severity of personal injury"

# (b)

# providing for a framework for the collection, co-ordination, and analysis of injury-related information:
# (c)

# ensuring that, where injuries occur, the Corporation’s primary focus should be on rehabilitation with the goal of achieving an appropriate quality of life through the provision of entitlements that restores to the maximum practicable extent a claimant’s health, independence, and participation:
# (d)

# ensuring that, during their rehabilitation, claimants receive fair compensation for loss from injury, including fair determination of weekly compensation and, where appropriate, lump sums for permanent impairment:
# (e)

# ensuring positive claimant interactions with the Corporation through the development and operation of a Code of ACC Claimants’ Rights:
# (f)

# ensuring that persons who suffered personal injuries before the commencement of this Act continue to receive entitlements where appropriate.
