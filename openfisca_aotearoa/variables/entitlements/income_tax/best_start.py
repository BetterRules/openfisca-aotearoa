# -*- coding: utf-8 -*-

# Import from openfisca-core the common python objects used to code the legislation in OpenFisca
from openfisca_core.model_api import *
# Import the entities specifically defined for this tax and benefit system
from openfisca_aotearoa.entities import Person, Family
from numpy import datetime64


class income_tax__caregiver_eligible_for_best_start_tax_credit(Variable):
    value_type = bool
    entity = Person
    definition_period = MONTH
    label = u'Is each person classified as eligible for best start tax credit'
    reference = "http://legislation.govt.nz/bill/government/2017/0004/15.0/DLM7512349.html"

    def formula(persons, period, parameters):
        qualifies = persons("income_tax__qualifies_for_entitlements_under_family_scheme", period)
        family_is_eligible = persons.family("income_tax__family_has_children_eligible_for_best_start", period)
        return qualifies * family_is_eligible


class income_tax__family_has_children_eligible_for_best_start(Variable):
    value_type = bool
    entity = Family
    definition_period = MONTH
    label = u'Is each family classified as eligible for best start tax credit'
    reference = "http://legislation.govt.nz/bill/government/2017/0004/15.0/DLM7512349.html"

    def formula(families, period, parameters):
        families_have_children_born_after_launch_date = families.max(families.members("date_of_birth", period) >= datetime64('2018-06-01'))
        families_have_children_due_after_launch_date = families.max(families.members("due_date_of_birth", period) >= datetime64('2018-06-01'))
        families_have_children_younger_than_three_years = families("age_of_youngest", period) < 3
        return ((families_have_children_born_after_launch_date + families_have_children_due_after_launch_date) > 0) * families_have_children_younger_than_three_years


class income_tax__best_start_tax_credit_per_child(Variable):
    value_type = float
    entity = Person
    definition_period = MONTH
    label = u'Value of a Families entitlement for best start tax credit'
    reference = "http://legislation.govt.nz/bill/government/2017/0004/15.0/DLM7512349.html"

    def formula(persons, period, parameters):
        threshold = parameters(period).entitlements.income_tax.best_start.full_year_abatement_threshold
        rate = parameters(period).entitlements.income_tax.best_start.full_year_abatement_rate
        prescribed_amount = parameters(period).entitlements.income_tax.best_start.prescribed_amount

        # sum up families income
        family_income = persons.family.sum(persons.family.members("income_tax__family_scheme_income", period.this_year))  # TODO understand the period approach

        # calculate income over the threshold
        income_over_threshold = where((family_income - threshold) < 0, 0, family_income - threshold)

        # work out the ages for each family member
        ages = persons('age', period)

        # work out if each dependant child is eligible for full best start tax credit
        dependant_eligible_full = (ages < 1) * prescribed_amount

        # work out if each dependant child is eligible for abated best start tax credit
        dependant_eligible_abated_1 = (ages == 1) * (prescribed_amount - (income_over_threshold * rate))

        dependant_eligible_abated_2 = (ages == 2) * (prescribed_amount - (income_over_threshold * rate))

        # sum up the entitlement for each child
        return dependant_eligible_full + dependant_eligible_abated_1 + dependant_eligible_abated_2


class income_tax__entitlement_for_best_start_tax_credit(Variable):
    value_type = float
    entity = Person
    definition_period = MONTH
    label = u'The total value the principal carer is entitled to for the best start tax credit'
    reference = "http://legislation.govt.nz/bill/government/2017/0004/15.0/DLM7512349.html"

    def formula(persons, period, parameters):

        # sum up families income
        return persons.family.sum(persons.family.members("income_tax__best_start_tax_credit_per_child", period)) * persons("income_tax__caregiver_eligible_for_best_start_tax_credit", period)
