# -*- coding: utf-8 -*-

# Import from openfisca-core the common python objects used to code the legislation in OpenFisca
from openfisca_core.model_api import *
# Import the entities specifically defined for this tax and benefit system
from openfisca_aotearoa.entities import Person
from numpy import round

class weekly_compensation_before_tax(Variable):
    """
    Calculate the weekly compensation based on employee earnings over the last 52 weeks
    and self-employed earnings in most recent tax year.
    This relies on the user totalling the earnings over the last 52 weeks and the earnings period in weeks.
    Ideally a user would be able to enter the earnings per week (over a period) and the totals would then
    be calculated.
    """
    value_type = float
    entity = Person
    definition_period = YEAR # TODO - determine whether we need to get WEEK to work
    label = u"The amount payable as compensation per week before tax"
    # note that this also implements http://www.legislation.govt.nz/act/public/2016/0096/latest/whole.html?search=ts_act%40bill%40regulation%40deemedreg_live+organ_resel_25_a#DLM6965116
    reference = "http://www.legislation.govt.nz/act/public/2016/0096/latest/whole.html?search=ts_act%40bill%40regulation%40deemedreg_live+organ_resel_25_a#DLM6965123"

    def formula(persons, period, parameters):
        earnings_amount = persons('sum_of_earnings_in_last_52_weeks', period) 
        compensation_amount = persons('sum_of_earnings_during_compensation_period_in_last_52_weeks', period)
        earnings_excluding_compensation_amount = earnings_amount - compensation_amount

        earnings_period = persons('earnings_period_in_weeks', period)
        compensation_period = persons('compensation_period_in_weeks', period)
        earnings_excluding_compensation_period = earnings_period - compensation_period

        self_employed_earnings_in_most_recent_tax_year = persons('sum_of_self_employed_earnings_in_most_recently_completed_tax_year', period)
        most_recent_tax_year_period = persons('number_of_weeks_in_most_recently_completed_tax_year', period)

        employee_weekly_earnings = earnings_excluding_compensation_amount / earnings_excluding_compensation_period
        self_employed_weekly_earnings = self_employed_earnings_in_most_recent_tax_year / most_recent_tax_year_period
        
        return round(employee_weekly_earnings + self_employed_weekly_earnings, 2)

class kiwisaver_employee_deduction(Variable):
    value_type = float
    entity = Person
    definition_period = YEAR # TODO - determine whether we need to get WEEK to work
    label = u"The amount deducted as a kiwisaver contribution"
    # Salary or wages includes a payment of earnings compensation under the Compensation for Live Organ Donors Act 2016;
    # Ref: http://www.legislation.govt.nz/act/public/2007/0097/latest/DLM1519947.html?search=ts_act%40bill%40regulation%40deemedreg_live+organ_resel_25_a#DLM1519947
    # KiwiSaver deductions:
    reference = "http://www.legislation.govt.nz/act/public/2006/0040/latest/whole.html?search=ts_act%40bill%40regulation%40deemedreg_live+organ_resel_25_a#DLM379040"

    def formula(persons, period, parameters):
        earnings_amount = persons('sum_of_earnings_in_last_52_weeks', period) 
        compensation_amount = persons('sum_of_earnings_during_compensation_period_in_last_52_weeks', period)
        earnings_excluding_compensation_amount = earnings_amount - compensation_amount

        earnings_period = persons('earnings_period_in_weeks', period)
        compensation_period = persons('compensation_period_in_weeks', period)
        earnings_excluding_compensation_period = earnings_period - compensation_period

        self_employed_earnings_in_most_recent_tax_year = persons('sum_of_self_employed_earnings_in_most_recently_completed_tax_year', period)
        most_recent_tax_year_period = persons('number_of_weeks_in_most_recently_completed_tax_year', period)

        employee_weekly_earnings = earnings_excluding_compensation_amount / earnings_excluding_compensation_period
        self_employed_weekly_earnings = self_employed_earnings_in_most_recent_tax_year / most_recent_tax_year_period
        
        weekly_compensation = round(employee_weekly_earnings + self_employed_weekly_earnings, 2)

        kiwisaver_employee_deduction_percentage = persons('kiwisaver_employee_deduction_percentage', period)
        return round(weekly_compensation * kiwisaver_employee_deduction_percentage / 100, 2)

class kiwisaver_member(Variable):
    value_type = bool
    default_value = True
    entity = Person
    label = u"Whether the person currently pays into Kiwisaver"
    definition_period = YEAR

class sum_of_earnings_in_last_52_weeks(Variable):
    value_type = float
    entity = Person
    label = u"Total earnings over last 52 weeks"
    reference = "http://organiccoders.allengeer.com/brk-1234-abcdfcrg234356/"
    definition_period = YEAR

class earnings_period_in_weeks(Variable):
    value_type = int
    default_value = 52
    entity = Person
    label = u"The number of weeks over which earnings have been earned"
    reference = "http://organiccoders.allengeer.com/definitions-number-of-weeks/"
    definition_period = YEAR

class sum_of_earnings_during_compensation_period_in_last_52_weeks(Variable):
    value_type = float
    entity = Person
    label = u"Earnings during the period in which the donor was entitled to weekly compensation (as defined in section 6(1) of the Accident Compensation Act 2001)"
    definition_period = YEAR

class compensation_period_in_weeks(Variable):
    value_type = int
    entity = Person
    label = u"The number of weeks in which the donor was entitled to weekly compensation (as defined in section 6(1) of the Accident Compensation Act 2001) over the last 52 weeks"
    definition_period = YEAR

class sum_of_self_employed_earnings_in_most_recently_completed_tax_year(Variable):
    value_type = float
    default_value = 0
    entity = Person
    label = u"Self-employed earnings during the period in which the donor was entitled to weekly compensation (as defined in section 6(1) of the Accident Compensation Act 2001)"
    definition_period = YEAR

class number_of_weeks_in_most_recently_completed_tax_year(Variable):
    value_type = int
    default_value = 52
    entity = Person
    label = u"The number of weeks in the most recently completed tax year"
    definition_period = YEAR

class kiwisaver_employee_deduction_percentage(Variable):
    value_type = int
    default_value = 0
    entity = Person
    label = u"Kiwisaver employee deduction percentage "
    definition_period = YEAR
