from openfisca_core.model_api import *
from openfisca_aotearoa.entities import Person


class acc__costs_incurred_outside_new_zealand(Variable):
    value_type = bool
    entity = Person
    definition_period = MONTH
    reference = "http://www.legislation.govt.nz/act/public/2001/0049/latest/DLM101809.html"
