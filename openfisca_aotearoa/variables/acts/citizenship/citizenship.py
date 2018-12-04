# -*- coding: utf-8 -*-

from openfisca_core.model_api import Variable
from openfisca_core.periods import DAY, ETERNITY
from openfisca_aotearoa.entities import Person


class citizenship__citizenship_by_grant_may_be_authorized(Variable):
    value_type = bool
    entity = Person
    definition_period = DAY
    reference = "http://www.legislation.govt.nz/act/public/1977/0061/latest/DLM443855.html"
    label = u"statisfies criteria such that the Minister may authorise the grant of New Zealand citizenship to this person"

    def formula_2005_04_20(persons, period, parameters):

        return (persons('age', period) >= parameters(period).citizenship.by_grant.minimum_age_threshold) * \
            persons('is_of_full_capacity', period) * \
            persons('citizenship__meets_minimum_presence_requirements', period) * \
            persons('citizenship__is_of_good_character', period) * \
            persons('citizenship__has_sufficient_knowledge_of_the_responsibilities_and_privileges_attaching_to_nz_citizenship', period) * \
            persons('citizenship__has_sufficient_knowledge_of_the_english_language', period) * \
            (persons('citizenship__intends_to_reside_in_nz', period) + persons('citizenship__intends_crown_service', period) + \
                persons('citizenship__intends_international_service', period) + persons('citizenship__intends_nz_employment', period))


class citizenship__meets_minimum_presence_requirements(Variable):
    value_type = bool
    entity = Person
    definition_period = DAY
    label = u"was present in New Zealand for a min of 1,350 days during the 5 years immediately preceding the date of application"
    reference = "http://www.legislation.govt.nz/act/public/1977/0061/latest/DLM443855.html"

    def formula(persons, period, parameters):
        # persons('immigration__entitled_to_stay_indefinitely', period) * \
        # (ii) for at least 240 days in each of those 5 years,—
        # being days during which the applicant was entitled in terms of the Immigration Act 2009 to be in New Zealand indefinitely
        # for p in [period.offset(offset) for offset in range(-365, 1)]:
        return persons('citizenship__meets_5_year_presence_requirement', period) * \
            persons('citizenship__meets_each_year_minimum_presence_requirements', period)


class citizenship__meets_each_year_minimum_presence_requirements(Variable):
    value_type = bool
    entity = Person
    definition_period = DAY
    label = u"was present in New Zealand for a minimum of 1350 days during the 5 years immediately preceding the date of the application"
    reference = "http://www.legislation.govt.nz/act/public/1977/0061/latest/DLM443855.html"

    def formula(persons, period, parameters):
        # that the applicant was present in New Zealand—
        # (i) for a minimum of 1350 days during the 5 years immediately preceding the date of the application; and
        required_days = parameters(period).citizenship.by_grant.minimum_days_present_for_each_of_preceeding_5_years

        meets_presence = True

        for n in range(0, 5):
            n_years_ago = period.offset(days_since_n_years_ago(period, n * -1))
            meets_presence_n_years_ago = (persons('days_present_in_new_zealand_in_preceeding_year', n_years_ago) >= required_days)

            meets_presence = meets_presence_n_years_ago * meets_presence

        return meets_presence


class citizenship__meets_5_year_presence_requirement(Variable):
    value_type = bool
    entity = Person
    definition_period = DAY

    label = u"was present in New Zealand for for a minimum of 1350 days during the 5 years immediately preceding the date of the application"
    reference = "http://www.legislation.govt.nz/act/public/1977/0061/latest/DLM443855.html"

    def formula(persons, period, parameters):
        # that the applicant was present in New Zealand—
        # (i)  and
        required_days = parameters(period).citizenship.by_grant.minimum_days_present_in_preceeding_5_years
        days_present = persons('days_present_in_new_zealand_in_preceeding_5_years', period)

        return (days_present >= required_days)


class days_present_in_new_zealand_in_preceeding_5_years(Variable):
    value_type = int
    entity = Person
    definition_period = DAY
    default_value = 0

    def formula(persons, period, parameters):

        sum = 0
        for offset in range((days_since_n_years_ago(period, 5) * -1), 1):
            p = period.offset(offset)
            sum += (persons('present_in_new_zealand', p) * 1)

        return sum


def days_since_n_years_ago(period, n=1):
    date_n_years_ago = period.date.replace(year=period.date.year - n)
    # The days in that rolling year could  be 365 or 366
    days = (period.date - date_n_years_ago).days - 1  # subtract one to not include that day
    return days


class days_present_in_new_zealand_in_preceeding_year(Variable):
    value_type = int
    entity = Person
    definition_period = DAY
    label = u"was present this many days in the last year"
    reference = "Accumlative from `present_in_new_zealand` variable`"
    default_value = 0

    def formula(persons, period, parameters):

        sum = 0

        # print("{} to {} = {} days".format(one_year_ago, period.date, days_since_n_years_ago))
        for p in [period.offset(offset) for offset in range((days_since_n_years_ago(period) * -1), 1)]:
            sum += (persons('present_in_new_zealand', p) * 1)

        return sum


class present_in_new_zealand(Variable):
    value_type = bool
    entity = Person
    definition_period = DAY
    default_value = False
    label = u"was present in New Zealand on this day"
    reference = "http://www.legislation.govt.nz/act/public/1977/0061/latest/DLM443855.html"


class immigration__holds_indefinite_stay_visa(Variable):
    value_type = bool
    entity = Person
    definition_period = DAY
    label = u"is entitled in terms of the Immigration Act 2009 to be in New Zealand indefinitely"
    reference = "http://www.legislation.govt.nz/act/public/1977/0061/latest/DLM443855.html"


class citizenship__is_of_good_character(Variable):
    value_type = bool
    entity = Person
    definition_period = ETERNITY
    label = u"is of good character"
    reference = ["http://www.legislation.govt.nz/act/public/1977/0061/latest/DLM443855.html", "http://www.legislation.govt.nz/act/public/1977/0061/latest/DLM443872.html"]


class citizenship__has_sufficient_knowledge_of_the_responsibilities_and_privileges_attaching_to_nz_citizenship(Variable):
    value_type = bool
    entity = Person
    definition_period = ETERNITY
    label = u"has sufficient knowledge of the responsibilities and privileges attaching to New Zealand citizenship"
    reference = "http://www.legislation.govt.nz/act/public/1977/0061/latest/DLM443855.html"


class citizenship__has_sufficient_knowledge_of_the_english_language(Variable):
    value_type = bool
    entity = Person
    definition_period = ETERNITY
    label = u"has sufficient knowledge of the English language"
    reference = "http://www.legislation.govt.nz/act/public/1977/0061/latest/DLM443855.html"


class citizenship__intends_to_reside_in_nz(Variable):
    value_type = bool
    entity = Person
    definition_period = ETERNITY
    label = u"intends to continue to reside in New Zealand"
    reference = "http://www.legislation.govt.nz/act/public/1977/0061/latest/DLM443855.html"


class citizenship__intends_crown_service(Variable):
    value_type = bool
    entity = Person
    definition_period = ETERNITY
    label = u"intends to enter into or continue in Crown service under the New Zealand Government"
    reference = "http://www.legislation.govt.nz/act/public/1977/0061/latest/DLM443855.html"


class citizenship__intends_international_service(Variable):
    value_type = bool
    entity = Person
    definition_period = ETERNITY
    label = u"intends to enter into or continue service under an international organisation of which the New Zealand Government is a member"
    reference = "http://www.legislation.govt.nz/act/public/1977/0061/latest/DLM443855.html"


class citizenship__intends_nz_employment(Variable):
    value_type = bool
    entity = Person
    definition_period = ETERNITY
    label = u"intends to enter into or continue service in the employment of a person, company, society, or other body of persons resident or established in New Zealand"
    reference = "http://www.legislation.govt.nz/act/public/1977/0061/latest/DLM443855.html"
