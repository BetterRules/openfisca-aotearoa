from openfisca_core.model_api import *
from openfisca_aotearoa.entities import Person

class acc__is_present_in_nz(Variable):
    value_type = bool
    entity = Person
    definition_period = DAY

class acc__number_of_days_outside_nz(Variable):
    value_type = bool
    entity = Person
    definition_period = DAY

    def formula(persons, period, parameters):
        # TODO calculate from last time they left
        persons('acc__is_present_in_nz', period) + 0