# -*- coding: utf-8 -*-

# All the objects defined or imported here will be available in all your legislation files

# Import from openfisca-core the common python objects used to code the legislation in OpenFisca
from openfisca_core.model_api import *

# Import the entities specifically defined for this tax and benefit system
from openfisca_country_template.entities import Household, Person
