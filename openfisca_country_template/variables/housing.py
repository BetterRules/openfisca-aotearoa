# -*- coding: utf-8 -*-

# This file defines the variables of our legislation.
# A variable is property of a person, or an entity (e.g. a household).
# See https://doc.openfisca.fr/variables.html

# Import from openfisca-core the common python objects used to code the legislation in OpenFisca
from openfisca_core.model_api import *
# Import the entities specifically defined for this tax and benefit system
from openfisca_country_template.entities import *


# This variable is a pure input: it doesn't have a formula
class accomodation_size(Variable):
    column = FloatCol
    entity = Household
    definition_period = MONTH
    label = u"Size of the accomodation, in square metters"


# This variable is a pure input: it doesn't have a formula
class rent(Variable):
    column = FloatCol
    entity = Household
    definition_period = MONTH
    label = u"Rent paid by the household"
