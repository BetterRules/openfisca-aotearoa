# -*- coding: utf-8 -*-

from openfisca_core.model_api import *
from openfisca_aotearoa.entities import Person, Family


class family_scheme__base_qualifies(Variable):
    value_type = bool
    entity = Person
    definition_period = MONTH
    label = u'Is a person qualified as eligible under the family scheme'
    reference = "http://www.legislation.govt.nz/act/public/2007/0097/latest/DLM1518477.html"

    def formula(persons, period, parameters):
        age_qualifies = persons("family_scheme__caregiver_age_qualifies", period)
        principle_carer = persons("family_scheme__qualifies_as_principal_carer", period)
        residence = persons("income_tax__residence", period)  # this is for caregiver OR child, clarify the test

        return age_qualifies * principle_carer * residence


class family_scheme__caregiver_age_qualifies(Variable):
    value_type = bool
    entity = Person
    definition_period = MONTH
    label = u'Is a person qualified under the family scheme age parameters'
    reference = "http://legislation.govt.nz/act/public/2007/0097/latest/DLM1518479.html#DLM1518479"

    def formula(persons, period, parameters):
        print(period)
        print(period.start)
        return persons("age", period.start) >= parameters(period).entitlements.income_tax.family_scheme.principal_caregiver_age_threshold


class family_scheme__qualifies_as_principal_carer(Variable):
    value_type = bool
    entity = Person
    definition_period = MONTH
    label = u'Is the person the principal caregiver and do they have dependent children'
    reference = "http://legislation.govt.nz/act/public/2007/0097/latest/DLM1518480.html"

    def formula(persons, period, parameters):
        return persons.has_role(Family.PRINCIPAL_CAREGIVER) * persons.family("family_scheme__has_dependent_children", period)


class family_scheme__full_time_earner(Variable):
    value_type = int
    entity = Person
    definition_period = MONTH
    label = u'Does the hours per week the person is employed for qualify them as a full time earner'
    reference = "http://legislation.govt.nz/act/public/2007/0097/latest/DLM1518419.html"

    def formula(persons, period, parameters):
        has_partner = (persons('has_a_partner', period) > 0)
        hours_per_week_threshold = parameters(period).entitlements.social_security.family_scheme.hours_per_week_threshold
        hours_per_week_threshold_with_partner = parameters(period).entitlements.social_security.family_scheme.hours_per_week_threshold_with_partner

        return ((has_partner == 0) * (persons("hours_per_week_employed", period) >= hours_per_week_threshold)) +\
            ((has_partner > 0) * (persons.family.sum(persons.family.members("hours_per_week_employed", period, role=Family.PARTNER)) >= hours_per_week_threshold_with_partner))


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
        return families.max(families.members("income_tax__dependent_child", period.start))
