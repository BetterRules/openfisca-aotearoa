# -*- coding: utf-8 -*-

from openfisca_core.model_api import *
from openfisca_aotearoa.entities import Person


class immigration__holds_resident_visa(Variable):
    value_type = bool
    entity = Person
    definition_period = MONTH
    label = u"Holder of a resident visa"


class immigration__holds_permanent_resident_visa(Variable):
    value_type = bool
    entity = Person
    definition_period = ETERNITY
    label = u"Holder of a permanent resident visa"


class is_resident(Variable):
    value_type = bool
    entity = Person
    definition_period = ETERNITY
    label = u"Holder of a permanent resident visa or a resident visa"
    reference = "Immigration Act 2009 (interpretation) http://legislation.govt.nz/act/public/2009/0051/latest/whole.html#DLM1440311"

    def formula(persons, period, parameters):
        return persons('immigration__holds_resident_visa', period) + persons('immigration__holds_permanent_resident_visa', period)


class is_permanent_resident(Variable):
    value_type = bool
    entity = Person
    definition_period = ETERNITY
    label = u"Holder of a permanent resident visa"
    reference = "Immigration Act 2009 (interpretation) http://legislation.govt.nz/act/public/2009/0051/latest/whole.html#DLM1440311"

    def formula(persons, period, parameters):
        return persons('immigration__holds_permanent_resident_visa', period)


class is_nz_citizen(Variable):
    value_type = bool
    entity = Person
    definition_period = ETERNITY
    label = u"""New Zealand citizen means a person who has New Zealand citizenship as provided in
        the Citizenship Act 1977 or the Citizenship (Western Samoa) Act 1982"""
    reference = "Immigration Act 2009 (interpretation) http://legislation.govt.nz/act/public/2009/0051/latest/whole.html#DLM1440311"


class is_citizen_or_resident(Variable):
    value_type = bool
    entity = Person
    definition_period = ETERNITY
    label = u"NZ Citizen or Resident"
    reference = "Immigration Act 2009 (interpretation) http://legislation.govt.nz/act/public/2009/0051/latest/whole.html#DLM1440311"

    def formula(persons, period, parameters):
        return persons('is_nz_citizen', period) + persons('is_permanent_resident', period) + persons('is_resident', period)


class immigration__is_recognised_refugee(Variable):
    value_type = bool
    entity = Person
    definition_period = MONTH
    label = u"is recognised as a refugee"


class immigration__is_protected_person(Variable):
    value_type = bool
    entity = Person
    definition_period = MONTH
    label = u"is recognised as a a protected person in New Zealand"
