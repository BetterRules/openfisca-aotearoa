# -*- coding: utf-8 -*-

from openfisca_core.model_api import *
from openfisca_aotearoa.entities import Person, Family


class income_tax__qualifies_for_entitlements_under_family_scheme(Variable):
    value_type = bool
    entity = Person
    definition_period = MONTH
    label = u'Is a person is classified as eligible under the family scheme'
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
    label = u'Is a person  eligible under the family scheme age parameters'
    reference = "http://legislation.govt.nz/act/public/2007/0097/latest/DLM1518479.html#DLM1518479"

    def formula(persons, period, parameters):
        return persons("age", period) >= parameters(period).entitlements.income_tax.working_for_families.principal_caregiver_age_threshold


class income_tax__person_principal_carer_qualifies_under_family_scheme(Variable):
    value_type = bool
    entity = Person
    definition_period = MONTH
    label = u'Is the person the principal caregiver and do they have dependent children'
    reference = "http://legislation.govt.nz/act/public/2007/0097/latest/DLM1518480.html"

    def formula(persons, period, parameters):
        return persons.has_role(Family.PRINCIPAL_CAREGIVER) * persons.family("income_tax__family_has_dependent_children", period)


class income_tax__proportion_as_principal_carer(Variable):
    value_type = float
    entity = Person
    default_value = 1
    definition_period = MONTH
    label = u'Expression of the amount of time the child is with the family and principal carer where 1 is "all the time"'
    reference = "http://legislation.govt.nz/act/public/2007/0097/latest/DLM1518454.html#DLM1518454"


class income_tax__family_scheme_income(Variable):
    base_function = missing_value
    value_type = float
    entity = Person
    definition_period = YEAR
    label = u'The annual net income for a person as relates to the family scheme'
    reference = "http://legislation.govt.nz/act/public/2007/0097/latest/DLM1518454.html#DLM1518454"
    # Allows user to declare a salary for a year. OpenFisca will spread the yearly amount over the months contained in the year.
    set_input = set_input_divide_by_period

    # TODO there is a myriad of conditions on this variable that represent a large body of work.
    # def formula(person, period, parameters):
    # See legislation reference above however currently "A person’s family scheme income is an amount
    # based on their net income" is possibly the most common use case scenario
    # return person('income_tax__net_income', period)


class income_tax__family_scheme_income_for_month(Variable):
    base_function = missing_value
    value_type = float
    entity = Person
    definition_period = MONTH
    label = u'The monthly net income for a person as relates to the family scheme'
    reference = "http://legislation.govt.nz/act/public/2007/0097/latest/DLM1518454.html#DLM1518454"

    def formula(persons, period, parameters):
        return persons('income_tax__family_scheme_income', period, options=[DIVIDE])
