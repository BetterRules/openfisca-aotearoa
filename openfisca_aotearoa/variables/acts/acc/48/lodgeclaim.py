# -*- coding: utf-8 -*-

# Import from openfisca-core the common python objects used to code the legislation in OpenFisca
from openfisca_core.model_api import *
# Import the entities specifically defined for this tax and entitlement system
from openfisca_aotearoa.entities import Person


class acc__part_3__has_lodged_claim(Variable):
    value_type = bool
    entity = Person
    definition_period = ETERNITY
    label = u"Has lodged a claim with the Corporation"
    reference = "http://www.legislation.govt.nz/act/public/2001/0049/latest/DLM100910.html"

    def formula(persons, period, parameters):
        return (
            persons('acc__lodged_claim_for_cover_for_personal_injury', period)
            + persons('acc__lodged_claim_for_cover_and_specified_entitlement_for_personal_injury', period)
            + persons('acc__assessed_as_having_a_need_caused_by_this_covered_injury', period)
        )

# - a specified entitlement for his or her personal injury, once the Corporation has accepted the person has cover for the personal injury.

# class acc__(Variable):
