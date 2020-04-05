from openfisca_core.model_api import *
from openfisca_aotearoa.entities import Person, Business

class registered_in_NZ(Variable):
    value_type = bool
    entity = Business
    definition_period = MONTH
    label = u"Is the business registered with the New Zealand Companies Office?"
    reference = "https://workandincome.govt.nz/products/a-z-benefits/covid-19-support.html"


class located_in_NZ(Variable):
    value_type = bool
    entity = Business
    definition_period = MONTH
    label = u"Is the business physically located and operates in NZ?"
    reference = "https://workandincome.govt.nz/products/a-z-benefits/covid-19-support.html"


class sole_trader_operates_business(Variable):
    value_type = bool
    entity = Business
    definition_period = MONTH
    label = u"Is the person a sole trader?"
    reference = "https://workandincome.govt.nz/products/a-z-benefits/covid-19-support.html"


class sole_trader_has_IRD_number(Variable):
    value_type = bool
    entity = Business
    definition_period = MONTH
    label = u"Does the person have a personal IRD number used for paying income tax and GST?"
    reference = "https://workandincome.govt.nz/products/a-z-benefits/covid-19-support.html"


class sole_trader_has_applicable_licenses(Variable):
    value_type = bool
    entity = Business
    definition_period = MONTH
    label = u"Does the sole trader have applicable licenses and permits for their business needs?"
    reference = "https://workandincome.govt.nz/products/a-z-benefits/covid-19-support.html"


class qualifications_or_registration_for_trade(Variable):
    value_type = bool
    entity = Business
    definition_period = MONTH
    label = u"Does the sole trader have qualifications or registrations for their trade or profession?"
    reference = "https://workandincome.govt.nz/products/a-z-benefits/covid-19-support.html"


class employees_legally_work_in_NZ(Variable):
    value_type = bool
    entity = Business
    definition_period = MONTH
    label = u"Are all the named employees legally entitled to work in NZ?"
    '''Legally working in New Zealand means a person is both working in New Zealand and is legally entitled to work in New Zealand. A person is legally entitled to work in New Zealand if they:
    are a New Zealand or Australian citizen (including a person born in the Cook Islands, Niue or Tokelau), or
    have a New Zealand residence class visa, or
    have a New Zealand work visa or a condition on their New Zealand temporary visa that allows them to work in New Zealand.'''
    reference = "https://workandincome.govt.nz/products/a-z-benefits/covid-19-support.html"


class decline_in_business_revenue_due_to_covid_19(Variable):
    value_type = bool
    entity = Business
    definition_period = MONTH
    label = u"Has the business observed in actual or predicted (due to reduction in bookings, etc) revenue by more than 30% due to COVID-19?"
    ''' The business must experience this decline between January 2020 and 9 June 2020.'''
    reference = "https://workandincome.govt.nz/products/a-z-benefits/covid-19-support.html"


class already_applied_for_wage_subsidy(Variable):
    value_type = bool
    entity = Business
    definition_period = MONTH
    label = u"Has the business already applied for a wage subsidy?"


class covid_19_wage_subsidy__eligibility(Variable):
    value_type = bool
    entity = Business
    definition_period = MONTH
    label = u"Conditions for checking eligibility for wage subsidy"
    reference = "https://workandincome.govt.nz/products/a-z-benefits/covid-19-support.html"

    def formula(business, period, parameters):
        conditions_for_sole_traders = business('sole_trader_has_IRD_number',
        period) * business('sole_trader_has_applicable_licenses', period) *
        business('qualifications_or_registration_for_trade', period)

        conditions_for_all_businesses = business('registered_in_NZ', period)
        * business('located_in_NZ', period)
        * business('employees_legally_work_in_NZ', period)
        * business('decline_in_business_revenue_due_to_covid_19', period)
        * not_(business('already_applied_for_wage_subsidy', period))

        return conditions_for_all_businesses *
        ((business('sole_trader_operates_business', period) *
        conditions_for_sole_traders) +
        (not_(business('sole_trader_operates_business', period))))
