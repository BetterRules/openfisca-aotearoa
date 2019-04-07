# -*- coding: utf-8 -*-

from openfisca_core.model_api import *
from openfisca_aotearoa.entities import Person


class is_of_full_capacity(Variable):
    value_type = bool
    entity = Person
    definition_period = ETERNITY
    label = "is of full capacity (a person shall be deemed to be of full capacity if he is not of unsound mind)"
    reference = "http://www.legislation.govt.nz/act/public/1977/0061/latest/DLM443689.html#DLM443689"


class date_of_injury(Variable):
    value_type = date
    entity = Person
    label = u"Date of injury, ACC act does not explicitly define this term but does add to it for specific circumstances"
    definition_period = ETERNITY  # This variable cannot change over time.
    reference = u""
