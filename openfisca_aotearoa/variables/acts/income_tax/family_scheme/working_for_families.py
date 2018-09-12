# -*- coding: utf-8 -*-

from openfisca_core.model_api import *
from openfisca_aotearoa.entities import Person


class family_scheme__qualifies_for_working_for_families(Variable):
    value_type = bool
    entity = Person
    definition_period = MONTH
    label = u'Is a person is qualified as eligible for the working for families'
    reference = "http://www.legislation.govt.nz/act/public/2007/0097/latest/DLM1518484.html"

    def formula(persons, period, parameters):
        received_parents_allowance = persons('veterans_support__received_parents_allowance', period)
        received_childrens_pension = persons('veterans_support__received_childrens_pension', period)

        return persons("family_scheme__base_qualifies", period) * not_(received_parents_allowance) * not_(received_childrens_pension)


class family_scheme__working_for_families_entitlement(Variable):
    value_type = float
    entity = Person
    definition_period = MONTH
    label = u'The entitlement a person has under the family scheme'
    reference = "http://www.legislation.govt.nz/act/public/2007/0097/latest/DLM1518503.html"

    def formula(persons, period, parameters):
        family_tax_credit = persons('family_scheme__family_tax_credit_entitlement', period)
        in_work_tax_credit = persons('family_scheme__in_work_tax_credit_entitlement', period)
        child_tax_credit = persons('family_scheme__child_tax_credit_entitlement', period)
        parental_tax_credit_entitlement = persons('family_scheme__parental_tax_credit_entitlement', period)
        credit_abatement = 5 * -1  # TODO need to insert abatement calculation
        return family_tax_credit + (in_work_tax_credit or child_tax_credit) + parental_tax_credit_entitlement + credit_abatement
