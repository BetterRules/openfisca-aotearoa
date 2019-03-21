# -*- coding: utf-8 -*-

# Import from openfisca-core the common python objects used to code the legislation in OpenFisca
from openfisca_core.model_api import *
# Import the entities specifically defined for this tax and entitlement system
from openfisca_aotearoa.entities import Person
from numpy import logical_not


class acc_sched_1__minimum_weekly_earnings(Variable):
    value_type = float
    entity = Person
    definition_period = DAY
    label = u"Minimum weekly earnings"
    reference = "http://www.legislation.govt.nz/act/public/2001/0049/latest/DLM104874.html"
