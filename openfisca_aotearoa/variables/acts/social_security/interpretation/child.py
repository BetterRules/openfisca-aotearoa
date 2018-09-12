# -*- coding: utf-8 -*-

# Import from openfisca-core the common python objects used to code the legislation in OpenFisca
from openfisca_core.model_api import *
# Import the entities specifically defined for this tax and benefit system
from openfisca_aotearoa.entities import Person


class social_security__has_dependant_child(Variable):
    value_type = bool
    entity = Person
    label = u"has a dependent child (or children)"
    definition_period = MONTH


class social_security__is_a_child(Variable):
    value_type = bool
    entity = Person
    label = u"""child means a single person under the age of 18 years, other than a person who is—
        (a) aged 16 years or 17 years; and
        (b) financially independent
        """
    definition_period = MONTH
    reference = u""

    def formula(persons, period, parameters):
        under_16 = persons('age', period) < 16
        under_18 = persons('age', period) < 18

        financially_independent = persons(
            'social_security__is_financially_independent', period)

        return under_16 + (under_18 * not_(financially_independent))


class social_security__has_child_in_family(Variable):
    value_type = bool
    entity = Person
    definition_period = MONTH

    def formula(persons, period, parameters):
        children = families.members('social_security__is_a_child', period)
        return families.any(children, role=Family.CHILD)
