# -*- coding: utf-8 -*-

from openfisca_core.model_api import *
from openfisca_aotearoa.entities import Person
from numpy import logical_not


class acc__earner(Variable):
    value_type = bool
    entity = Person
    definition_period = ETERNITY
    label = u"A natural person who engages in employment"
    reference = "http://www.legislation.govt.nz/act/public/2001/0049/latest/DLM100103.html#DLM100167"


class acc__potential_earner(Variable):
    value_type = bool
    entity = Person
    definition_period = ETERNITY
    label = u"Is a potential earner"
    reference = "http://www.legislation.govt.nz/act/public/2001/0049/latest/DLM100103.html#DLM100322"

    def formula(persons, period, parameters):
        birth = persons('date_of_birth', period)
        eighteenth_year = birth.astype('datetime64[Y]').astype(int) + 1970 + 18
        eighteenth_month = birth.astype('datetime64[M]').astype(int) % 12 + 1
        eighteenth_day = (birth - birth.astype('datetime64[M]') + 1).astype(int)\

        date_of_injury = persons('date_of_injury', period)
        injury_year = date_of_injury.astype('datetime64[Y]').astype(int) + 1970
        injury_month = date_of_injury.astype('datetime64[M]').astype(int) % 12 + 1
        injury_day = (date_of_injury - date_of_injury.astype('datetime64[M]') + 1).astype(int)\

        injured_under_18 = ((injury_year < eighteenth_year)
                            + ((injury_year == eighteenth_year) * (injury_month < eighteenth_month))
                            + ((injury_year == eighteenth_year) * (injury_month == eighteenth_month) * (injury_day < eighteenth_day))
                            ) > 0

        finish_date = persons('finish_date_of_full_time_study_training_bridging_18th_birthday', period)
        finish_year = finish_date.astype('datetime64[Y]').astype(int) + 1970
        finish_month = finish_date.astype('datetime64[M]').astype(int) % 12 + 1
        finish_day = (finish_date - finish_date.astype('datetime64[M]') + 1).astype(int)\

        injured_while_studying = ((injury_year < finish_year)
                                  + ((injury_year == finish_year) * (injury_month < finish_month))
                                  + ((injury_year == finish_year) * (injury_month == finish_month) * (injury_day <= finish_day))
                                  ) > 0

        injured_over_18_in_study = logical_not(injured_under_18) * injured_while_studying

        return (injured_under_18 + injured_over_18_in_study) > 0
