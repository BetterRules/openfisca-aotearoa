# Import from openfisca-core the common python objects used to code the legislation in OpenFisca
from openfisca_core.model_api import *
# Import the entities specifically defined for this tax and benefit system
from openfisca_aotearoa.entities import Person


class citizen(Variable):
    value_type = bool
    entity = Person
    definition_period = ETERNITY
    label = u"Number of Persons classified as dependant for the purposes of rates rebates"
    reference = "http://www.legislation.govt.nz/act/public/1977/0061/latest/whole.html"
