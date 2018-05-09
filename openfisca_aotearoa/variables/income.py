# -*- coding: utf-8 -*-

# Import from openfisca-core the common python objects used to code the legislation in OpenFisca
from openfisca_core.model_api import *
# Import the entities specifically defined for this tax and benefit system
from openfisca_aotearoa.entities import *


class salary(Variable):
    value_type = float
    entity = Person
    definition_period = YEAR
    set_input = set_input_divide_by_period  # Allows user to declare a salary for a year. OpenFisca will spread the yearly amount over the months contained in the year.
    label = "Salary"
