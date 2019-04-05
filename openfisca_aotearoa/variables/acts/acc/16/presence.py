from openfisca_core.model_api import *
from openfisca_aotearoa.entities import Person


class acc__is_present_in_new_zealand(Variable):
    value_type = bool
    entity = Person
    definition_period = DAY

    def formula(persons, period, parameters):

        longitude = persons('longitude', period)
        latitude = persons('latitude', period)
        return (
            persons('in_the_north_island', period)
            + persons('in_the_south_island', period)
            + persons('on_stewart_island', period)
            + persons('in_the_chatham_islands', period)
            # between the 162nd degree of east longitude and the 173rd degree of west longitude
            # and between the 33rd and 53rd parallels of south latitude; and
            + ((longitude >= 162) * (longitude <= 173) * (latitude >= 33) * (latitude <= 53))
            # (b) those islands situated in the South Pacific Ocean lying
            # between the 177th and 180th degrees of west longitude and between the 29th and 32nd parallels of south latitude,
            # commonly known as the Kermadec Group; and
            + ((longitude >= 177) * (longitude <= 180) * (latitude >= 29) * (latitude <= 32))
            + persons('within_the_internal_waters_of_new_zealand', period)
            + persons('within_territorial_sea_of_new_zealand_adjacent', period)
            + persons('acc__on_drilling_rig_or_installation_continental_shelf_adjacent', period)
            )


class acc__number_of_days_outside_new_zealand(Variable):
    value_type = int
    entity = Person
    definition_period = DAY

    def formula(persons, period, parameters):
        # TODO calculate from last time they left
        return (persons('acc__is_present_in_new_zealand', period) * 0)


class acc__on_drilling_rig_or_installation_continental_shelf_adjacent(Variable):
    value_type = bool
    entity = Person
    definition_period = DAY
    label = """
    any installation or drilling rig that—
    (i) is constructed, erected, placed, or used in, on, or above those parts of the continental shelf adjacent to the land territories, islands, and islets referred to in paragraphs (a) and (b); and
    (ii) has the purpose of the exploration of the continental shelf or the exploitation of the mineral or other natural non-living resources of the continental shelf.
    """

    def formula(persons, period, parameters):
        return persons('acc__on_drilling_rig_or_installation', period) + persons('on_continental_shelf', period)


class acc__on_drilling_rig_or_installation(Variable):
    value_type = bool
    entity = Person
    definition_period = DAY

    label = """
    (ii) any installation or drilling rig, whether permanent or temporary:
    (ii) any aircraft, floating platform, ship, or other device that is for the time being in, on, or above the continental shelf and is being used in connection with any installation or drilling rig.
    """

