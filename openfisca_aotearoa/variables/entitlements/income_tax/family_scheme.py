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
        residence = persons("income_tax__residence", period)
        return age_qualifies * principle_carer * residence


class income_tax__caregiver_age_qualifies_under_family_scheme(Variable):
    value_type = bool
    entity = Person
    definition_period = MONTH
    label = u'A person is only eligible under the family scheme if they are as old or older than specified'
    reference = "http://legislation.govt.nz/act/public/2007/0097/latest/DLM1518479.html#DLM1518479"

    def formula(persons, period, parameters):
        return persons("age", period) >= 16  # TODO possibly set this as a parameter if it ever changes


class income_tax__person_principal_carer_qualifies_under_family_scheme(Variable):
    value_type = bool
    entity = Person
    definition_period = MONTH
    label = u'A person is only eligible under the family scheme if they are a primary carer of 1 or more dependant persons'
    reference = "http://legislation.govt.nz/act/public/2007/0097/latest/DLM1518480.html"

    def formula(persons, period, parameters):
        return persons.has_role(Family.PRINCIPAL_CAREGIVER) * persons.family("income_tax__family_has_dependent_children", period)
