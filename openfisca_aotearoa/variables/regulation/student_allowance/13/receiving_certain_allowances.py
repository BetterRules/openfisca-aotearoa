
# -*- coding: utf-8 -*-

from openfisca_core.model_api import *
from openfisca_aotearoa.entities import Person


class student_allowance__partner_or_person_receiving_certain_allowances(Variable):
    value_type = bool
    entity = Person
    definition_period = MONTH
    reference = "http://www.legislation.govt.nz/regulation/public/1998/0277/latest/DLM260340.html"
    label = "Student not eligible for certain allowances where student or spouse or partner receiving social security payments, New Zealand superannuation, or veteran’s pension"

# not using social_security__received_income_tested_benefit here because
# a) student allowances eligibility also apply to spouse
# b) the "orphan's benefit" and "unsupported child’s benefit" appear to be excluded
