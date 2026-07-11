"""TODO: Add missing doctring."""

# Import from openfisca-core the common python objects used to code the legislation in OpenFisca
from openfisca_core.holders import set_input_dispatch_by_period
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.variables import Variable

# Import the entities specifically defined for this tax and benefit system
from openfisca_aotearoa.entities import Person


class income_tax__residence(Variable):
    value_type = bool
    entity = Person
    definition_period = MONTH
    set_input = set_input_dispatch_by_period
    default_value = True
    label = "Boolean for if a Person is classified as meeting residence requirements"
    reference = "http://www.legislation.govt.nz/act/public/2007/0097/latest/DLM1518482.html"


class income_tax__annual_gross_income(Variable):
    value_type = float
    entity = Person
    definition_period = YEAR
    label = "Annual gross income"
    reference = "http://www.legislation.govt.nz/act/public/2007/0097/latest/DLM1512333.html"


class income_tax__annual_total_deduction(Variable):
    value_type = float
    entity = Person
    definition_period = YEAR
    label = "Annual total deduction"
    reference = "http://www.legislation.govt.nz/act/public/2007/0097/latest/DLM1512336.html"


class income_tax__net_income(Variable):
    value_type = float
    entity = Person
    definition_period = YEAR
    label = "Net income"
    reference = "http://www.legislation.govt.nz/act/public/2007/0097/latest/DLM1512339.html"

    def formula(person, period, parameters):
        net_income = person("income_tax__annual_gross_income", period) - person("income_tax__annual_total_deduction", period)

        return (
            net_income * (net_income > 0)
            )


class income_tax__net_loss(Variable):
    value_type = float
    entity = Person
    definition_period = YEAR
    label = "Net loss"
    reference = "http://www.legislation.govt.nz/act/public/2007/0097/latest/DLM1512339.html"

    def formula(person, period, parameters):
        net_loss = person("income_tax__annual_gross_income", period) - person("income_tax__annual_total_deduction", period)

        return (
            net_loss * (net_loss < 0)
            )


class income_tax__available_tax_loss(Variable):
    value_type = float
    entity = Person
    definition_period = YEAR
    label = "Available tax loss"
    reference = "http://www.legislation.govt.nz/act/public/2007/0097/latest/DLM1520575.html#DLM1520774"


class income_tax__taxable_income(Variable):
    value_type = float
    entity = Person
    definition_period = YEAR
    label = "A person's taxable income for a tax year"
    reference = "http://www.legislation.govt.nz/act/public/2007/0097/latest/DLM1512344.html"

    def formula(person, period, parameters):
        taxable_income = (person("income_tax__net_income", period) - person("income_tax__available_tax_loss", period))

        return (
            taxable_income * (taxable_income > 0)
            )


def _nz_tax_year_april_instant(period):
    """NZ tax / levy years generally commence 1 April.

    OpenFisca YEAR periods start on 1 January. For annual assessments that use
    rates in force for the April–March tax year, look up parameters as at
    1 April of the same calendar year as ``period.start``.

    Example: period ``2026`` (calendar) → parameter instant ``2026-04-01``.
    """
    return period.start.offset(3, "month")


class income_tax__schedule_1_tax_before_credits(Variable):
    value_type = float
    entity = Person
    definition_period = YEAR
    unit = "NZD"
    label = (
        "Schedule 1 individual income tax on taxable income before credits "
        "(progressive marginal scale; excludes ACC earners' levy and tax credits)"
        )
    reference = [
        "https://www.legislation.govt.nz/act/public/2007/0097/latest/DLM1523138.html",
        "https://www.ird.govt.nz/income-tax/income-tax-for-individuals/tax-codes-and-tax-rates-for-individuals/tax-rates-for-individuals",
        ]

    def formula(person, period, parameters):
        taxable_income = person("income_tax__taxable_income", period)
        # Non-positive taxable income yields zero tax (scale also returns 0 for negatives).
        scale = parameters(_nz_tax_year_april_instant(period)).taxes.income_tax.individual_income_tax_rate
        return scale.calc(taxable_income)


class income_tax__income_tax_before_credits(Variable):
    """Alias aligned with comparative / RuleSpec naming."""

    value_type = float
    entity = Person
    definition_period = YEAR
    unit = "NZD"
    label = "Individual income tax before credits (alias of income_tax__schedule_1_tax_before_credits)"
    reference = [
        "https://www.legislation.govt.nz/act/public/2007/0097/latest/DLM1523138.html",
        "https://www.ird.govt.nz/income-tax/income-tax-for-individuals/tax-codes-and-tax-rates-for-individuals/tax-rates-for-individuals",
        ]

    def formula(person, period, parameters):
        return person("income_tax__schedule_1_tax_before_credits", period)
