from openfisca_core.model_api import *
from openfisca_aotearoa.entities import Person


class on_continental_shelf(Variable):
    value_type = bool
    entity = Person
    definition_period = DAY
    reference = "http://www.legislation.govt.nz/act/public/1964/0028/latest/DLM351644.html"
    label = "on the seabed and subsoil of those submarine areas that extend beyond the territorial limits of New Zealand, throughout the natural prolongation of the land territory of New Zealand, to the seaward-side boundaries"
