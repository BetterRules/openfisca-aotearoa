# -*- coding: utf-8 -*-

from openfisca_core.model_api import *
from openfisca_aotearoa.entities import Person, Family


class family_scheme__qualifies_for_entitlements(Variable):
    value_type = bool
    entity = Person
    definition_period = MONTH
    label = u'Is a person is classified as eligible under the family scheme'
    reference = "http://www.legislation.govt.nz/act/public/2007/0097/latest/DLM1518477.html"

    def formula(persons, period, parameters):
        received_tested_benefit = persons('social_security__received_income_tested_benefit', period)
        received_parents_allowance = persons('veterans_support__received_parents_allowance', period)
        received_childrens_pension = persons('veterans_support__received_childrens_pension', period)
        age_qualifies = persons("family_scheme__caregiver_age_qualifies", period)
        principle_carer = persons("family_scheme__qualifies_as_principal_carer", period)
        residence = persons("income_tax__residence", period)
        return not_(received_tested_benefit) * not_(received_parents_allowance) * not_(received_childrens_pension) * age_qualifies * principle_carer * residence
        # TODO - Add remaining eligibility criteria as per legislation.


class family_scheme__caregiver_age_qualifies(Variable):
    value_type = bool
    entity = Person
    definition_period = MONTH
    label = u'Is a person  eligible under the family scheme age parameters'
    reference = "http://legislation.govt.nz/act/public/2007/0097/latest/DLM1518479.html#DLM1518479"

    def formula(persons, period, parameters):
        return persons("age", period) >= parameters(period).entitlements.income_tax.working_for_families.principal_caregiver_age_threshold


class family_scheme__qualifies_as_principal_carer(Variable):
    value_type = bool
    entity = Person
    definition_period = MONTH
    label = u'Is the person the principal caregiver and do they have dependent children'
    reference = "http://legislation.govt.nz/act/public/2007/0097/latest/DLM1518480.html"

    def formula(persons, period, parameters):
        return persons.has_role(Family.PRINCIPAL_CAREGIVER) * persons.family("family_scheme__has_dependent_children", period)


class family_scheme__proportion_as_principal_carer(Variable):
    value_type = float
    entity = Person
    default_value = 1
    definition_period = MONTH
    label = u'Expression of the amount of time the child is with the family and principal carer where 1 is "all the time"'
    reference = "http://legislation.govt.nz/act/public/2007/0097/latest/DLM1518454.html#DLM1518454"


class family_scheme__assessable_income(Variable):
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


class family_scheme__assessable_income_for_month(Variable):
    base_function = missing_value
    value_type = float
    entity = Person
    definition_period = MONTH
    label = u'The monthly net income for a person as relates to the family scheme'
    reference = "http://legislation.govt.nz/act/public/2007/0097/latest/DLM1518454.html#DLM1518454"

    def formula(persons, period, parameters):
        return persons('family_scheme__assessable_income', period, options=[DIVIDE])


class family_scheme__has_dependent_children(Variable):
    value_type = bool
    entity = Family
    definition_period = MONTH
    label = u'A family has one or more people who qualify as financially dependant children'
    reference = "http://legislation.govt.nz/act/public/2007/0097/latest/DLM1518480.html"

    def formula(families, period, parameters):
        return families.max(families.members("income_tax__dependent_child", period))

