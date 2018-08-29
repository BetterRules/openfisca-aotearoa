# -*- coding: utf-8 -*-

from openfisca_core.model_api import *
from openfisca_aotearoa.entities import Person


class social_security__meets_young_parent_payment_in_relationship_requirements(Variable):
    value_type = bool
    entity = Person
    definition_period = MONTH
    label = "Meets Young Parent Payment single person requirements from section 165"
    reference = u"""
        Young parent payment: persons who are or have been married, or in civil union or de facto relationship
        (a) he or she is not married, or in a civil union or de facto relationship, but has been married or in
        a civil union or de facto relationship; or

        (b) he or she is married, or in a civil union or a de facto relationship, but his or her spouse or partner
            is not a specified beneficiary within the meaning of paragraphs (b) to (d) of the definition of that term in section 157.
        legislation.govt.nz/act/public/1964/0136/latest/whole.html#DLM4686082
    """

    def formula(persons, period, parameters):
        in_relationship = (persons('is_married_or_in_a_civil_union_or_de_facto_relationship', period))
        was_in_relationship = persons('has_been_married_or_in_a_civil_union_or_de_facto_relationship', period)

        spouse_is_a_specified_beneficiary = persons('social_security__spouse_is_a_specified_beneficiary', period)

        return (not_(in_relationship) * was_in_relationship) + (in_relationship * not_(spouse_is_a_specified_beneficiary))
