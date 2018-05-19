# -*- coding: utf-8 -*-

# Import from openfisca-core the common python objects used to code the legislation in OpenFisca
from openfisca_core.model_api import *
# Import the entities specifically defined for this tax and benefit system
from openfisca_aotearoa.entities import Person

#All variables are according to the reference link http://www.legislation.govt.nz/act/public/2006/0040/latest/DLM379487.html#DLM379487

class owned_home_before(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = u"Whether the prospective home buyer owned a home before"

class has_ks(Variable):
    value_type = bool
    entity = Person
    label = u"Whether the prospective home buyer has a kiwisaver account"

class ks_duration(Variable):
    value_type = int
    entity = Person
    definition_period = YEAR
    label = u"Years the prospective home buyer has been a member of a kiwisaver account"

class ks_contrib_duration:
    value_type = int
    entity = Person
    definition_period = YEAR
    label = u"Years the prospective home buyer has been contributing continuously to their kiwisaver account"
