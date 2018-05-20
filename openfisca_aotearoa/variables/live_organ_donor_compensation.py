# -*- coding: utf-8 -*-

# Import from openfisca-core the common python objects used to code the legislation in OpenFisca
from openfisca_core.model_api import *
# Import the entities specifically defined for this tax and benefit system
from openfisca_aotearoa.entities import Person
from numpy import round

class weekly_compensation_before_tax(Variable):
    value_type = float
    entity = Person
    definition_period = YEAR # TODO - determine whether we need to get WEEK to work
    label = u"The amount payable as compensation per week before tax"

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

# class PayFrequency(Enum):
#     weekly = u'Weekly'
#     fortnightly = u'Fortnightly'
#     four_weekly = u'Four Weekly'
#     monthly = u'Monthly'

# class pay_frequency(Variable):
#     value_type = Enum
#     possible_values = PayFrequency
#     default_value = PayFrequency.weekly  # The default is mandatory
#     entity = Person
#     definition_period = YEAR
#     label = u"The frequency at which a person is paid"

# class salary_per_pay(Variable):
#     value_type = float
#     entity = Person
#     definition_period = YEAR # TODO - determine whether we need to get WEEK to work
#     label = u"The salary earned by a person before tax"

class kiwisaver_member(Variable):
    value_type = bool
    default_value = True
    entity = Person
    label = u"Whether the person currently pays into Kiwisaver"
    reference = "http://organiccoders.allengeer.com/definitions-number-of-weeks/"
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
