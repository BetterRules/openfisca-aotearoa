# -*- coding: utf-8 -*-

from openfisca_core.model_api import *
from openfisca_aotearoa.entities import Person, Family


class family_scheme__parental_tax_credit_entitlement(Variable):
    value_type = float
    entity = Person
    definition_period = MONTH
    label = u'The parental tax credit entitlement a person has under the family scheme'
    reference = "http://www.legislation.govt.nz/act/public/2007/0097/latest/DLM1518546.html#DLM1518546"

    def formula(persons, period, parameters):
        # TODO
        return persons
