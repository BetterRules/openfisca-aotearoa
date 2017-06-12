# -*- coding: utf-8 -*-

# This file defines the variables of our legislation.
# A variable is property of a person, or an entity (e.g. a household).
# See https://doc.openfisca.fr/variables.html

# Import from openfisca-core the common python objects used to code the legislation in OpenFisca
from openfisca_core.model_api import *
# Import the entities specifically defined for this tax and benefit system
from openfisca_country_template.entities import *

from numpy import datetime64


class age(Variable):
    column = IntCol
    entity = Person
    definition_period = MONTH
    label = u"Person's age (in years)"

    # A person's age is computed according to its birth date.
    def formula(person, period, legislation):
        birth = person('birth', period)
        return (datetime64(period.date) - birth).astype('timedelta64[Y]')


# This variable is a pure input: it doesn't have a formula
class birth(Variable):
    column = DateCol(default = date(1970, 1, 1))  # By default, is no value is set for a simulation, we consider the people involed in a simulation to be born on the 1st of Jan 1970.
    entity = Person
    label = u"Birth date"
    definition_period = ETERNITY  # This variable cannot change over time.
    url = "https://en.wiktionary.org/wiki/birthdate"
