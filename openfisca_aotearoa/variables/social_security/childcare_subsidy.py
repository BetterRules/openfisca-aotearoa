
# -*- coding: utf-8 -*-

from openfisca_core.model_api import *
from openfisca_aotearoa.entities import Person


class childcare_subsidy__is_a_dependant_child(Variable):
    value_type = bool
    entity = Person
    definition_period = MONTH
    label = u"Is a dependant child"
    reference = "http://www.legislation.govt.nz/regulation/public/2004/0268/latest/DLM282545.html"


class childcare_subsidy__childs_age(Variable):
    value_type = int
    entity = Person
    definition_period = MONTH
    label = u"Child's age"
    reference = "http://www.legislation.govt.nz/regulation/public/2004/0268/latest/DLM282545.html"


class childcare_subsidy__is_child_attending_school(Variable):
    value_type = bool
    entity = Person
    definition_period = MONTH
    label = u"Is child attending school"
    reference = "http://www.legislation.govt.nz/regulation/public/2004/0268/latest/DLM282545.html"


class childcare_subsidy__child_has_disability_allowance(Variable):
    value_type = bool
    entity = Person
    definition_period = MONTH
    label = u"Child has disability allowance"
    reference = u"http://www.legislation.govt.nz/regulation/public/2004/0268/latest/DLM282545.html"


class childcare_subsidy__eligibility(Variable):
    value_type = bool
    entity = Person
    definition_period = MONTH
    label = u"Eligibility of child for payment of childcare subsidy"
    reference = u"http://www.legislation.govt.nz/regulation/public/2004/0268/latest/DLM282545.html"

    def formula(persons, period, parameters):
        is_citizen = persons('is_nz_citizen', period)

        return is_citizen * persons('childcare_subsidy__is_primary_carer', period) * \
            persons('childcare_subsidy__is_child_attending_school', period) * \
            (persons('childcare_subsidy__childs_age', period) <= 5) + \
            persons('childcare_subsidy__child_has_disability_allowance', period) * \
