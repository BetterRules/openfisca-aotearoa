# -*- coding: utf-8 -*-

# Import from openfisca-core the common python objects used to code the legislation in OpenFisca
from openfisca_core.model_api import *
# Import the entities specifically defined for this tax and entitlement system
from openfisca_aotearoa.entities import Person



class super__living_alone(Variable):
    value_type = int
    entity = Person
    definition_period = MONTH
    label = u"Is a person considered as living alone"
    reference = "http://www.legislation.govt.nz/act/public/2001/0084/latest/whole.html#DLM5578822"


