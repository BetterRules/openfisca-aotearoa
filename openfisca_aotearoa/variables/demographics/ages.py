# -*- coding: utf-8 -*-

# Import from openfisca-core the common python objects used to code the legislation in OpenFisca
from openfisca_core.model_api import *
# Import the entities specifically defined for this tax and benefit system
from openfisca_aotearoa.entities import Person, Family


# This variable is a pure input: it doesn't have a formula
class date_of_birth(Variable):
    base_function = missing_value
    value_type = date
    entity = Person
    label = u"Birth date"
    definition_period = ETERNITY  # This variable cannot change over time.
    reference = u"https://en.wiktionary.org/wiki/birthdate"


# This variable is a pure input: it doesn't have a formula
class due_date_of_birth(Variable):
    value_type = date
    entity = Person
    label = u"Birth due date"
    definition_period = ETERNITY  # This variable cannot change over time.
    reference = u""


class age(Variable):
    value_type = int
    entity = Person
    definition_period = DAY
    label = u"The age of a Person (in years)"
    unit = 'years'
    default_value = -9999
    # A person's age is computed according to their birth date.

    def formula(persons, period, parameters):
        birth = persons('date_of_birth', period)
        birth_year = birth.astype('datetime64[Y]').astype(int) + 1970
        birth_month = birth.astype('datetime64[M]').astype(int) % 12 + 1
        birth_day = (birth - birth.astype('datetime64[M]') + 1).astype(int)

        is_birthday_past = (birth_month < period.start.month) + (birth_month == period.start.month) * (birth_day <= period.start.day)
        return (period.start.year - birth_year) - where(is_birthday_past, 0, 1)  # If the birthday is not passed this year, substract one year


class age_of_youngest(Variable):
    value_type = int
    entity = Family
    definition_period = DAY
    unit = 'years'
    label = u"The age of the youngest member of a family"
    # A person's age is computed according to their birth date.

    def formula(families, period, parameters):
        return families.min(families.members("age", period))


class age_of_partner(Variable):
    value_type = int
    entity = Person
    definition_period = DAY
    unit = 'years'
    label = u"The age of partner in a family"

    def formula(persons, period, parameters):
        return persons.family.members("age", period, role=Family.PARTNER)
