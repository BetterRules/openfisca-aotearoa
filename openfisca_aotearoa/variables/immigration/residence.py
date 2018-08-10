# -*- coding: utf-8 -*-

from openfisca_core.model_api import *
from openfisca_aotearoa.entities import Person


class is_resident(Variable):
    value_type = bool
    entity = Person
    definition_period = ETERNITY
    label = u"Holder of a permanent resident visa or a resident visa"
    reference = "Immigration Act 2009 (interpretation) http://legislation.govt.nz/act/public/2009/0051/latest/whole.html#DLM1440311"


class is_permanent_resident(Variable):
    value_type = bool
    entity = Person
    definition_period = ETERNITY
    label = u"Holder of a permanent resident visa"
    reference = "Immigration Act 2009 (interpretation) http://legislation.govt.nz/act/public/2009/0051/latest/whole.html#DLM1440311"


class is_nz_citizen(Variable):
    value_type = bool
    entity = Person
    definition_period = ETERNITY
    label = u"New Zealand citizen means a person who has New Zealand citizenship as provided in the Citizenship Act 1977 or the Citizenship (Western Samoa) Act 1982"
    reference = "Immigration Act 2009 (interpretation) http://legislation.govt.nz/act/public/2009/0051/latest/whole.html#DLM1440311"


class number_of_years_lived_in_nz(Variable):
    value_type = int
    entity = Person
    definition_period = ETERNITY
    label = u"Number of years lived in NZ"
