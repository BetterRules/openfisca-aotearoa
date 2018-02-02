# -*- coding: utf-8 -*-

# This file defines the variables of our legislation.
# A variable is property of a person, or an entity (e.g. a household).
# See http://openfisca.org/doc/variables.html

# Import from openfisca-core the common python objects used to code the legislation in OpenFisca
from openfisca_core.model_api import *
# Import the entities specifically defined for this tax and benefit system
from openfisca_country_template.entities import *

from numpy import datetime64


class age(Variable):
    # By default, you can use utf-8 characters in a variable. OpenFisca web API manages utf-8 encoding.
    value_type = int
    entity = Person
    definition_period = MONTH
    label = u"Person's age (in years). In french : Âge d'une personne (en années)."
    reference = u"https://ar.wikipedia.org/wiki/العمر"

    def formula(person, period, parameters):
        '''
        A person's age is computed according to its birth date.
        In french : L'âge d'une personne est calculé d'après sa date de naissance.
        '''
        birth = person('birth', period)
        return (datetime64(period.date) - birth).astype('timedelta64[Y]')


# This variable is a pure input: it doesn't have a formula
class birth(Variable):
    value_type = date
    default_value = date(1970, 1, 1)  # By default, is no value is set for a simulation, we consider the people involed in a simulation to be born on the 1st of Jan 1970.
    entity = Person
    label = u"Birth date"
    definition_period = ETERNITY  # This variable cannot change over time.
