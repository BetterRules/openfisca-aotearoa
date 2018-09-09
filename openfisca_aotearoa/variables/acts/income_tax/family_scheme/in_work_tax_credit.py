# -*- coding: utf-8 -*-

from openfisca_core.model_api import *
from openfisca_aotearoa.entities import Person, Family


class family_scheme__in_work_tax_credit_entitlement(Variable):
    value_type = float
    entity = Person
    definition_period = MONTH
    label = u'The in-work tax credit entitlement a person has under the family scheme'
    reference = "http://www.legislation.govt.nz/act/public/2007/0097/latest/DLM1518521.html"

    def formula(persons, period, parameters):
        # TODO
        return persons

