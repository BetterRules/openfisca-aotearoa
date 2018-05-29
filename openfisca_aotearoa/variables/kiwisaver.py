# -*- coding: utf-8 -*-

# Import from openfisca-core the common python objects used to code the legislation in OpenFisca
from openfisca_core.model_api import *
# Import the entities specifically defined for this tax and benefit system
from openfisca_aotearoa.entities import Person
from numpy import clip

# All variables are according to the reference link http://www.legislation.govt.nz/act/public/2006/0040/latest/DLM379487.html#DLM379487


class ks_duration(Variable):
    value_type = int
    entity = Person
    definition_period = MONTH
    label = u"Years the prospective home buyer has been a member of a kiwisaver account"


class contrib_duration__kiwisaver(Variable):
    value_type = int
    entity = Person
    definition_period = MONTH
    label = u"Years the prospective home buyer has been contributing continuously to their kiwisaver account"


class meets_contrib_duration_requirement__kiwisaver(Variable):
    value_type = bool
    entity = Person
    definition_period = MONTH
    label = u"This flag returns true or false if the contribution period is valid"

    def formula(persons, period):
        return persons('contrib_duration__kiwisaver', period) >= 3


class homestart_grant__kiwisaver(Variable):
    value_type = float
    entity = Person
    definition_period = MONTH
    label = u"Amount available to you from the Homestart grant"

    def formula(persons, period):
        HS_grant = persons('ks_contrib_duration', period) * \
            persons('ks_contrib_duration_satisfied', period) * 1000
        return clip(HS_grant, 0, 5000)


class purc_price(Variable):
    value_type = int
    entity = Person
    definition_period = YEAR
    label = u"Purchase price of the proposed home"


class lvr_deposit_req__kiwisaver(Variable):
    value_type = float
    entity = Person
    definition_period = MONTH
    label = u"Loan to value ratio deposit requirement"

    def formula(persons, period):
        return persons('purc_price', period) * 0.2


class homestart_deposit_req__kiwisaver(Variable):
    value_type = float
    entity = Person
    definition_period = MONTH
    label = u"Homestart grant deposit requirement"

    def formula(persons, period):
        return persons('purc_price', period) * 0.1


class total_savings__kiwisaver(Variable):
    value_type = float
    entity = Person
    definition_period = MONTH
    label = u"Homestart grant deposit requirement"

    def formula(persons, period):
        return persons('savings__kiwisaver', period) + persons('homestart_grant__kiwisaver', period) + persons('net__kiwisaver', period)


class gross__kiwisaver(Variable):
    value_type = float
    entity = Person
    definition_period = MONTH
    label = u"Gross kiwi saver balance"


class net__kiwisaver(Variable):
    value_type = float
    entity = Person
    definition_period = MONTH
    label = u"Gross kiwi saver balance"

    def formula(persons, period):
        return persons('gross__kiwisaver', period) - 1000


# The savings variable is for the purposes of calculating how much deposit, it's not part of the kiwisaver legislation
class savings__kiwisaver(Variable):
    value_type = float
    entity = Person
    definition_period = MONTH
    label = u"Personal cash savings in bank"


class homestart_deposit_eligible(Variable):
    value_type = float
    entity = Person
    definition_period = MONTH
    label = u"Deposit amount needed to be eligble for homestart grant"

    def formula(persons, period):
        return persons('total_savings__kiwisaver', period) >= persons('homestart_deposit_req__kiwisaver', period)


class lvr_deposit_eligible(Variable):
    value_type = float
    entity = Person
    definition_period = MONTH
    label = u"Deposit amount needed to be eligble for homestart grant"

    def formula(persons, period):
        return persons('total_savings__kiwisaver', period) >= persons('lvr_deposit_req__kiwisaver', period)


class indv_income_per_hs_grant(Variable):
    value_type = int
    entity = Person
    definition_period = YEAR
    set_input = set_input_divide_by_period
    # Check how to set input by user and check against the threshold


class combined_income_per_hs_grant(Variable):
    value_type = int
    entity = Person
    definition_period = YEAR
    # Allows user to declare a salary for a year.
    set_input = set_input_divide_by_period
    # Check how to set input by user and check against the threshold
    label = "Combined income"
