
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


class parental_leave__passes_12_month_employment_test(Variable):
    value_type = bool
    entity = Person
    definition_period = MONTH
    label = u"Number of Persons classified as dependant for the purposes of rates rebates"
    reference = """
    http://www.legislation.govt.nz/act/public/1987/0129/latest/link.aspx

    In this Act, the following tests are used to determine an employee’s entitlements to parental leave:
    an employee meets the 12-month employment test if the employee will have been employed by the same employer for at least an average of 10 hours a week in the 12 months immediately preceding the expected date of—
    (i) delivery of the child (in the case of a child to be born to the employee or to the employee’s spouse or partner); or
    (ii) assumption of responsibility for the care of the child (in any other case).
    """


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

        return (is_citizen * persons('parental_leave__is_primary_carer', period) * \
            persons('parental_leave__applied_for_leave_or_stopped_working', period) * \
            persons('parental_leave__passes_12_month_employment_test', period) * \
            not_(persons('parental_leave__had_previous_parental_leave_in_last_six_months', period)))
