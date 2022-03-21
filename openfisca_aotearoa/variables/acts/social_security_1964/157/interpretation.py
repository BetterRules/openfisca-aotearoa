# -*- coding: utf-8 -*-

from openfisca_core.model_api import *
from openfisca_aotearoa.entities import Person


class social_security__spouse_is_a_specified_beneficiary(Variable):
    value_type = bool
    entity = Person
    definition_period = MONTH
    label = """his or her spouse is a specified beneficiary within the meaning of paragraphs (b) to (d) of the definition
        of that term in section 157."""
    reference = u"""
    specified beneficiary means a person who is married, in a civil union, or in a de facto relationship and
        receives in his or her own right
    (a) [Repealed]
    (b) an emergency benefit, supported living payment under section 40B, or jobseeker support; or
    (c) New Zealand superannuation paid at a rate specified in clause 2 of Schedule 1 of the New
        Zealand Superannuation and Retirement Income Act 2001; or
    (d) a veteran’s pension at the relationship (partner not receiving superannuation or pension) rate or
        the relationship (partner not receiving superannuation or pension) legacy rate (as defined in
        section 158 of the Veterans’ Support Act 2014)
        http://legislation.govt.nz/act/public/1964/0136/latest/DLM4686046.html#DLM4686046
    """
