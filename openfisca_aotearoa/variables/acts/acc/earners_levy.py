"""ACC earners' levy — standard employee calculation.

Rates and maximum earnings are taken from IRD's published earners' levy tables
(amounts include GST). This module models the standard flat-rate employee levy
with the annual earnings cap. Self-employed minimum-earnings rules and work
account levies are out of scope here.
"""

import numpy

from openfisca_core.periods import YEAR
from openfisca_core.variables import Variable

from openfisca_aotearoa.entities import Person
from openfisca_aotearoa.variables.acts.income_tax.individual import (
    _nz_tax_year_april_instant,
    )


class acc__earnings_for_earners_levy(Variable):
    value_type = float
    entity = Person
    definition_period = YEAR
    unit = "NZD"
    label = "Annual earnings liable for ACC earners' levy (input)"
    reference = "https://www.ird.govt.nz/income-tax/income-tax-for-individuals/acc-clients-and-carers/acc-earners-levy-rates"


class acc__earners_levy_including_gst(Variable):
    value_type = float
    entity = Person
    definition_period = YEAR
    unit = "NZD"
    label = (
        "Standard ACC earners' levy including GST "
        "(rate × min(earnings, maximum earnings); zero if earnings ≤ 0)"
        )
    reference = [
        "https://www.ird.govt.nz/income-tax/income-tax-for-individuals/acc-clients-and-carers/acc-earners-levy-rates",
        ]

    def formula(persons, period, parameters):
        earnings = persons("acc__earnings_for_earners_levy", period)
        p = parameters(_nz_tax_year_april_instant(period)).acc.earners_levy
        rate = p.rate_including_gst
        maximum_earnings = p.maximum_earnings
        liable = numpy.minimum(numpy.maximum(earnings, 0.0), maximum_earnings)
        return liable * rate


class acc__earners_levy(Variable):
    """Alias for the standard including-GST levy amount."""

    value_type = float
    entity = Person
    definition_period = YEAR
    unit = "NZD"
    label = "Standard ACC earners' levy including GST (alias of acc__earners_levy_including_gst)"
    reference = "https://www.ird.govt.nz/income-tax/income-tax-for-individuals/acc-clients-and-carers/acc-earners-levy-rates"

    def formula(persons, period, parameters):
        return persons("acc__earners_levy_including_gst", period)
