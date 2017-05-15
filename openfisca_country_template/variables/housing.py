# -*- coding: utf-8 -*-

# Import from openfisca-core the common python objects used to code the legislation in OpenFisca
from openfisca_core.model_api import *
# Import the entities specifically defined for this tax and benefit system
from openfisca_country_template.entities import *


class accomodation_size(Variable):
    column = FloatCol
    entity = Household
    definition_period = MONTH
    label = u"Size of the accomodation, in square metters"
