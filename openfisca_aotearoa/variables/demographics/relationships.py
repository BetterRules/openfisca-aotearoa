# -*- coding: utf-8 -*-

# Import from openfisca-core the common python objects used to code the legislation in OpenFisca
from openfisca_core.model_api import *
# Import the entities specifically defined for this tax and benefit system
from openfisca_aotearoa.entities import Person, Family


# Re-usable variable for having a partner
class has_a_partner(Variable):
    value_type = bool
    entity = Person
    label = u"Is this person in a relationship?"
    definition_period = MONTH  # This variable changes over time.
    reference = u"TODO"

    def formula(persons, period, parameters):
        # has 1 or more partners
        number_of_partners = persons.family.nb_persons(role=Family.PARTNER)
        return number_of_partners >= 1


class is_adequately_supported_by_partner(Variable):
    value_type = bool
    entity = Person
    label = u"""Is adequately supported by their partner? (false if lost the regular support of
    their partner as their partner has been imprisoned or is subject to release or detention conditions that prevent employment)
    """
    definition_period = MONTH
    reference = u"https://www.workandincome.govt.nz/map/income-support/main-benefits/sole-parent-support/qualifications.html"
    default_value = True


class is_a_parent(Variable):
    value_type = bool
    entity = Person
    definition_period = MONTH
    label = "Is a parent?"


class is_a_step_parent(Variable):
    value_type = bool
    entity = Person
    definition_period = MONTH
    label = "Is a step-parent?"


class is_married(Variable):
    value_type = bool
    entity = Person
    definition_period = MONTH
    label = "Is married?"

    def formula(persons, period, parameters):
        return persons('marriage__is_married', period)


class is_in_civil_union(Variable):
    value_type = bool
    entity = Person
    definition_period = MONTH
    label = "Is in a civil union?"

    def formula(persons, period, parameters):
        return persons('civil_union__is_in_civil_union', period)


class is_in_de_facto_relationship(Variable):
    value_type = bool
    entity = Person
    definition_period = MONTH
    label = "Is in a de facto relationship?"

    def formula(persons, period, parameters):
        return persons('property_relationships__is_in_de_facto_relationship', period)


class has_been_married_or_in_a_civil_union_or_de_facto_relationship(Variable):
    value_type = bool
    entity = Person
    definition_period = MONTH
    label = "He or she is not married but has been married or in a civil union or de facto relationship"


class is_married_or_in_a_civil_union_or_de_facto_relationship(Variable):
    value_type = bool
    entity = Person
    definition_period = MONTH
    label = "He or she is married, or in a civil union or de facto relationship"

    def formula(persons, period, parameters):
        return persons('is_married', period) + persons('is_in_civil_union', period) + persons('is_in_de_facto_relationship', period)
