# -*- coding: utf-8 -*-

# Import from openfisca-core the common python objects used to code the legislation in OpenFisca
from openfisca_core.model_api import *
# Import the entities specifically defined for this tax and benefit system
from openfisca_aotearoa.entities import Person
from numpy import clip

# All variables are according to the reference link http://www.legislation.govt.nz/act/public/2006/0040/latest/DLM379487.html#DLM379487


class kiwisaver__duration(Variable):
    value_type = int
    entity = Person
    definition_period = MONTH
    label = u"Years the prospective home buyer has been a member of a kiwisaver account"


class kiwisaver__contrib_duration(Variable):
    value_type = int
    entity = Person
    definition_period = MONTH
    label = u"Years the prospective home buyer has been contributing continuously to their kiwisaver account"


class kiwiserver__meets_contrib_duration_requirement(Variable):
    value_type = bool
    entity = Person
    definition_period = MONTH
    label = u"This flag returns true or false if the contribution period is valid"

    def formula(persons, period):
        return persons('kiwisaver__contrib_duration', period) >= 3


class kiwisaver__homestart_grant(Variable):
    value_type = float
    entity = Person
    definition_period = MONTH
    label = u"Amount available to you from the Homestart grant"

    def formula(persons, period):
        HS_grant = persons('kiwisaver__duration', period) * \
            persons('kiwisaver__contrib_duration', period) * 1000
        return clip(HS_grant, 0, 5000)


class kiwisaver__purchase_price(Variable):
    value_type = int
    entity = Person
    definition_period = YEAR
    label = u"Purchase price of the proposed home"


class kiwisaver__lvr_deposit_req(Variable):
    value_type = float
    entity = Person
    definition_period = MONTH
    label = u"Loan to value ratio deposit requirement"

    def formula(persons, period):
        return persons('kiwisaver__purchase_price', period) * 0.2


class homestart_deposit_req__kiwisaver(Variable):
    value_type = float
    entity = Person
    definition_period = MONTH
    label = u"Homestart grant deposit requirement"

    def formula(persons, period):
        return persons('kiwisaver__purchase_price', period) * 0.1


class kiwisaver__total_savings(Variable):
    value_type = float
    entity = Person
    definition_period = MONTH
    label = u"Homestart grant deposit requirement"

    def formula(persons, period):
        return persons('kiwisaver__savings', period) + persons('kiwisaver__homestart_grant', period) + persons('kiwisaver__net', period)


class kiwisaver__gross(Variable):
    value_type = float
    entity = Person
    definition_period = MONTH
    label = u"Gross kiwi saver balance"


class kiwisaver__net(Variable):
    value_type = float
    entity = Person
    definition_period = MONTH
    label = u"Gross kiwi saver balance"

    def formula(persons, period):
        return persons('kiwisaver__gross', period) - 1000


# The savings variable is for the purposes of calculating how much deposit, it's not part of the kiwisaver legislation
class kiwisaver__savings(Variable):
    value_type = float
    entity = Person
    definition_period = MONTH
    label = u"Personal cash savings in bank"


class kiwisaver__homestart_deposit_eligible(Variable):
    value_type = float
    entity = Person
    definition_period = MONTH
    label = u"Deposit amount needed to be eligble for homestart grant"

    def formula(persons, period):
        return persons('kiwisaver__total_savings', period) >= persons('homestart_deposit_req__kiwisaver', period)


class kiwisaver__lvr_deposit_eligible(Variable):
    value_type = float
    entity = Person
    definition_period = MONTH
    label = u"Deposit amount needed to be eligble for homestart grant"

    def formula(persons, period):
        return persons('kiwisaver__total_savings', period) >= persons('kiwisaver__lvr_deposit_req', period)


class kiwisaver__individual_income_per_homestart_grant(Variable):
    value_type = int
    entity = Person
    definition_period = YEAR
    set_input = set_input_divide_by_period
    # Check how to set input by user and check against the threshold


class kiwisaver__combined_income_per_hs_grant(Variable):
    value_type = int
    entity = Person
    definition_period = YEAR
    # Allows user to declare a salary for a year.
    set_input = set_input_divide_by_period
    # Check how to set input by user and check against the threshold
    label = "Combined income"
