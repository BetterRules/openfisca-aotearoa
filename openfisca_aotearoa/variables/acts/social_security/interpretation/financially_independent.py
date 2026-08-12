"""TODO: Add missing doctring."""

from openfisca_core import holders, periods, variables

from openfisca_aotearoa import entities


# TODO: Review against the new 2018 act
class social_security__financially_independent(variables.Variable):
    value_type = bool
    entity = entities.Person
    label = """financially independent, in relation to a person, means—
        (a) in full employment; or
        (b) in receipt of a basic grant or an independent circumstances grant under the Student Allowances Regulations 1998 (SR 1998/277); or
        (c) in receipt of payments under a Government-assisted scheme which the chief executive considers analogous to a main benefit under this Act; or
        (d) in receipt of a main benefit under this Act
        """

    definition_period = periods.WEEK
    reference = """Interpretation section of Social Security Act 1964"""
    set_input = holders.set_input_dispatch_by_period

    def formula(persons, period, parameters):
        in_full_employment = persons("social_security__full_employment", period)
        receives_grant = persons("social_security__in_receipt_of_basic_grant", period.first_month)
        receives_gov_assisted_payments = persons("social_security__receives_government_assisted_scheme_payments", period.first_month)
        receives_benefit = persons("social_security__receives_main_benefit", period.first_month)

        return in_full_employment + receives_grant + receives_gov_assisted_payments + receives_benefit


# TODO: Review against the new 2018 act
class social_security__receives_government_assisted_scheme_payments(variables.Variable):
    value_type = bool
    entity = entities.Person
    default_value = False
    definition_period = periods.MONTH
    label = "In receipt of payments under a Government-assisted scheme which the chief executive considers analogous to a main benefit under Social Security Act"


# TODO: Review against the new 2018 act
class social_security__in_receipt_of_basic_grant(variables.Variable):
    value_type = bool
    entity = entities.Person
    default_value = False
    definition_period = periods.MONTH
    label = "in receipt of a basic grant or an independent circumstances grant under the Student Allowances Regulations 1998 (SR 1998/277)"


# TODO: Review against the new 2018 act
class social_security__receives_main_benefit(variables.Variable):
    value_type = bool
    entity = entities.Person
    default_value = False
    definition_period = periods.MONTH
    label = "in receipt of a main benefit under Social Security Act"


# TODO: Review against the new 2018 act
class social_security__received_income_tested_benefit(variables.Variable):
    value_type = bool
    entity = entities.Person
    definition_period = periods.YEAR  # Questioning if there's a reason this is a year.
    label = "Boolean for if a Person is classified as receiving an income tested benefit"
    reference = "http://www.legislation.govt.nz/act/public/1964/0136/latest/DLM359124.html#DLM360353"
