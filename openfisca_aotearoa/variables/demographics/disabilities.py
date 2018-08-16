# -*- coding: utf-8 -*-

# Import from openfisca-core the common python objects used to code the legislation in OpenFisca
from openfisca_core.model_api import *
# Import the entities specifically defined for this tax and benefit system
from openfisca_aotearoa.entities import Person, Family


class has_serious_disability(Variable):
    value_type = bool
    entity = Person
    label = u"TODO"
    definition_period = MONTH
    reference = u"TODO"
    default_value = False


class has_permanent_and_severe_disability(Variable):
    value_type = bool
    entity = Person
    label = u"TODO"
    definition_period = MONTH
    reference = u"TODO"
    default_value = False


class is_totally_blind(Variable):
    value_type = bool
    entity = Person
    label = u"""Is adequately supported by their partner? (false if lost the regular support of
    their partner as their partner has been imprisoned or is subject to release or detention conditions that prevent employment)
    """
    definition_period = MONTH
    reference = u"TODO"
    default_value = False


class disability_was_self_inflicted(Variable):
    value_type = bool
    entity = Person
    label = u"""40B (5) if the chief executive is satisfied that the person’s restricted capacity for work, or total blindness,
    was self-inflicted and brought about by the person with a view to qualifying for a benefit
    """
    definition_period = MONTH
    reference = u"TODO"
    default_value = False
