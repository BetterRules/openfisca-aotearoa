

from openfisca_core.model_api import *
from openfisca_aotearoa.entities import Person


class property_relationships__is_in_de_facto_relationship(Variable):
    value_type = bool
    entity = Person
    definition_period = MONTH
    label = "in a de facto relationship, a relationship between 2 persons (whether a man and a woman, or a man and a man, or a woman and a woman)"
    reference = "http://www.legislation.govt.nz/act/public/1976/0166/latest/DLM441113.html"
