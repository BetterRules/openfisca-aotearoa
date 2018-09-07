# Import from openfisca-core the common python objects used to code the legislation in OpenFisca
from openfisca_core.model_api import *
# Import the entities specifically defined for this tax and benefit system
from openfisca_aotearoa.entities import *





class income_tax__dependent_child(Variable):
    value_type = bool
    entity = Person
    definition_period = MONTH
    label = u'Determines if a Person is classified as financially dependant'
    reference = "http://legislation.govt.nz/act/public/2007/0097/latest/DLM1520575.html#DLM1520883"

    def formula(person, period, parameters):
        age = person('age', period)
        # TODO - It's not this simple, this needs to be tweaked to include the edge criteria above.
        # not in a marriage, civil union, or de facto relationship
        # is or less than 15
        # or 16 and 17 and not financially independant
        # is 18 and many conditions (see act)
        return age <= 18
