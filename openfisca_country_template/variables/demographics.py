# -*- coding: utf-8 -*-

# Import from openfisca-core the common python objects used to code the legislation in OpenFisca
from openfisca_core.model_api import *
# Import the entities specifically defined for this tax and benefit system
from openfisca_country_template.entities import *


class age(Variable):
    column = IntCol(default = 40)  # By default, is no value is set for a simulation, we consider the people involed in a simulation to be 40.
    entity = Person
    definition_period = MONTH
    label = u"Person's age"
