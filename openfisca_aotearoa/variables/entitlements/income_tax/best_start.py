# -*- coding: utf-8 -*-

# Import from openfisca-core the common python objects used to code the legislation in OpenFisca
from openfisca_core.model_api import *
# Import the entities specifically defined for this tax and benefit system
from openfisca_aotearoa.entities import Person, Family
from numpy import datetime64


class income_tax__family_has_children_eligible_for_best_start(Variable):
    value_type = bool
    entity = Family
    definition_period = MONTH
    label = u'Boolean for if a family is classified as eligible for best start tax credit'
    reference = "http://legislation.govt.nz/bill/government/2017/0004/15.0/DLM7512349.html"

    def formula(families, period, parameters):
        families_have_children_born_after_launch_date = families.max(families.members("date_of_birth", period) >= datetime64('2018-06-01'))
        families_have_children_due_after_launch_date = families.max(families.members("due_date_of_birth", period) >= datetime64('2018-06-01'))
        families_have_children_younger_than_three_years = families("age_of_youngest", period) < 3
        return ((families_have_children_born_after_launch_date + families_have_children_due_after_launch_date) > 0) * families_have_children_younger_than_three_years


class income_tax__caregiver_eligible_for_best_start_tax_credit(Variable):
    value_type = bool
    entity = Person
    definition_period = MONTH
    label = u'Boolean for if a Person is classified as eligible for best start tax credit'
    reference = "http://legislation.govt.nz/bill/government/2017/0004/15.0/DLM7512349.html"

    def formula(persons, period, parameters):
        is_primary_care_giver = persons.has_role(Family.PRINCIPAL_CAREGIVER)
        family_is_eligible = persons.family("income_tax__family_has_children_eligible_for_best_start", period)
        return family_is_eligible * is_primary_care_giver


class income_tax__entitlement_for_best_start_tax_credit(Variable):
    value_type = float
    entity = Family
    definition_period = MONTH
    label = u'Value of a Families entitlement for best start tax credit'
    reference = "http://legislation.govt.nz/bill/government/2017/0004/15.0/DLM7512349.html"

    def formula(family, period, parameters):

        # sum up families income
        family_income = family.sum(family.members('income_tax__income', period.this_year))

        # calculate income over the threshold
        income_over_threshold = where((family_income - 79000) < 0, 0, family_income - 79000)

        # work out the ages for each family member
        ages = family.members('age', period)

        # work out if each dependant child is eligible for full best start tax credit
        dependant_eligible_full = ages == 0

        # work out if each dependant child is eligible for abated best start tax credit
        dependant_eligible_abated_1 = ages == 1
        dependant_eligible_abated_2 = ages == 2

        # sum up the entitlement for each child
        bstc_entitlement = family.sum(dependant_eligible_full * 3120 + dependant_eligible_abated_1 * (3120 - (income_over_threshold * .21)) + dependant_eligible_abated_2 * (3120 - (income_over_threshold * .21)))

        return bstc_entitlement
        # TODO - Replace hardcoded values with parameters already created.
