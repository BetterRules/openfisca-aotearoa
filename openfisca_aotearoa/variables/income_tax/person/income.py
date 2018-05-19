# Import from openfisca-core the common python objects used to code the legislation in OpenFisca
from openfisca_core.model_api import *
# Import the entities specifically defined for this tax and benefit system
from openfisca_aotearoa.entities import *


class TaxPayerFilingStatus(Enum):
    __order__ = "non_filing filing filing_with_schedular_income"
    non_filing = u'Non-filing taxpayer'
    filing = u'Filing taxpayer'
    filing_with_schedular_income = u'Filing taxpayer with schedular income'
    reference = "http://www.legislation.govt.nz/act/public/2007/0097/latest/DLM1512331.html"


class tax_payer_filing_status(Variable):
    value_type = Enum
    possible_values = TaxPayerFilingStatus
    default_value = TaxPayerFilingStatus.non_filing
    entity = Person
    definition_period = YEAR
    label = u""
    reference = "http://www.legislation.govt.nz/act/public/2007/0097/latest/DLM1512331.html"


class annual_gross_income(Variable):
    value_type = float
    entity = Person
    definition_period = YEAR
    label = "Annual gross income"
    reference = "http://www.legislation.govt.nz/act/public/2007/0097/latest/DLM1512333.html"


class annual_total_deduction(Variable):
    value_type = float
    entity = Person
    definition_period = YEAR
    label = "Annual total deduction"
    reference = "http://www.legislation.govt.nz/act/public/2007/0097/latest/DLM1512336.html"


class net_income(Variable):
    value_type = float
    entity = Person
    definition_period = YEAR
    label = "Net income"
    reference = "http://www.legislation.govt.nz/act/public/2007/0097/latest/DLM1512339.html"

    def formula(person, period, parameters):
        net_income_calc = person('annual_gross_income', period) - person('annual_total_deduction', period)

        return (
            net_income_calc * (net_income_calc > 0)
            )


class net_loss(Variable):
    value_type = float
    entity = Person
    definition_period = YEAR
    label = "Net loss"
    reference = "http://www.legislation.govt.nz/act/public/2007/0097/latest/DLM1512339.html"

    def formula(person, period, parameters):
        net_income_calc = person('annual_gross_income', period) - person('annual_total_deduction', period)

        return (
            net_income_calc * (net_income_calc < 0)
            )


class available_tax_loss(Variable):
    value_type = float
    entity = Person
    definition_period = YEAR
    label = "Available tax loss"
    reference = "http://www.legislation.govt.nz/act/public/2007/0097/latest/DLM1520575.html#DLM1520774"


class taxable_income(Variable):
    value_type = float
    entity = Person
    definition_period = YEAR
    label = "Net loss"
    reference = "http://www.legislation.govt.nz/act/public/2007/0097/latest/DLM1512344.html"

    def formula(person, period, parameters):
        return (person('net_income', period) - person('available_tax_loss', period))
