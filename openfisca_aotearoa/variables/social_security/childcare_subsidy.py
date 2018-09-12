
# -*- coding: utf-8 -*-

from openfisca_core.model_api import *
from openfisca_aotearoa.entities import Person


class childcare_subsidy__is_a_dependant_child(Variable):
    value_type = bool
    entity = Person
    definition_period = MONTH
    label = u"Is a dependant child"
    reference = "http://www.legislation.govt.nz/regulation/public/2004/0268/latest/DLM282545.html"


class childcare_subsidy__child_is_no_older_than_5_years_28_days(Variable):
    value_type = bool
    entity = Person
    definition_period = MONTH
    label = u"Child is no older than 5 years 28_days"
    reference = "http://www.legislation.govt.nz/regulation/public/2004/0268/latest/DLM282545.html"


class childcare_subsidy__is_child_attending_school(Variable):
    value_type = bool
    entity = Person
    definition_period = MONTH
    label = u"Is child attending school"
    reference = "http://www.legislation.govt.nz/regulation/public/2004/0268/latest/DLM282545.html"


class childcare_subsidy__child_will_be_enrolled_to_school_with_cohort_policy(Variable):
    value_type = bool
    entity = Person
    definition_period = MONTH
    label = u"Child will be enrolled in a school that has a cohort entry policy in place"
    reference = """ http://www.legislation.govt.nz/regulation/public/2004/0268/latest/DLM282545.html

      (ba) who is 5, whose parent, principal caregiver, or guardian intends to enrol the child in a school that has a cohort entry policy in place, and who (under section 5B(2) of the Education Act 1989) may not be enrolled in that school until the term start date of the next term;"""


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

        return is_citizen * persons('childcare_subsidy__is_a_dependant_child', period) * \
            persons('childcare_subsidy__child_is_no_older_than_5_years_28_days', period) * \
            not_(persons('childcare_subsidy__is_child_attending_school', period)) + \
            persons('childcare_subsidy__child_will_be_enrolled_to_school_with_cohort_policy', period) + \
            persons('childcare_subsidy__child_has_disability_allowance', period)
