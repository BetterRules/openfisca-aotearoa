# -*- coding: utf-8 -*-

from openfisca_core.model_api import *
from openfisca_aotearoa.entities import Person


class family_scheme__qualifies_for_family_tax_credit(Variable):
    value_type = bool
    entity = Person
    definition_period = MONTH
    label = u'Is a person qualified as eligible for the family tax credit'
    reference = "http://www.legislation.govt.nz/act/public/2007/0097/latest/DLM1518515.html#DLM1518515"

    def formula(persons, period, parameters):
        return persons("family_scheme__base_qualifies", period) *\
            persons("family_scheme__family_tax_credit_income_under_threshold", period)


class family_scheme__family_tax_credit_income_under_threshold(Variable):  # this variable is a proxy for the calculation "family_scheme__family_tax_credit_entitlement" which needs to be coded
    value_type = bool
    entity = Person
    definition_period = MONTH
    label = u'Is the person income under the threshold for the family tax credit'
    reference = "http://www.legislation.govt.nz/act/public/2007/0097/latest/DLM1518484.html"


class family_scheme__family_tax_credit_entitlement(Variable):
    value_type = float
    entity = Person
    definition_period = MONTH
    label = u'The family tax credit person is entitlement to under the family scheme'
    reference = "http://www.legislation.govt.nz/act/public/2007/0097/latest/DLM1518514.html"

    def formula(persons, period, parameters):
        # eldest_child_credit = parameters(period).entitlements.income_tax.family_scheme.family_tax_credit.eldest_child
        # subsequent_child_credit = parameters(period).entitlements.income_tax.family_scheme.family_tax_credit.subsequent_child
        # threshold = parameters(period).entitlements.income_tax.family_scheme.family_tax_credit.full_year_abatement_threshold
        # rate = parameters(period).entitlements.income_tax.family_scheme.family_tax_credit.full_year_abatement_rate

        # sum up families income
        # http://legislation.govt.nz/act/public/2007/0097/latest/DLM1518488.html#DLM1518488
        # family_income = persons.family.sum(persons.family.members("family_scheme__assessable_income", period.this_year))

        # calculate income over the threshold
        # income_over_threshold = where((family_income - threshold) < 0, 0, family_income - threshold)

        # calculate the number of children
        number_of_children = persons.family.sum(
            persons("income_tax__dependent_child", period))

        # TODO this variable is incomplete and requires the formula to be finished
        return number_of_children
