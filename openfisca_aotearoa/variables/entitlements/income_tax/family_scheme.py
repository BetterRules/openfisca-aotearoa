# -*- coding: utf-8 -*-

# Import from openfisca-core the common python objects used to code the legislation in OpenFisca
from openfisca_core.model_api import *
# Import the entities specifically defined for this tax and benefit system
from openfisca_aotearoa.entities import Person, Family


class income_tax__qualifies_for_entitlements_under_family_scheme(Variable):
    value_type = bool
    entity = Person
    definition_period = MONTH
    label = u'Boolean for if a person is classified as eligible under the family scheme'
    reference = "http://legislation.govt.nz/act/public/2007/0097/latest/DLM1518477.html"

    def formula(persons, period, parameters):
        age_qualifies = persons("income_tax__caregiver_age_qualifies_under_family_scheme", period)
        principle_carer = persons("income_tax__person_principal_carer_qualifies_under_family_scheme", period)
        residence = persons("income_tax__qualifies_for_residence_under_family_scheme", period)
        return age_qualifies * principle_carer * residence


class income_tax__caregiver_age_qualifies_under_family_scheme(Variable):
    value_type = bool
    entity = Person
    definition_period = MONTH
    label = u'A person is only eligible under the family scheme if they are as old or older than specified'
    reference = "http://legislation.govt.nz/act/public/2007/0097/latest/DLM1518479.html#DLM1518479"

    def formula(persons, period, parameters):
        return persons("age", period) >= 16  # TODO possibly set this as a parameter if it ever changes


class income_tax__qualifies_for_residence_under_family_scheme(Variable):
    value_type = bool
    entity = Person
    default_value = True  # TODO residency is required as defined in the act
    definition_period = MONTH
    label = u'A person is only eligible under the family scheme if they are a primary carer of 1 or more dependant persons'
    reference = "http://legislation.govt.nz/act/public/2007/0097/latest/DLM1518482.html"


class income_tax__person_principal_carer_qualifies_under_family_scheme(Variable):
    value_type = bool
    entity = Person
    definition_period = MONTH
    label = u'A person is only eligible under the family scheme if they are a primary carer of 1 or more dependant persons'
    reference = "http://legislation.govt.nz/act/public/2007/0097/latest/DLM1518480.html"

    def formula(persons, period, parameters):
        return persons.has_role(Family.PRINCIPAL_CAREGIVER) * persons.family("income_tax__family_has_dependent_children", period)


class income_tax__family_has_dependent_children(Variable):
    value_type = bool
    entity = Family
    definition_period = MONTH
    label = u'A family has one or more people who qualify as financially dependant children'
    reference = "http://legislation.govt.nz/act/public/2007/0097/latest/DLM1518480.html"

    def formula(families, period, parameters):
        return families.max(families.members("income_tax__dependent_child", period))


class income_tax__dependent_child(Variable):
    value_type = bool
    entity = Person
    definition_period = MONTH
    label = u'Determines if a Person is classified as financially dependant'
    reference = "http://legislation.govt.nz/act/public/2007/0097/latest/DLM1520575.html#DLM1520883"

    def formula(person, period, parameters):
        age = person('age', period)
        # TODO - It's not this simple, this needs to be tweaked to include the edge criteria above.
        # not in a marriage, civil union, or de facto relationship
        # is or less than 15
        # or 16 and 17 and not finanially independant
        # is 18 and many conditions (see act)
        return age <= 18
