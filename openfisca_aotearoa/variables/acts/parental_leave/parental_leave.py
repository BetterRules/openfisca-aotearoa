
# -*- coding: utf-8 -*-

from openfisca_core.model_api import *
from openfisca_aotearoa.entities import Person


class parental_leave__is_primary_carer(Variable):
    value_type = bool
    entity = Person
    definition_period = MONTH
    label = u"Is primary carer"
    reference = "http://www.legislation.govt.nz/act/public/1987/0129/latest/DLM120458.html"


class parental_leave__applied_for_leave_or_stopped_working(Variable):
    value_type = bool
    entity = Person
    definition_period = MONTH
    label = u"Has applied for/taken leave or stopped working immediately"
    reference = "http://www.legislation.govt.nz/act/public/1987/0129/latest/DLM121773.html"


class parental_leave__threshold_tests(Variable):
    value_type = int
    entity = Person
    definition_period = MONTH
    label = u"satisfies Parental Leave Threshold Tests (tests are used to determine an employee's entitlements to parental leave)"
    reference = u"http://www.legislation.govt.nz/act/public/1987/0129/latest/DLM6810651.html"


class parental_leave__had_previous_parental_leave_in_last_six_months(Variable):
    value_type = bool
    entity = Person
    definition_period = MONTH
    label = u"Had previous parental leave in last six months"
    reference = u"http://www.legislation.govt.nz/act/public/1987/0129/latest/DLM120450.html"


class parental_leave__eligible_employee(Variable):
    value_type = bool
    entity = Person
    definition_period = MONTH
    label = u"Eligible employee"
    reference = u"http://www.legislation.govt.nz/act/public/1987/0129/latest/DLM121539.html"

    def formula(persons, period, parameters):
        is_citizen = persons('is_nz_citizen', period)

        return is_citizen * persons('parental_leave__is_primary_carer', period) * \
            persons('parental_leave__applied_for_leave_or_stopped_working', period) * \
            (persons('parental_leave__threshold_tests', period) >= 6) * \
            not_(persons('parental_leave__had_previous_parental_leave_in_last_six_months', period))
