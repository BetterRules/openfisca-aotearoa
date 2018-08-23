# -*- coding: utf-8 -*-

# Import from openfisca-core the common python objects used to code the legislation in OpenFisca
from openfisca_core.model_api import *
# Import the entities specifically defined for this tax and benefit system
from openfisca_aotearoa.entities import Person


class has_dependent_child(Variable):
    value_type = bool
    entity = Person
    label = u"""Is adequately supported by their partner? (false if lost the regular support of
    their partner as their partner has been imprisoned or is subject to release or detention conditions that prevent employment)
    """
    definition_period = MONTH
    default_value = True


class living_with_parent_or_guardian(Variable):
    value_type = bool
    entity = Person
    label = "is living with a parent or guardian"
    definition_period = MONTH


class financially_supported_by_parent_or_guardian(Variable):
    value_type = bool
    entity = Person
    label = "is being financially supported by a parent or guardian"
    definition_period = MONTH
