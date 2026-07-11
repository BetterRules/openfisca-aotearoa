"""KiwiSaver contribution rate parameters — basic minimum employee/employer amounts.

This is a thin surface for comparative validation. It applies the published
minimum/default rates to a gross earnings input. Eligibility, contribution
holidays, ESCT, Crown contributions, and opted-up employee rates are out of
scope.
"""

import numpy

from openfisca_core.periods import YEAR
from openfisca_core.variables import Variable

from openfisca_aotearoa.entities import Person
from openfisca_aotearoa.variables.acts.income_tax.individual import (
    _nz_tax_year_april_instant,
    )


def max_(left, right):
    """Element-wise maximum compatible with OpenFisca vector formulas."""
    return numpy.maximum(left, right)


class kiwisaver__gross_salary_or_wages(Variable):
    value_type = float
    entity = Person
    definition_period = YEAR
    unit = "NZD"
    label = "Gross salary or wages used as the KiwiSaver contribution base (input)"
    reference = "https://www.ird.govt.nz/kiwisaver/kiwisaver-individuals/making-contributions/how-much-you-need-to-contribute"


class kiwisaver__employee_minimum_contribution(Variable):
    value_type = float
    entity = Person
    definition_period = YEAR
    unit = "NZD"
    label = "Employee KiwiSaver contribution at the minimum/default rate"
    reference = [
        "https://www.ird.govt.nz/kiwisaver-changes",
        "https://www.ird.govt.nz/kiwisaver/kiwisaver-individuals/kiwisaver-benefits",
        ]

    def formula(persons, period, parameters):
        earnings = persons("kiwisaver__gross_salary_or_wages", period)
        rate = parameters(
            _nz_tax_year_april_instant(period)
            ).kiwisaver.employee_minimum_contribution_rate
        # Contributions are never negative; clamp base like RuleSpec companion tests.
        return max_(earnings, 0) * rate


class kiwisaver__employer_minimum_contribution(Variable):
    value_type = float
    entity = Person
    definition_period = YEAR
    unit = "NZD"
    label = "Compulsory employer KiwiSaver contribution at the minimum rate"
    reference = [
        "https://www.ird.govt.nz/kiwisaver-changes",
        "https://www.ird.govt.nz/kiwisaver/kiwisaver-employers/contributions-and-deductions/employer-contributions-to-kiwisaver-and-complying-funds",
        ]

    def formula(persons, period, parameters):
        earnings = persons("kiwisaver__gross_salary_or_wages", period)
        rate = parameters(
            _nz_tax_year_april_instant(period)
            ).kiwisaver.employer_minimum_contribution_rate
        return max_(earnings, 0) * rate
