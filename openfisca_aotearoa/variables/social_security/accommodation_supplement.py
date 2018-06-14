"""
    age => 16
    normally_lives_in_nz: True
    is_nz_resident: True
    has_accomodation_costs: True
    has_social_housing: False
    accommodation_supplement__below_income_threshold: True
    accommodation_supplement__below_cash_threshold: True
"""
from openfisca_aotearoa.entities import Person, Family
from openfisca_core.model_api import *


class accommodation_supplement__benefit_eligible(Variable):
    value_type = bool
    entity = Person
    definition_period = MONTH
    label = "Eligible for Accommodation Supplement"
    reference = "TODO"

    def formula(persons, period, parameters):
        pass
