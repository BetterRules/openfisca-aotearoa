# -*- coding: utf-8 -*-

# Import from openfisca-core the common python objects used to code the legislation in OpenFisca
from openfisca_core.model_api import *
# Import the entities specifically defined for this tax and benefit system
from openfisca_aotearoa.entities import Person, Family
from numpy import datetime64


class best_start__eligibility(Variable):
    value_type = bool
    entity = Person
    definition_period = MONTH
    label = u'Is each person classified as eligible for best start tax credit'
    reference = "http://legislation.govt.nz/bill/government/2017/0004/15.0/DLM7512349.html"

    def formula(persons, period, parameters):
        qualifies = persons("family_scheme__qualifies_for_entitlements", period)
        family_is_eligible = persons.family("best_start__family_has_children_eligible", period)
        return qualifies * family_is_eligible


class best_start__family_has_children_eligible(Variable):
    value_type = bool
    entity = Family
    definition_period = MONTH
    label = u'Is each family classified as eligible for best start tax credit'
    reference = "http://legislation.govt.nz/bill/government/2017/0004/15.0/DLM7512349.html"

    def formula(families, period, parameters):
        families_have_children_born_after_launch_date = families.max(families.members("date_of_birth", period) >= datetime64('2018-07-01'))
        families_have_children_due_after_launch_date = families.max(families.members("due_date_of_birth", period) >= datetime64('2018-07-01'))
        families_have_children_younger_than_three_years = families("age_of_youngest", period) < 3
        return ((families_have_children_born_after_launch_date + families_have_children_due_after_launch_date) > 0) * \
            families_have_children_younger_than_three_years


class best_start__year_of_child(Variable):
    value_type = float
    entity = Person
    definition_period = MONTH
    label = u'Returns the year of eligibilty either 1, 2 or 3 otherwise returns zero'
    reference = "http://legislation.govt.nz/bill/government/2017/0004/15.0/DLM7512349.html"

    def formula(persons, period, parameters):
        birth = persons('date_of_birth', period)
        birth_year = birth.astype('datetime64[Y]').astype(int) + 1970
        birth_month = birth.astype('datetime64[M]').astype(int) % 12 + 1
        birth_day = (birth - birth.astype('datetime64[M]') + 1).astype(int)\


        adjust_month = birth_month + (birth_day > 1)  # adjusts month for first full month after birth
        is_birthday_month_past = (adjust_month <= period.start.month)
        is_current_or_previous_year = birth_year <= period.start.year
        whatyear = (period.start.year - birth_year) - where(is_birthday_month_past, 0, 1)

        whatyear = whatyear + 1
        whatyear = whatyear * \
            (whatyear < 4) * \
            is_current_or_previous_year * (((persons("date_of_birth", period) >=
                                             datetime64('2018-07-01')) + (persons("due_date_of_birth", period) >= datetime64('2018-07-01'))) > 0)

        return whatyear


class best_start__tax_credit_per_child(Variable):
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
        # http://legislation.govt.nz/act/public/2007/0097/latest/DLM1518488.html#DLM1518488
        family_income = persons.family.sum(persons.family.members("family_scheme__assessable_income", period.this_year))

        # calculate income over the threshold
        income_over_threshold = where((family_income - threshold) < 0, 0, family_income - threshold)

        # work out the ages for each family member
        years = persons('best_start__year_of_child', period)

        # work out if each dependant child is eligible for full best start tax credit
        dependant_eligible_full = (years == 1) * prescribed_amount

        # work out if each dependant child is eligible for abated best start tax credit
        dependant_eligible_abated_1 = (years == 2) * (prescribed_amount - (income_over_threshold * rate))

        dependant_eligible_abated_2 = (years == 3) * (prescribed_amount - (income_over_threshold * rate))

        # sum up the entitlement for each child
        return (dependant_eligible_full + dependant_eligible_abated_1 + dependant_eligible_abated_2) / 12


class best_start__entitlement(Variable):
    value_type = float
    entity = Person
    definition_period = MONTH
    label = u'The total value the principal carer is entitled to for the best start tax credit'
    reference = "http://legislation.govt.nz/bill/government/2017/0004/15.0/DLM7512349.html"

    def formula(persons, period, parameters):

        # sum up families income
        return persons.family.sum(
            persons.family.members("best_start__tax_credit_per_child", period)) * \
            persons("best_start__eligibility", period)
